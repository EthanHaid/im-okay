<script setup lang="ts">
import Title from "@/components/title.vue";

import Button from "primevue/button";
import VVanta from 'vue-vanta';

const options = {
  mouseControls: true,
  touchControls: true,
  minHeight: 1440.00,
  minWidth: 200.00,
  scale: 1.00,
  scaleMobile: 1.00,
  color: 0x144470,
  waveSpeed: 1.20,
}
</script>

<template>
  <div class="absolute">
    <Title />
    <div class="row">
      <Button class="btn" @click="$router.push('status')" label="Check In" />
      <p>with emergency services</p>
    </div>
    <div class="row">
      <Button class="btn" @click="$router.push('request')" label="Request the Status" />
      <p>of someone in trouble</p>
    </div>
    <div class="row">
      <Button class="btn" @click="$router.push('map')" label="View the Map" />
      <p>of issues worldwide</p>
    </div>
  </div>
  <v-vanta id="bg" effect="waves" :options="options" />
</template>

<style scoped>
.absolute {
    position: absolute;
    left: 5%;
    top: 20%;
    font-size: 2em;
    min-width: 40vw;
    background-color: var(--secondary);
    padding: 1em;
}

.row {
  display: flex;
  flex-direction: row;
  margin: 0.5rem;
}

p {
  font-size: 0.7em;
  color: var(--primary-light);
  margin: 0.5rem;
}

#bg {
  color: #999999;
  width: 100vw;
  height: 120vh;
  position: fixed;
  z-index: -100;
}
</style>
