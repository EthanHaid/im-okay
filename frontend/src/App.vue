<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
</script>

<template>
  <router-view />
</template>

<style>
@import 'primevue/resources/primevue.min.css';
@import 'primeflex/primeflex.css'; /* TODO: minify build artifact: https://purgecss.com/ */
@import 'primeicons/primeicons.css';

@import 'primevue/resources/themes/bootstrap4-light-blue/theme.css';
@import './colors.css';

@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@600&family=Raleway:wght@300;400;600&display=swap");

html {
  font-family: 'Nunito', sans-serif; /* TODO: Pick a better one (+ remove url import) */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html, body, #app, #view {
  height: 100%;
  margin: 0;
}

h1 {
  font-family: var(--display-font);
  color: var(--text-color);
}

.highlight {
  color: var(--primary);
}

#view {
  background-color: var(--light);
  display: flex;
  flex-direction: column;
}

#content {
  height: 100%;
  overflow-y: auto;
}

.page-container {
  max-width: 80rem;
  margin: auto;
  padding: 1rem;
}

/* width */
::-webkit-scrollbar {
  width: 15px
}

/* Track */
::-webkit-scrollbar-track {
  background: #202020;
  border-left: 1px solid #2c2c2c;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #3e3e3e;
  border: solid 3px #252525;
  border-radius: 7px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>
