import Vue from "vue";
import Vuetify from "vuetify/lib";
import colors from "vuetify/lib/util/colors";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: true,
    themes: {
      dark: {
        primary: colors.pink.lighten2,
        secondary: colors.cyan.lighten2,
        accent: colors.yellow.lighten2,
        error: colors.red.lighten1
      }
    }
  }
});
