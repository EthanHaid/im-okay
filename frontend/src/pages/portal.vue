<script setup lang="ts">
import Sidebar from "@/components/sidebar.vue";
import Button from "primevue/button";
</script>

<template>
  <div>
  	<Sidebar />
  	<div>
      <div class="p-grid">
        <div class="p-row">
          <div id="map" class="p-col">
            <h2>Map View</h2>
          </div>
          <div class="p-col">
            <div id="summary" class="p-row">
              <h2>Data Summary</h2>
            </div>
            <div id="responses" class="p-row">
              <h2>Responses</h2>
            </div>
          </div>
        </div>
        <div id="other" class="p-row">
          <h2>Other Messages Sent</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  #map {
    height: 70vh;
    width: 50vw;
    background-color: var(--cream);
    float: left;
  }
</style>
