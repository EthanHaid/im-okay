<script setup lang="ts">
import Title from "@/components/title.vue";
import Button from "primevue/button";
</script>

<template>
  <div class="sidebar">
    <Title />
    <a><i class="pi pi-home"></i>&nbsp&nbspHome</a><br/><br/>
    <a><i class="pi pi-envelope"></i>&nbsp&nbspInbox</a><br/><br/>
    <a><i class="pi pi-clock"></i>&nbsp&nbspHistory</a><br/><br/><br/><br/>
    <Button class="btn" label="Create Message"/>
  </div>
</template>

<style scoped>
.sidebar {
  height: 100vh;
  width: 20vw;
  background-color: var(--secondary);
  padding: 1em;
  color: var(--cream);
  font-family: var(--text-font);
  float: left;
}
</style>
