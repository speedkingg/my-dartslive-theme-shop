<template>
  <div class="pa-4">
    <div class="my-2 title">
      <v-icon left color="primary">mdi-image-search-outline</v-icon>検索
    </div>
    <div class="caption blue-grey--text text--lighten-4 d-flex flex-column">
      <div v-if="isFirebase">・前方一致検索</div>
      <div v-if="isFirebase">・大文字/小文字、全角/半角を区別しています。</div>
      <div>・2文字以上で検索できます。</div>
      <div>・検索ワード例：「RATING」「おみくじ」「IC06」</div>
    </div>
    <div class="d-flex mx-5">
      <v-text-field v-model="queryValue" />
      <v-btn
        class="my-auto ml-2"
        outlined
        small
        color="primary"
        :disabled="searchable"
        @click="search()"
      >検索</v-btn>
    </div>

    <SearchThemeList
      :key="key"
      v-if="searchShow"
      :query-key="queryKey"
      :query-value="queryValue"
      :filter-value="key"
      class="tabItem"
    />
  </div>
</template>

<script>
import SearchThemeList from "@/components/SearchThemeList";
import config from "@/config/config";

export default {
  name: "Search",
  components: {
    SearchThemeList
  },

  data: () => ({
    queryKey: "theme_name",
    queryValue: "",

    searchShow: false,
    key: ""
  }),

  computed: {
    isFirebase() {
      return config.ENV === "firebase";
    },
    searchable() {
      return this.queryValue.length < 2;
    }
  },

  methods: {
    search() {
      if (!this.searchShow) this.searchShow = true;
      this.key = this.queryValue;
    }
  }
};
</script>

<style scoped>
</style>
