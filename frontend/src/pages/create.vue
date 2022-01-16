<script setup lang="ts">
import Title from "@/components/title.vue";
import Button from "primevue/button";
import InputText from 'primevue/inputtext';
import {onMounted, ref} from 'vue';
import {DisasterAPI} from "@/api/disaster";
import {axios} from "@/services/axios";
import {AxiosError} from "axios";
import {useRouter} from "vue-router";

const router = useRouter();
let message = ref('')
let location_string = ref('')

async function submitDisaster() {
  let disaster = {
    message: message.value,
    location_string: location_string.value,
  }

  try {
    await axios.post(`/disasters/`, disaster);
    await router.push('/request');
  } catch(e: any) {
    alert("Oops... Request failed." + e.message);
  }
}


</script>

<template>
  <header>
    <Title />
  </header>
  <div class="center">
    <div class="title">Create a new disaster</div>
    <div class="subtitle">You can then send messages to potential victims in the request page</div>


    <div class="list-container">
      <InputText id="message" type="text" v-model="message" placeholder="Message"/>
      <InputText id="location" type="text" v-model="location_string" placeholder="Location"/>
      <Button class="btn" label="Submit Disaster" @click="submitDisaster" :disabled="message === '' || location_string === ''"/>

    </div>


  </div>
</template>

  <style scoped>
    header {
      background-color: var(--secondary);
      width: 100vw;
    }
    header > h1 {
      color: var(--cream);
      margin: 0em 0.5em;
    }

    .center {
      text-align: center;
      padding: 2em;
    }
    .title {
      font-size: 1.5rem;
      margin: 1rem;
    }

    .subtitle {
      font-size: 1.2rem;
    }

    .list-container {
      margin: 2rem auto;
      text-align: center;
      max-width: 40rem;
    }

    .list-item {
      padding: 0.5rem;
    }

    /* Chrome, Safari, Edge, Opera */
    input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }

    /* Firefox */
    input[type=number] {
      -moz-appearance: textfield;
    }
</style>

