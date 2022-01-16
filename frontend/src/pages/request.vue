<script setup lang="ts">
import {onMounted, ref} from "vue";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Dropdown from 'primevue/dropdown';

import Title from "@/components/title.vue";
import {axios} from "@/services/axios";
import {DisasterAPI} from "@/api/disaster";

const numbers = ref<String[]>([])
const disasters = ref<String[]>([])
const number = ref("")
const sent = ref(false);
const selectedDisaster = ref(null);

// Load disasters for autocomplete
onMounted(async () => {
  let disasterApi = new DisasterAPI(null, null)

  // Parse data for better viewing
  let axiosData = (await disasterApi.getDisasters()).data;
  disasters.value = axiosData;
  console.log(axiosData)
})

const keyDownEvent = (event: KeyboardEvent) => {
  if (event.key === "Enter") {
    event.preventDefault();
    numbers.value.push(number.value);
    number.value = "";
  }
};

async function submitNumbers(disasterId: string) {
  if(!selectedDisaster.value || !selectedDisaster.value.id) { return; }

  sent.value = true;
  await axios.post(`/message/send/list?disaster_id=${selectedDisaster.value.id}`, numbers.value)
}

function uploadCSV(event: any) {
  const file = event.target.files[0];

  const reader = new FileReader();
  reader.onload = () => {
    let text = reader.result as string;
    const stuff = text.split(',')
    numbers.value = numbers.value.concat(stuff)
  };

  reader.readAsText(file);
};

</script>

<template>
  <header>
    <Title />
  </header>
  <div class="center">
    <div class="title">Send a safety message</div>
    <div class="subtitle">recipients will receive a text asking if they're okay, and if they need location-based emergency services</div>


    <div v-if="!sent" class="list-container">
      <div class="list-item" v-for="number in numbers">
        {{number}}
      </div>
      <Dropdown v-model="selectedDisaster" :options="disasters" optionLabel="message" placeholder="Select a Disaster" />
      <InputText :disabled="selectedDisaster === null" type="number" placeholder="Enter a phone number" v-model="number" @keydown="keyDownEvent" />
      <br/> or
      <input :disabled="selectedDisaster === null" type='file' @change='uploadCSV($event)' id='fileInput'>
    </div>
    <div v-else class="list-container">
      Message sent!
      &nbsp;
      <Button @click="sent = false" label="Send another"></Button>
    </div>
    <Button v-if="numbers.length > 0" class="submit-button" @click="submitNumbers('-MtW3zaUorRXshWPTJN3')" label="Send Safety Message" />
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
