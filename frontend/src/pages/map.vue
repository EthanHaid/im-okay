<script setup lang="ts">
import { ref } from 'vue';
import Map from "@/components/map.vue";
import Title from "@/components/title.vue";

import Button from "primevue/button";
import Checkbox from 'primevue/checkbox';
import Sidebar from "primevue/sidebar";

const visibleRight = ref(false);
</script>

  <template>
    <header>
      <Title />
    </header>
    <Map />

    <Sidebar v-model:visible="visibleRight" position="right">
      <p>Filter by</p>
    </Sidebar>

    <Button
      id="filter-button"
      icon="pi pi-filter-fill"
      class="p-button-rounded btn"
      @click="visibleRight= true" />

</template>

<style scoped>
header {
    background-color: rgba(53, 84, 151, 0.75);
    position: fixed;
    top: 0;
    width: 100vw;
}
header > h1 {
  color: var(--cream);
  margin: 0.2em 0.5em;
}

#filter-button {
  position: fixed;
  bottom: 2em;
  right: 2em;
}
</style>
