<template>
  <div id="app">
    <img alt="The Thing From the Future logo" src="./assets/tftf_logo.jpeg">
    <br>
    <br>
    <tftf msg="Wicked Problems, Wolfpack Solutions Edition"/>
  </div>
</template>

<script>
import tftf from './components/tftf.vue'

export default {
  name: 'App',
  components: {
    tftf
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #262626;
  margin-top: 60px;
}
</style>
