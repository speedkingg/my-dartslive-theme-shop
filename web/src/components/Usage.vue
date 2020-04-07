<template>
  <div class="pa-4">
    <div class="caption blue-grey--text text--lighten-4">v0.1.4 - {{ env }}</div>

    <div class="my-2 title">
      <v-icon left color="secondary">mdi-information-outline</v-icon>使い方
    </div>
    <div
      class="caption blue-grey--text text--lighten-4"
    >・テーマの画像をクリックすると、お気に入りリストに飛ぶので、そちらから購入してください。</div>
    <div class="mt-2 caption blue-grey--text text--lighten-4">・購入する際は、同じブラウザでダーツライブへログインしている必要がります。</div>

    <div class="mt-10 mb-2 title">
      <v-icon left color="secondary">mdi-alert-outline</v-icon>注意
    </div>
    <div class="caption blue-grey--text text--lighten-4">
      ・本コンテンツは 2020/02/12
      にクロールした結果を参照しています。リンク先にテーマが存在しない場合もございますのでご容赦ください。
    </div>

    <div class="mt-10 body-2">
      <v-icon left x-large color="primary">mdi-gesture-swipe-left</v-icon>左にスワイプしてテーマを探しましょう！
    </div>

    <div class="mt-10 mb-2 title">
      <v-icon left color="secondary">mdi-dice-multiple</v-icon>テーマ数
    </div>
    <UsageItemThemeCount class="mx-5" />

    <div class="mt-10 my-2 title">
      <v-icon left color="secondary">mdi-update</v-icon>Update
    </div>
    <div class="subtitle-1 blue-grey--text text--lighten-4 ml-5">- v0.1.2</div>
    <div class="caption blue-grey--text text--lighten-4 ml-10 d-flex flex-column">
      <div>・Limited(購入不可) 追加</div>
      <div>・テーマ数増加</div>
    </div>

    <div class="subtitle-1 blue-grey--text text--lighten-4 ml-5">- v0.1.3</div>
    <div class="caption blue-grey--text text--lighten-4 ml-10 d-flex flex-column">
      <div>・Search(検索機能) 追加</div>
    </div>

    <div class="subtitle-1 blue-grey--text text--lighten-4 ml-5">- v0.1.4</div>
    <div class="caption blue-grey--text text--lighten-4 ml-10 d-flex flex-column">
      <div>・Favorite(お気に入り機能) 追加</div>
      <div>・タブアイコン追加</div>
    </div>
  </div>
</template>

<script>
import UsageItemThemeCount from "@/components/UsageItemThemeCount";
import config from "@/config/config";

export default {
  name: "Usage",
  components: {
    UsageItemThemeCount
  },

  data: () => ({}),

  computed: {
    env() {
      return config.ENV;
    }
  },
  methods: {}
};
</script>

<style scoped></style>
