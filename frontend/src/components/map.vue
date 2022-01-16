<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { db } from "@/services/firebase";
import { PointsApi } from "@/api/points";

declare const harp: any;

const canvasRef = ref();
let features: any[] = [];
let clickedPoint: any = [];

onMounted(() => {
  const canvas = canvasRef.value;
  const mapView = new harp.MapView({
    canvas,
    theme: {
      extends:
          'https://unpkg.com/@here/harp-map-theme/resources/berlin_tilezen_effects_streets.json',
      styles: {
        geojson: [
          {
            when: ['==', ['geometry-type'], 'Point'],
            technique: 'circles',
            renderOrder: 10000,
            color: '#ff6458',
            size: 20,
          }
        ]
      }
    },
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
  mapView.canvas.addEventListener('click', (e: any) => {
      const intersectResult = mapView.intersectMapObjects(e.offsetX, e.offsetY);
      if (intersectResult.length) {
        // @ts-ignore
        clickedPoint = features.features[intersectResult[0].dataSourceOrder]
      }
  });

  new PointsApi("-MtW3zaUorRXshWPTJN3").getPoints().then(f => {
      // @ts-ignore
      features = f
      const dataProvider = new harp.GeoJsonDataProvider('features', features);
      mapView.addDataSource(new harp.OmvDataSource({
        name: 'static',
        styleSetName: 'geojson',
        dataProvider: dataProvider,
        addGroundPlane: false,
      })).then(() => { mapView.update()});
  });
})



</script>

<template>
  <canvas ref="canvasRef" />
</template>

<style scoped>
</style>
