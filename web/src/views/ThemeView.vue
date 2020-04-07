<template>
  <v-container>
    <Header />

    <v-content>
      <v-layout>
        <v-tabs centered icons-and-text>
          <v-tab>
            Usage
            <v-icon>mdi-information-outline</v-icon>
          </v-tab>
          <v-tab>
            Picture
            <v-icon>mdi-image-area</v-icon>
          </v-tab>
          <v-tab>
            Movie
            <v-icon>mdi-image-area</v-icon>
          </v-tab>
          <v-tab>
            App
            <v-icon>mdi-image-area</v-icon>
          </v-tab>
          <v-tab>
            Special
            <v-icon>mdi-image-area</v-icon>
          </v-tab>
          <v-tab>
            Limited
            <v-icon>mdi-image-off</v-icon>
          </v-tab>
          <v-tab>
            Search
            <v-icon>mdi-image-search-outline</v-icon>
          </v-tab>
          <v-tab>
            Favorite
            <v-icon>mdi-heart</v-icon>
          </v-tab>

          <v-tab-item class="tabItem">
            <Usage />
          </v-tab-item>
          <v-tab-item>
            <ThemeList
              :category-name="`Picture`"
              :queryKey="`price`"
              :queryValue="`120`"
              class="tabItem"
            />
          </v-tab-item>
          <v-tab-item>
            <ThemeList
              :category-name="`Movie`"
              :queryKey="`price`"
              :queryValue="`480`"
              class="tabItem"
            />
          </v-tab-item>
          <v-tab-item>
            <ThemeList
              :category-name="`App`"
              :queryKey="`price`"
              :queryValue="`800`"
              class="tabItem"
            />
          </v-tab-item>
          <v-tab-item>
            <ThemeList
              :category-name="`Special`"
              :queryKey="`price`"
              :queryValue="`1600`"
              class="tabItem"
            />
          </v-tab-item>
          <v-tab-item>
            <ThemeList
              :category-name="`Limited`"
              :queryKey="`can_buy`"
              :queryValue="`False`"
              class="tabItem"
            />
          </v-tab-item>
          <v-tab-item>
            <Search class="tabItem" />
          </v-tab-item>
          <v-tab-item>
            <Favorite class="tabItem" />
          </v-tab-item>
        </v-tabs>
      </v-layout>
    </v-content>
  </v-container>
</template>

<script>
import Header from "@/components/Header";
import Usage from "@/components/Usage";
import ThemeList from "@/components/ThemeList";
import Search from "@/components/Search";
import Favorite from "@/components/FavoriteThemeList";

import store from "@/store/index.js";

export default {
  name: "ThemeView",
  components: {
    ThemeList,
    Search,
    Favorite,
    Usage,
    Header
  },
  data: () => ({}),
  computed: {},
  created() {
    store.dispatch("getFavoriteThemes");
  }
};
</script>

<style scoped>
.tabItem {
  min-height: 80vh;
}
</style>
