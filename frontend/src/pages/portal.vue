<script setup lang="ts">
import Toolbar from "@/components/toolbar.vue"

import Button from "primevue/button";
</script>

<template>
  <div class="p-grid">
  	<div class="p-col-3">
      <Toolbar/>
    </div>
  	<div class="p-col-9">
      <h2>Login</h2>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@600&family=Raleway:wght@300;400;600&display=swap");
h2 {
  background-color: red
}
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
