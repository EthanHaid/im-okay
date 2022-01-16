<script setup lang="ts">
import Button from "primevue/button";
</script>

<template>
  <div className="p-grid">
  	<div className="p-col-3 sidebar">
      <h1>Disaster+Recovery</h1>
      <a>Home</a>
      <a>Inbox</a>
      <a>History</a>
      <button>Create Message</button>
    </div>
  	<div className="p-col-9">
      <h2>Login</h2>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
    height: 100vh;
    background-color: red;
  }
</style>
