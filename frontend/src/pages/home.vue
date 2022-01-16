<script setup lang="ts">
import Title from "@/components/title.vue";

import Button from "primevue/button";
import VVanta from 'vue-vanta';

const options = {
            mouseControls: true,
            touchControls: true,
            minHeight: 500.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00
        }

</script>

<template>
  <v-vanta effect="globe" :options=options></v-vanta>
  <div class="p-grid" id="container">
  	<div class="p-col-6 sidebar">
      <Title />
    </div>
  	<div class="p-col-6">
      <Button class="btn" @click="$router.push('map')" label="View Map" />
      <br />
      <Button class="btn" @click="$router.push('send')" label="Send safety check" />
    </div>
  </div>
</template>

<style scoped>
.sidebar {
    background-color: var(--secondary);
    width: 50vw;
    height: 100vh;
}
</style>
