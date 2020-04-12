<template>
  <mu-container style="padding: 1rem 0 1rem 0;">
    <mu-flex align-items="center" justify-content="center">
      <mu-avatar :size="66">
        <img
          src="http://www.gravatar.com/avatar/34b45a6df4eedeb6459f2688348d676f"
          alt="Me"
        />
      </mu-avatar>
      <h1 style="font-weight: 300; margin-left: 20px">Kanai's Music List</h1>
    </mu-flex>
    <mu-list textline="two-line" v-show="music">
      <mu-list-item
        v-for="(item, i) in music.items"
        :key="i"
        button
        :href="`http://music.163.com/song?id=${item.id}&userid=500231854`"
        target="_blank"
      >
        <mu-list-item-content>
          <mu-list-item-title style="color: #f0f0f0">{{
            item.name
          }}</mu-list-item-title>
          <mu-list-item-sub-title style="color: #f0f0f0">{{
            item.author.join(", ")
          }}</mu-list-item-sub-title>
        </mu-list-item-content>
      </mu-list-item>
    </mu-list>
    <mu-flex justify-content="center" style="max-width: 95%">
      <mu-pagination
        @change="changePage($event)"
        :total="music.total"
        :current="music.page"
        :page-size="pageSize"
      ></mu-pagination>
    </mu-flex>
  </mu-container>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      music: "",
      pageSize: 20
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
    },
    changePage(page) {
      this.getMusic(page);
    }
  }
};
</script>
