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
let location = {}
let disasterApi = new DisasterAPI(String(route.query.d), String(route.query.p))
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
      disasterApi.updateLocation(pos)
  });
}

</script>

<template>
    <header>
      <Title />
    </header>
  <div>
    <p>We detected that you are near:</p>
    <div class="for-adam">
      <h3>3345 Pearl St. New York, NY, United States</h3>
    </div>
    <p>where there is currently a <strong>hurricane warning</strong></p>
    <h3>Are you okay?</h3>
    <span class="p-float-label">
    	<InputText id="comment" type="text" v-model="value" placeholder="Optional message"/>
    	<label for="comment"></label>
    </span><br/>
    <Button class="btn" label="SEND HELP" @click="help()"/><br/>
    <Button class="ok-btn" label="I'm Okay" @click="thanks()"/>
  </div>
</template>

<style scoped>
.for-adam {
  background-image: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
}

div {
  text-align: center;
  padding: 2em;
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
