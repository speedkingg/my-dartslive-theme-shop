<template>
  <div>
    <Loading v-if="isLoading" />

    <ThemeListItem
      v-else
      :id="theme.id"
      :theme-name="theme.theme_name"
      :theme-image-name="theme.img_file_name"
      :user-id="theme.user_id"
      :price="theme.price"
      :can-buy="theme.can_buy"
    />
  </div>
</template>

<script>
import { database } from "firebase/app";

import Loading from "@/components/Utils/Loading";
import ThemeListItem from "@/components/ThemeListItem";

export default {
  name: "FavoriteThemeListItem",
  components: { ThemeListItem, Loading },

  props: {
    themeId: {
      type: String,
      require: true
    }
  },

  data: () => ({
    theme: {},
    isLoading: true
  }),

  created() {
    database()
      .ref(`theme/`)
      .orderByChild("id")
      .equalTo(this.themeId)
      .once("value")
      .then(snapshot => {
        const res = snapshot.val();
        // length=1 を想定
        for (const key in res) {
          this.theme = res[key];
          this.isLoading = false;
          break;
        }
      });
  }
};
</script>

<style scoped>
</style>

