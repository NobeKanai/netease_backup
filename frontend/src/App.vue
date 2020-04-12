<template>
  <div id="app">
    <mu-appbar title="MyMusicList" text-color="#fff">
      <mu-tooltip content="GitHub" slot="right">
        <mu-button
          icon
          href="https://github.com/NobeKanai/netease_backup"
          target="_blank"
        >
          <mu-icon value=":fab fa-github"></mu-icon>
        </mu-button>
      </mu-tooltip>
    </mu-appbar>
    <hello-world></hello-world>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {
    HelloWorld: () => import("./components/HelloWorld")
  }
};
</script>

<style lang="sass">
#app
  color: #fff
  background-image: linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.25)), url("https://i.loli.net/2020/04/12/KhwRBueHkg3Vlps.jpg")
  background-position: center
  background-repeat: no-repeat
  background-attachment: fixed
  header
    background-color: rgba(255,255,255,0.2)
    backdrop-filter: blur(10px)
</style>
