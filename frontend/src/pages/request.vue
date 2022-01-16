<script setup lang="ts">
import { ref } from "vue";
import Button from "primevue/button";
import InputText from "primevue/inputtext";

import Title from "@/components/title.vue";

const numbers = ref<String[]>([])
const number = ref("")
const sent = ref(false);

const keyDownEvent = (event: KeyboardEvent) => {
  if (event.key === "Enter") {
    event.preventDefault();
    numbers.value.push(number.value);
    number.value = "";
  }
};

function submitNumbers() {
  sent.value = true;
  // TODO submit to backend
  numbers.value = [];
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
      <InputText type="number" placeholder="Enter a phone number" v-model="number" @keydown="keyDownEvent" />
      <br/> or
      <input type='file' @change='uploadCSV($event)' id='fileInput'>
    </div>
    <div v-else class="list-container">
      Message sent!
      &nbsp;
      <Button @click="sent = false" label="Send another"></Button>
    </div>
    <Button v-if="numbers.length > 0" class="submit-button" @click="submitNumbers" label="Send Safety Message" />
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
