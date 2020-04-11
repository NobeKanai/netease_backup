<template>
  <v-container class="fill-height">
    <v-row
      align="center"
      class="px-3 my-3"
    >
      <v-avatar
        size="100"
        class="mx-3"
      >
        <img
          src="http://www.gravatar.com/avatar/34b45a6df4eedeb6459f2688348d676f?size=100"
          alt="Kanai"
        >
      </v-avatar>
      <h1 class="font-weight-regular">Kanai's Music List</h1>
    </v-row>
    <v-card
      tile
      width="100%"
    >
      <v-list
        subheader
        two-line
        v-if="music"
      >
        <v-subheader>All {{ music.total }} songs</v-subheader>

        <v-list-item
          v-for="(item, i) in music.items"
          :key="i"
          :ripple="true"
          :href="`http://music.163.com/song?id=${item.id}&userid=500231854`"
          target="_blank"
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
    <v-row
      justify="center"
      class="mt-3"
    >
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
  data () {
    return {
      music: ""
    };
  },
  created () {
    this.getMusic();
  },
  methods: {
    getMusic (page = null) {
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
