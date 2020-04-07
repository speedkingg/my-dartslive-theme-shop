<template>
  <v-container>
    <LoginForm class="mx-auto align-center" />
  </v-container>
</template>

<script>
import LoginForm from "@/components/LoginForm";

export default {
  name: "LoginView",
  components: {
    LoginForm
  },
  data: () => ({})
};
</script>
