<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      class="px-5"
    >
      <div class="d-flex align-center">
        <h2 class="font-weight-regular">MyMusciList</h2>
      </div>

      <v-spacer></v-spacer>

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn
            href="https://github.com/NobeKanai/netease_backup"
            target="_blank"
            text
            icon
            v-on="on"
          >
            <v-icon>mdi-github</v-icon>
          </v-btn>
        </template>
        <span>
          GitHub
        </span>
      </v-tooltip>
    </v-app-bar>

    <v-content>
      <HelloWorld />
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",

  components: {
    HelloWorld
  },

  data: () => ({
    //
  })
};
</script>
