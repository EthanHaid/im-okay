<script setup lang="ts">
import Button from "primevue/button";
</script>

<template>
  <h1>Home</h1>
  <Button @click="$router.push('map')" label="View Map" />
  <br />
  <Button @click="$router.push('send')" label="Send safety check" />
</template>

<style scoped>
</style>
