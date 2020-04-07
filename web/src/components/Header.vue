<template>
  <v-app-bar app flat fixed color="rgba(255,255,255,.1)">
    <v-toolbar-title class="headerTitle d-flex">
      Dart
      <div class="primary--text">s</div>
      live theme
    </v-toolbar-title>
    <v-spacer />
    <v-toolbar-items>
      <v-btn @click="logout()" text>
        <v-icon left>mdi-logout</v-icon>sign out
      </v-btn></v-toolbar-items
    >
  </v-app-bar>
</template>

<script>
import store from "@/store/index.js";

export default {
  name: "Header",

  data: () => ({}),
  methods: {
    logout() {
      store.commit("signout");
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
