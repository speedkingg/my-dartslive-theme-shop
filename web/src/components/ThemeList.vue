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
          v-show="item"
        >
          <ThemeListItem
            v-if="item"
            :id="item.id"
            :theme-name="item.theme_name"
            :theme-image-name="item.img_file_name"
            :user-id="item.user_id"
            :price="item.price"
            :can-buy="item.can_buy"
          />
        </v-col>
      </v-row>

      <v-card
        width="100%"
        class="d-flex justify-center align-center px-3"
        color="rgba(255,255,255,.1)"
        v-if="isDisplayMoreButton"
      >
        <v-btn color="primary" @click="addItem()" class="my-2" block outlined large>もっと見る</v-btn>
      </v-card>
      <div
        v-if="!themeList.length && !Object.keys(themeList).length"
        class="d-flex justify-center align-center flex-column"
      >
        <v-icon color="blue-grey" size="100" class="mt-12">mdi-alert-rhombus-outline</v-icon>
        <div class="blue-grey--text mt-3">テーマが登録されていません。</div>
      </div>
    </div>
  </div>
</template>

<script>
import { database } from "firebase/app";
import axios from "axios";

import ThemeListItem from "@/components/ThemeListItem";
import Loading from "@/components/Utils/Loading";
import config from "@/config/config";
import store from "@/store/index.js";

export default {
  name: "ThemeList",
  components: {
    ThemeListItem,
    Loading
  },

  props: {
    categoryName: {
      type: String,
      require: true
    },
    queryKey: {
      type: String,
      require: true
    },
    queryValue: {
      type: String,
      require: true
    }
  },

  data: () => ({
    themeList: [],
    isLoading: true,

    dispalayItemCount: 10,
    countIncrease: 10
  }),

  computed: {
    isDisplayMoreButton() {
      if (this.themeList) {
        return (
          //上限まで表示した時
          store.getters.favoriteThemeCounts[this.categoryName] !==
          Object.keys(this.themeList).length
        );
      } else {
        return false;
      }
    }
  },

  methods: {
    getThemeList: async function() {
      if (config.ENV === "firebase") {
        database()
          .ref(`theme/`)
          .orderByChild(this.queryKey)
          .equalTo(this.queryValue)
          .limitToFirst(this.dispalayItemCount)
          .once("value")
          .then(snapshot => {
            this.themeList = snapshot.val();
            if (this.isLoading) this.isLoading = false;
          });
      } else if (config.ENV === "local") {
        axios
          .get(
            `${config.DB_LOCAL_HOST}/theme?${this.queryKey}=${this.queryValue}&_limit=${this.dispalayItemCount}`
          )
          .then(response => {
            this.themeList = response.data;
            if (this.isLoading) this.isLoading = false;
          });
      } else {
        console.log("invalid config.env");
      }
    },
    addItem() {
      this.dispalayItemCount += this.countIncrease;
      this.getThemeList();
    }
  },
  created() {
    this.getThemeList();
  }
};
</script>

<style scoped>
</style>
