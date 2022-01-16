<script setup lang="ts">
import { ref } from 'vue';
import Map from "@/components/map.vue"

import Button from "primevue/button";
import Checkbox from 'primevue/checkbox';
import Sidebar from "primevue/sidebar";


const visibleRight = ref(false);
</script>

<template>
  <div>
    <Button label="Help" />
    <Button label="I'm Ok" />
  </div>
</template>

<style scoped>
div {
  background-image: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
  height: 100vh;
}

header {
    background-color: rgba(53, 84, 151, 0.75);
    position: fixed;
    top: 0;
    width: 100vw;
}
header > h1 {
  color: var(--cream);
  margin: 0.2em 0.5em;
}

#filter-button {
  position: fixed;
  bottom: 2em;
  right: 2em;
  background-color: var(--primary);
  border: none;
}
</style>
