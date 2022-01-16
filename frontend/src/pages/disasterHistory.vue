<script setup lang="ts">
import Title from "@/components/title.vue";
import Button from "primevue/button";
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import {onMounted, ref} from 'vue';
import {DisasterAPI} from "@/api/disaster";

let data = ref([]
)

onMounted(async () => {
  let disasterApi = new DisasterAPI(null, null)

  // Parse data for better viewing
  let axiosData = (await disasterApi.getDisasters()).data;

  for(let i = 0; i < axiosData.length; i++) {
    // Format timestamp
    let timestamp = axiosData[i].timestamp
    if(timestamp) {
      axiosData[i].timestamp = timestamp.substring(0, timestamp.indexOf(' '));
    }

  }
  data.value = axiosData;
})



</script>

<template>
  <div class="p-grid">
    <div class="p-col content">
      <h1>History</h1>
      <DataTable :value="data" showGridlines responsiveLayout="scroll">
        <Column field="timestamp" header="Timestamp"></Column>
        <Column field="message" header="Message"></Column>
        <Column field="location_string" header="Location"></Column>
      </DataTable>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  height: 100vh;
  width: 20vw;
  background-color: var(--secondary);
  padding: 1em;
  color: var(--cream);
  font-family: var(--text-font)
}

.content {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
}
</style>
