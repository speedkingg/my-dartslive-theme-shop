<template>
  <v-app>
    <div class="backGroundImage" />
    <div class="filter" />
    <ThemeView v-if="isSignIn" />
    <LoginView v-else />
  </v-app>
</template>

<script>
import store from "@/store/index.js";
import ThemeView from "@/views/ThemeView.vue";
import LoginView from "@/views/LoginView.vue";

export default {
  name: "App",
  data: () => ({}),
  components: { ThemeView, LoginView },
  computed: {
    isSignIn() {
      return store.getters.isSignin;
    }
  }
};
</script>

<style>
#app {
  background-image: url("./assets/img/star.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  background-color: #999;
}
.filter {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  position: absolute;
  top: 0;
  left: 0;
}
</style>
