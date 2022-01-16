<script setup lang="ts">
import {onMounted, ref} from 'vue';
import Map from "@/components/map.vue"
import Title from "@/components/title.vue"

import Button from "primevue/button";
import Checkbox from 'primevue/checkbox';
import InputText from 'primevue/inputtext';
import Sidebar from "primevue/sidebar";
import { useRoute, onBeforeRouteUpdate } from "vue-router";
import { DisasterAPI } from "@/api/disaster";


const route = useRoute()
var value = ""
let location = ref({})
let disasterApi = new DisasterAPI(route.query.disaster_id, route.query.disaster_response_id)
setLocation()

async function help() {
  await disasterApi.respondHelp()
  alert("Help is on the way!")
}

async function thanks() {
  await disasterApi.respondOk()
  alert("Thanks for confirming!")
}

function setLocation() {
  navigator.geolocation.getCurrentPosition(pos => {
      location.value = `Latitude: ${pos.coords.latitude}, Longitude: ${pos.coords.latitude}`
      disasterApi.updateLocation(pos)
  });
}

</script>

<template>
    <header>
      <Title />
    </header>
  <div class="container">
    <p>We detected that you are near:</p>
    <div class="light">
      <h3>{{ location }}</h3>
    </div>
    <p>where there is currently a <strong>hurricane warning</strong></p>
    <h3>Are you okay?</h3>
    <InputText id="comment" type="text" placeholder="Optional message"/><br/><br/>
    <Button class="btn" label="SEND HELP" @click="help()"/><br/>
    <Button class="ok-btn" label="I'm Okay" @click="thanks()"/>
  </div>
</template>

<style scoped>
.light {
  background-color: var(--primary-light);
  padding: 2em;
}

.container {
  padding: 2em;
  text-align: center;
  max-width: 50em;
  width: 100%;
  background-color: var(--cream);
  position: fixed;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -45%);
  transform: translate(-50%, -45%);
}

header {
    background-color: var(--secondary);
    width: 100vw;
}
header > h1 {
  color: var(--cream);
  margin: 0em 0.5em;
}
.ok-btn {
  color: var(--primary);
  background-color: rgba(0,0,0,0);
  border: none;
}
.ok-btn:hover {
  color: var(primary);
  background-color: rgba(0,0,0,0) !important
}



</style>
