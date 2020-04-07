<template>
  <div>
    <v-row class="d-flex flex-wrap">
      <v-col
        cols="6"
        sm="4"
        md="3"
        lg="2"
        xl="2"
        v-for="(item, key) in favoriteThemes"
        :key="key"
        v-show="item"
      >
        <FavoriteThemeListItem :theme-id="key" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import FavoriteThemeListItem from "@/components/FavoriteThemeListItem";
import store from "@/store/index.js";

export default {
  name: "FavoriteThemeList",
  components: {
    FavoriteThemeListItem
  },
  computed: {
    favoriteThemes() {
      return store.getters.favoriteThemes;
    }
  }
};
</script>

<style scoped>
</style>
