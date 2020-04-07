<template>
  <v-card color="rgba(255,255,255,.1)" class="d-flex flex-column pa-5" max-width="400">
    <v-img src="@/assets/dice.png" width="100" />
    <v-card-title class="headerTitle d-flex">
      Dart
      <div class="primary--text">s</div>live theme
    </v-card-title>

    <v-card-text>
      <v-text-field v-if="isFirebase" dense placeholder="ID" type="text" v-model="email" />
      <v-text-field
        v-if="isFirebase"
        dense
        placeholder="PASSWORD"
        type="password"
        v-model="password"
      />
      <div class="my-5 primary--text">{{ errorMessage }}</div>
      <v-btn width="100%" outlined @click="login">sign in</v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
import { auth } from "firebase/app";

import store from "@/store/index.js";
import config from "@/config/config";

export default {
  name: "LoginForm",

  data: () => ({
    email: "",
    password: "",
    errorMessage: ""
  }),

  computed: {
    isFirebase() {
      return config.ENV === "firebase";
    }
  },

  methods: {
    login() {
      if (config.ENV === "firebase") {
        auth()
          .signInWithEmailAndPassword(this.email, this.password)
          .then(result => {
            console.log("success", result);
            store.commit("sigin", result.user);
          })
          .catch(error => {
            console.log("login error", error);
            this.errorMessage = "認証エラーです。";
          });
      } else if (config.ENV === "local") {
        store.commit("sigin", {});
      } else {
        console.log("invalid config.env");
      }
    }
  }
};
</script>

<style scoped>
@import "https://fonts.googleapis.com/css?family=Russo+One&display=swap";

.headerTitle {
  font-family: "Russo One";
}
</style>
