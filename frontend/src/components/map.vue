<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { db } from "@/firebase";

declare const harp: any;

const canvasRef = ref();

onMounted(() => {
  const canvas = canvasRef.value;
  const mapView = new harp.MapView({
    canvas,
    theme: "https://unpkg.com/@here/harp-map-theme@latest/resources/berlin_tilezen_night_reduced.json",
    projection: harp.sphereProjection
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

  db.ref('test').get().then(d => {
    let { lat, lon } = d.val();
    mapView.lookAt({
      target: new harp.GeoCoordinates(lat, lon),
      zoomLevel: 4,
      tilt: 40,
    });
  })
})

</script>

<template>
  <canvas ref="canvasRef" />
</template>

<style scoped>
</style>
