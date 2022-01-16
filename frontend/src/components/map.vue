<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue';
import { db } from "@/services/firebase";
import { PointsApi } from "@/api/points";

declare const harp: any;

const canvasRef = ref();
let features: any[] = [];
let clickedPoint: any = [];

const pointData = ref({
  selected: false,
  coordinates: null,
  properties: {
    phoneNumber: null,
    isOk: true,
    message: null,
    timestamp: null
  }
})

onMounted(() => {
  const canvas = canvasRef.value;
  const mapView = new harp.MapView({
    canvas,
    theme: {
      extends:
          'https://unpkg.com/@here/harp-map-theme/resources/berlin_tilezen_day_reduced.json',
      styles: {
        geojson: [
          {
            when: ['==', ['geometry-type'], 'Point'],
            technique: 'circles',
            renderOrder: 10000,
            color: '#ff6458',
            size: 10,
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
      const staticPoint: any = intersectResult.find((x: { dataSourceName: string; }) => x.dataSourceName === 'static');

      if (staticPoint != null) {
        console.log(staticPoint)
        // @ts-ignore
        clickedPoint = features.features[staticPoint.dataSourceOrder]
        pointData.value.selected = true;
        pointData.value.coordinates = clickedPoint.geometry.coordinates;
        pointData.value.properties = clickedPoint.properties;
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

  <div class="overlay" v-if="pointData.selected">
    <div class="title">Disaster Check-in</div>

    <div class="li" v-if="pointData.properties.phoneNumber">
      Phone Number: {{pointData.properties.phoneNumber}}
    </div>

    <div class="li">
      Status: 
      <span v-if="pointData.properties.isOk">
        Ok
      </span>
      <span v-else>Not Ok</span>
    </div>

    <div class="li" v-if="pointData.properties.timestamp">
      Time: {{pointData.properties.timestamp}}
    </div>

    <div class="li" v-if="pointData.properties.message">
      Message: {{pointData.properties.message}}
    </div>

    <div class="li" v-if="pointData.coordinates">
      Location: 
      Lat: {{pointData.coordinates[0]}}
      Lon: {{pointData.coordinates[1]}}
    </div>
  </div>
</template>

<style scoped>
.overlay {
  position: absolute;
  left: 0;
  bottom: 0;
  padding: 1.25rem;
  border-top-right-radius: 0.25rem;
  font-weight: 700;
  background-color: lightblue;
}

.title {
  font-size: 1.25rem;
  text-decoration: underline;
  text-align: center;
  margin-bottom: 0.75rem;
}

.li {
  padding: 0.2rem;
}
</style>
