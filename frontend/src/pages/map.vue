<script setup lang="ts">
import { ref } from 'vue';
import Map from "@/components/map.vue"

import Button from "primevue/button";
import Checkbox from 'primevue/checkbox';
import Sidebar from "primevue/sidebar";

const visibleRight = ref(false);
</script>

  <template>
    <Button @click="$router.push('/')" label="Home" />
    <Map />

    <Sidebar v-model:visible="visibleRight" position="right">
      <p>Filter by</p>
    </Sidebar>

    <Button
      id="filter-button"
      icon="pi pi-filter-fill"
      className="p-button-rounded"
      @click="visibleRight= true" />

</template>

<style scoped>
#filter-button {
  position: fixed;
  bottom: 2em;
  right: 2em;
  background-color: var(--primary);
  border: none;
}
</style>
