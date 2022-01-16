<script setup lang="ts">
import Title from "@/components/title.vue";

import Button from "primevue/button";
import VVanta from 'vue-vanta';

const options = {
            mouseControls: true,
            touchControls: true,
            minHeight: 1000.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x144470,
            waveSpeed: 1.20,
        }
</script>

<template>
  <div class="absolute">
    <Title/>
    <p>A visual application for getting people the help they need.</p>
    <Button class="btn" @click="$router.push('map')" label="View Map" />&nbsp
    <Button class="btn" @click="$router.push('send')" label="Send safety check" />
  </div>
  <v-vanta id="bg" effect="waves" :options=options></v-vanta>
</template>

<style scoped>
.absolute {
    position: absolute;
    left: 15vw;
    top: 30vh;
    font-size: 2em;
    width: 40vw;
    background-color: var(--secondary);
    padding: 1em;
}
.absolute > p {
  font-size: 0.7em;
  color: var(--primary-light);
}

#bg {
  color: #999999;
  width: 100vw;
  height: 120vh;
  position: fixed;
  z-index: -100;
}
</style>
