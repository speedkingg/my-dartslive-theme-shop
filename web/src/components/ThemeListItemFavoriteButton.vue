<template>
  <div>
    <v-btn text icon @click="changeFavorite()" :disabled="isDisable">
      <v-icon color="blue-grey" v-show="!isFavorite">mdi-heart-outline</v-icon>
      <v-icon color="primary" v-show="isFavorite">mdi-heart</v-icon>
    </v-btn>
  </div>
</template>

<script>
import { database } from "firebase/app";
import axios from "axios";
import config from "@/config/config";
import store from "@/store/index.js";

export default {
  name: "ThemeListItem",

  props: {
    themeId: {
      type: String,
      require: true
    }
  },

  data: () => ({
    isFavorite: Boolean,
    isDisable: false // 連打対策
  }),

  computed: {
    favoriteThemes() {
      return store.getters.favoriteThemes;
    }
  },

  methods: {
    changeFavorite() {
      if (config.ENV === "firebase") {
        if (!this.isFavorite) {
          this.postToFirebase();
        } else {
          this.deleteToFirebase();
        }
      } else if (config.ENV === "local") {
        if (!this.isFavorite) {
          this.postToLocal();
        } else {
          this.deleteToLocal();
        }
      } else {
        console.log("invalid config.env");
      }

      this.isFavorite = !this.isFavorite;
    },
    postToFirebase() {
      const userId = store.getters.userId;
      this.isDisable = true;
      database()
        .ref(`user/${userId}/themes/${this.themeId}`)
        .set(true)
        .then(res => {
          store.dispatch("getFavoriteThemes");
          this.isDisable = false;
        });
    },
    deleteToFirebase() {
      const userId = store.getters.userId;
      this.isDisable = true;
      database()
        .ref(`user/${userId}/themes/${this.themeId}`)
        .remove()
        .then(res => {
          store.dispatch("getFavoriteThemes");
          this.isDisable = false;
        });
    },
    postToLocal() {
      this.isDisable = true;
      axios.get(`${config.DB_LOCAL_HOST}/favorite`).then(res => {
        const favoriteThemes = res.data;
        favoriteThemes[this.themeId] = true;
        axios
          .post(`${config.DB_LOCAL_HOST}/favorite`, favoriteThemes)
          .then(res => {
            store.dispatch("getFavoriteThemes");
            this.isDisable = false;
          });
      });
    },
    deleteToLocal() {
      this.isDisable = true;
      axios.get(`${config.DB_LOCAL_HOST}/favorite`).then(res => {
        const favoriteThemes = res.data;
        delete favoriteThemes[this.themeId];
        axios
          .post(`${config.DB_LOCAL_HOST}/favorite`, favoriteThemes)
          .then(res => {
            store.dispatch("getFavoriteThemes");
            this.isDisable = false;
          });
      });
    },

    updateIsFavorite() {
      if (this.favoriteThemes) {
        return this.favoriteThemes.hasOwnProperty(this.themeId);
      } else {
        false;
      }
    }
  },
  created() {
    this.isFavorite = this.updateIsFavorite();
  },
  watch: {
    favoriteThemes() {
      this.isFavorite = this.updateIsFavorite();
    }
  }
};
</script>

<style scoped></style>
