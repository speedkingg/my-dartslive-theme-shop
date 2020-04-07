import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import { database } from "firebase/app";
import axios from "axios";
import config from "@/config/config";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isSigin: false,
    userId: "",
    favoriteThemes: {},
    favoriteThemeCounts: {}
  },
  mutations: {
    sigin(state, user) {
      state.isSigin = true;
      if (config.ENV === "firebase") {
        state.userId = user.email.replace(".", "-");
      } else if (config.ENV === "local") {
        state.userId = "local";
      } else {
        console.error("invalid environment congig:", config.ENV);
      }
    },
    signout(state) {
      state.isSigin = false;
      state.userId = "";
    },
    updateFavoriteThemes(state, favoriteThemes) {
      state.favoriteThemes = favoriteThemes;
    },
    updateFavoriteThemeCounts(state, favoriteThemeCounts) {
      state.favoriteThemeCounts = favoriteThemeCounts;
    }
  },
  getters: {
    isSignin: state => {
      return state.isSigin;
    },
    userId: state => {
      return state.userId;
    },
    favoriteThemes: state => {
      return state.favoriteThemes;
    },
    favoriteThemeCounts: state => {
      return state.favoriteThemeCounts;
    }
  },
  actions: {
    getFavoriteThemes(context) {
      if (config.ENV === "firebase") {
        database()
          .ref(`user/${context.state.userId}/themes`)
          .once("value")
          .then(snapshot => {
            context.commit("updateFavoriteThemes", snapshot.val());
          });
      } else if (config.ENV === "local") {
        axios.get(`${config.DB_LOCAL_HOST}/favorite`).then(response => {
          context.commit("updateFavoriteThemes", response.data);
        });
      } else {
        console.error("invalid environment congig:", config.ENV);
      }
    }
  },
  modules: {},
  plugins: [createPersistedState({ storage: window.sessionStorage })]
});
