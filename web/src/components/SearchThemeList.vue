<template>
  <div>
    <Loading v-if="isLoading" />

    <div v-else>
      <v-row class="d-flex flex-wrap">
        <v-col
          cols="6"
          sm="4"
          md="3"
          lg="2"
          xl="2"
          v-for="(item, key) in themeList"
          :key="key"
          v-show="item && item.theme_name.indexOf(filterValue) !== -1 || !isFirebase"
        >
          <!-- firebaseは、部分一致がなかっため、`startAt`で前方一致検索し、javascriptでキーワードを絞り込む -->
          <ThemeListItem
            v-if="item && item.theme_name.indexOf(filterValue) !== -1 || !isFirebase"
            :id="item.id"
            :theme-name="item.theme_name"
            :theme-image-name="item.img_file_name"
            :user-id="item.user_id"
            :price="item.price"
            :can-buy="item.can_buy"
          />
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import { database } from "firebase/app";
import axios from "axios";

import ThemeListItem from "@/components/ThemeListItem";
import Loading from "@/components/Utils/Loading";
import config from "@/config/config";

export default {
  name: "SearchThemeList",
  components: {
    ThemeListItem,
    Loading
  },

  props: {
    queryKey: {
      type: String,
      require: false
    },
    queryValue: {
      type: String,
      require: false
    },
    filterValue: {
      type: String,
      require: false
    }
  },

  data: () => ({
    themeList: {},
    isLoading: true,

    dispalayItemCount: 100
  }),

  computed: {
    isFirebase() {
      return config.ENV === "firebase";
    }
  },

  methods: {
    getThemeList: async function() {
      if (config.ENV === "firebase") {
        // 部分一致がなかっため、`startAt`で前方一致検索し、javascriptでキーワードを絞り込む
        database()
          .refFromURL(`https://dartslive-theme.firebaseio.com/theme`)
          .orderByChild(this.queryKey)
          .startAt(this.queryValue)
          .limitToFirst(this.dispalayItemCount)
          .once("value")
          .then(snapshot => {
            this.themeList = snapshot.val();
            if (this.isLoading) this.isLoading = false;
          });
      } else if (config.ENV === "local") {
        // 未実装
        // GET /posts?firstName_like=%ed%
        axios
          .get(
            `${config.DB_LOCAL_HOST}/theme?${this.queryKey}_like=${this.queryValue}`
          )
          .then(response => {
            this.themeList = response.data;
            if (this.isLoading) this.isLoading = false;
          });
      } else {
        console.log("invalid config.env");
      }
    }
  },
  created() {
    this.getThemeList();
  }
};
</script>

<style scoped>
</style>
