<script setup lang="ts">
import Map from '@/components/map.vue'

import Button from "primevue/button";
</script>

<template>
  <Button @click="$router.push('/')" label="Home" />
  <Map />
</template>

<style scoped>
</style>
