<template>
  <canvas ref="map" />
</template>

<script lang="ts">
import json from './wireless-hotspots.json'

export default {
    name: "Map",
    props: {
      value: Object,
      dark: Boolean,
      startingTilt: {
        type: Number,
        default: 45
      },
      startingZoom: {
        type: Number,
        default: 16
      },
      startingLatitude: {
        type: Number,
        default: 1.278676
      },
      startingLongitude: {
        type: Number,
        default: 103.850216
      },
      geojsonData: {
        type: Object,
        default: json
      }
    },
    watch: {
      dark(newVal, oldVal) {
        console.log('HERE', newVal, oldVal)
        if (newVal !== oldVal) {
          this.updateTheme()
        }
      },
      value(newVal, oldVal) {
        if (!newVal && newVal !== oldVal) {
          this.resetZoom()
        }
      }
    },
    data: () => ({
      map: undefined,
      geodata: json,
      apiToken: "61cG0CqLLHlSzg5-OFXCt22CbT3jR6GU4f4kl-JS-1A",
      pointStyle: [{
        when: ["==", ["geometry-type"], "Point"],
        technique: "circles",
        renderOrder: 10000,
        color: "#FF0000",
        size: 15,
      }],
    }),
    computed: {
      themeURL: ({ dark }) => `https://unpkg.com/@here/harp-map-theme@latest/resources/berlin_tilezen_${dark ? 'night': 'day'}_reduced.json`
    },
    async mounted() {
      this.map = new harp.MapView({
        canvas: this.$refs.map,
        theme: this.themeURL
      });
      const controls = new harp.MapControls(this.map);
      const mapData = new harp.VectorTileDataSource({
        authenticationCode: this.apiToken,
      });
      await this.map.addDataSource(mapData);
      await this.addGeojson(this.geojsonData, 'my-data');

      this.map.canvas.addEventListener("click", this.clickListener);
    },
    methods: {
      updateTheme() {
        console.log('Updating Theme')
        this.map.theme = this.themeURL
        this.map.update()
      },
      lookAt(latitude, longitude, tilt=this.startingTilt, zoom=this.startingZoom) {
        this.map.lookAt({target: new harp.GeoCoordinates(latitude, longitude), tilt: tilt, zoomLevel: zoom});
      },
      resetZoom() {
        this.animateTransition(this.startingLatitude, this.startingLongitude, 2000, 400)
      },
      async addGeojson(geojsonData, name) {
        // Adding geojson data
        const dataProvider = new harp.GeoJsonDataProvider(name, geojsonData);
        const geoJsonDataSource = new harp.VectorTileDataSource({dataProvider, name});
        await this.map.addDataSource(geoJsonDataSource);
        geoJsonDataSource.setStyleSet(this.pointStyle);

        // Updating map
        this.lookAt(this.startingLatitude, this.startingLongitude)
        this.map.update();
      },
      clickListener(e) {
        const intersectionResults = this.map.intersectMapObjects(e.pageX, e.pageY);
        if (intersectionResults.length) {
          const coords = this.map.getGeoCoordinatesAt(e.pageX, e.pageY)
          this.$emit('input', coords)
          this.animateTransition(coords.latitude, coords.longitude)
        }
      },

      // Modified from https://www.harp.gl/docs/master/examples/codebrowser.html?src=src%2Fcamera-animations_quaternion-slerp.ts
      animateTransition(latitude, longitude, height=300, altitude=0) {
        const startPosition = this.map.camera.position.clone();
        const startQuaternion = this.map.camera.quaternion.clone();
        const targetPosition = harp.MapViewUtils.getCameraPositionFromTargetCoordinates(
          new harp.GeoCoordinates(latitude, longitude, altitude),
          height,
          45,
          45,
          this.map.projection
        );

        const targetQuaternion = harp.MapViewUtils.getCameraRotationAtTarget(
          this.map.projection,
          new harp.GeoCoordinates(latitude, longitude),
          45,
          45,
        );

        const startTime = Date.now();
        const curve = new THREE.CatmullRomCurve3([startPosition, targetPosition]);

        const updateListener = () => {
          const time = Date.now();
          let t = (time - startTime) / 1000;

          if (t >= 1) {
            t = 1;
            this.map.endAnimation();
            this.map.removeEventListener(harp.MapViewEventNames.Render, updateListener);
          }
          this.map.camera.position.copy(curve.getPoint(t));
          const rotation = startQuaternion.clone().slerp(targetQuaternion, t);
          this.map.camera.quaternion.copy(rotation);
          this.map.camera.updateMatrixWorld(true);
        };

        this.map.addEventListener(harp.MapViewEventNames.Render, updateListener);
        this.map.beginAnimation();
      }
    }
  }

</script>

