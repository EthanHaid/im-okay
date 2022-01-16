<script setup lang="ts">
import Button from "primevue/button";
</script>

<template>
  <div class="page-container">
    <div class="title">This isn't the page you're looking for.</div>
    <Button @click="$router.push('/')" label="Go Home" />
  </div>
</template>

<style scoped>
.title {
  margin: 1rem;
  font-size: 1.25rem;
}

Button {
  display: block;
  margin: 1rem 0 0 2rem;
}
</style>
