<template>
  <v-sheet max-width="300">
    <v-simple-table dense>
      <tbody>
        <tr v-for="(count, key) in themeCounts" :key="key">
          <td>{{ key }}：</td>
          <td>{{ count }}</td>
        </tr>
      </tbody>
    </v-simple-table>
  </v-sheet>
</template>

<script>
import { database } from "firebase/app";
import axios from "axios";

import config from "@/config/config";
import store from "@/store/index.js";

export default {
  name: "UsageItemThemeCount",

  data: () => ({
    headers: [
      { text: "Name", value: "name" },
      { text: "Count", value: "count" }
    ],
    themeCounts: {
      Picture: 0,
      Movie: 0,
      App: 0,
      Special: 0,
      Limited: 0
    }
  }),

  computed: {},
  methods: {
    getThemeListCount: async function(queryKey, queryValue) {
      if (config.ENV === "firebase") {
        return database()
          .refFromURL(`https://dartslive-theme.firebaseio.com/theme`)
          .orderByChild(queryKey)
          .equalTo(queryValue)
          .once("value")
          .then(snapshot => {
            return Object.keys(snapshot.val()).length;
          });
      } else if (config.ENV === "local") {
        return axios
          .get(`${config.DB_LOCAL_HOST}/theme?${queryKey}=${queryValue}`)
          .then(response => {
            return response.data.length;
          });
      } else {
        console.log("invalid config.env");
      }
    }
  },
  created: async function() {
    this.themeCounts.Picture = await this.getThemeListCount("price", "120");
    this.themeCounts.Movie = await this.getThemeListCount("price", "480");
    this.themeCounts.App = await this.getThemeListCount("price", "800");
    this.themeCounts.Special = await this.getThemeListCount("price", "1600");
    this.themeCounts.Limited = await this.getThemeListCount("can_buy", "False");
    store.commit("updateFavoriteThemeCounts", this.themeCounts);
  }
};
</script>

<style scoped></style>
