<template>
  <v-container class="fill-height">
    <v-card tile class="mx-auto">
      <v-list subheader two-line flat :disabled="false" v-if="music">
        <v-subheader>All {{ music.total }} songs</v-subheader>

        <v-list-item
          v-for="(item, i) in music.items"
          :key="i"
          :ripple="true"
          :href="`http://music.163.com/song?id=${item.id}&userid=500231854`"
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.name }}</v-list-item-title>
            <v-list-item-subtitle>{{
              item.author.join(", ")
            }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>
    <v-row justify="center">
      <v-pagination
        v-model="music.page"
        :total-visible="10"
        :length="music.pages"
        @input="getMusic($event)"
      ></v-pagination>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      music: ""
    };
  },
  created() {
    this.getMusic();
  },
  methods: {
    getMusic(page = null) {
      const api = `/api/tracks/?page=${page || 1}`;

      this.$axios
        .get(api)
        .then(response => {
          this.music = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
