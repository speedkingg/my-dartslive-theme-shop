<template>
  <v-card color="rgba(255,255,255,.1)">
    <v-card-text>
      <a :href="`${favoriteUrl}${userId}`" class="cursor" target="_blank">
        <v-img class="mx-auto" :src="src" width="150" height="94" />
      </a>
      <div class="mx-auto subtitle-1">{{ themeName }}</div>
      <div class="d-flex">
        <div v-if="canBuy === 'True'" class="mx-auto">
          <v-icon color="orange darken-3" small left>mdi-coin</v-icon>
          {{ price }}
        </div>
        <div v-else class="blue-grey--text subtitle-2">購入不可</div>
        <v-spacer />
        <FavoriteButton :theme-id="id" />
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import { storage } from "firebase/app";

import FavoriteButton from "@/components/ThemeListItemFavoriteButton";
import config from "@/config/config";
import store from "@/store/index.js";

export default {
  name: "ThemeListItem",
  components: {
    FavoriteButton
  },

  props: {
    id: {
      type: String,
      require: true
    },
    themeName: {
      type: String,
      require: true
    },
    themeImageName: {
      type: String,
      require: true
    },
    userId: {
      type: String,
      require: true
    },
    price: {
      type: String,
      require: true
    },
    canBuy: {
      type: String,
      require: true
    }
  },

  data: () => ({
    src: ""
  }),

  computed: {
    favoriteUrl() {
      return config.BASE_FAVORITE_URL;
    }
  },

  methods: {
    getImage(imgName) {
      if (config.ENV === "firebase") {
        storage()
          .ref()
          .child(`dartslive_theme/${imgName}`)
          .getDownloadURL()
          .then(url => (this.src = url));
      } else if (config.ENV === "local") {
        this.src = `${config.WEB_LOCAL_HOST}/img/${imgName}`;
      } else {
        console.log("invalid config.env");
      }
    }
  },
  created() {
    this.getImage(this.themeImageName);
  }
};
</script>

<style scoped></style>
