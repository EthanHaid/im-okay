<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import HelloWorld from './components/HelloWorld.vue'
import Map from '@/components/map.vue'
</script>

<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
  <!-- <HelloWorld msg="Hello Vue 3 + TypeScript + Vite" /> -->
  <Map />
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@600&family=Raleway:wght@300;400;600&display=swap");
:root {
  --primary: #ff6458;
  --primary-light: #ffd1ba;
  --secondary: #355497;
  --secondary-light: #6987c9;
  --light: #fdf6ed;
  --dark: #1a150f;
  --display-font: "Cabin", sans-serif;
  --text-font: "Raleway", sans-serif;
}

#app {
  font-family: var(--text-font);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #ffffff;
  color: var(--dark);
  margin-top: 60px;
}
</style>
