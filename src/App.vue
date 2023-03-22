<template>
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cabin&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <!-- <h1> The Thing From the Future </h1> -->
  <div id="app">
    <!-- <img  alt="The Thing From the Future logo" src="./assets/tftf_logo.jpeg" width="400"> -->
    <h1> The Thing From the Future </h1>
    <tftf/>
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
h1 {
  font-family: 'Bebas Neue', cursive;
  font-size: 400%; 
}
#app {
  font-family: 'Cabin', sans-serif;
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black; 
  /* color: #262626; */
  margin-top: 60px;
}
</style>
