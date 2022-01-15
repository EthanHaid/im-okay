<script setup lang="ts">
import Button from "primevue/button";
</script>

<template>
  <h1>Home</h1>
  <Button @click="$router.push('map')" label="View Map" />
</template>

<style scoped>
</style>
