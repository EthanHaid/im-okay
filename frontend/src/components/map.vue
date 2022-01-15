<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { Harp } from "@/services/harp";

const mapCanvas = ref();

onMounted(() => {
  Harp.initializeMapView(mapCanvas.value)
})

</script>

<template>
  <h1>Disaster Recovery Map</h1>
  <canvas ref="mapCanvas" />
</template>

<style scoped>
</style>
