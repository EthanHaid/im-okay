<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
declare const harp: any;

const canvasRef = ref();

onMounted(() => {
  const canvas = canvasRef.value;
  const mapView = new harp.MapView({
    canvas,
    theme: "https://unpkg.com/@here/harp-map-theme@latest/resources/berlin_tilezen_night_reduced.json"
  });

  // TODO: base coords on backend data
  mapView.lookAt({
    target: new harp.GeoCoordinates(40.70398928, -74.01319808),
    zoomLevel: 17,
    tilt: 40,
  });

  const mapControls = new harp.MapControls(mapView);
  const ui = new harp.MapControlsUI(mapControls);
  canvas.parentElement.appendChild(ui.domElement);

  mapView.resize(window.innerWidth, window.innerHeight);
  window.onresize = () => mapView.resize(window.innerWidth, window.innerHeight);

  const vectorTileDataSource = new harp.VectorTileDataSource({
    authenticationCode: "61cG0CqLLHlSzg5-OFXCt22CbT3jR6GU4f4kl-JS-1A"
  });
  mapView.addDataSource(vectorTileDataSource);
})

</script>

<template>
  <canvas ref="canvasRef" />
</template>

<style scoped>
</style>
