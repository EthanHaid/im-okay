<script setup lang="ts">
import { ref, onMounted } from "vue";
import Button from "primevue/button";
import InputText from "primevue/inputtext"

let numbers: String[] = []
const number = ref("")

function addNumber() {
  numbers.push(number.value);
  number.value = "";
}

const keyDownEvent = (event: KeyboardEvent) => {
  if (event.key === "Enter") {
    event.preventDefault();
    addNumber();
  }
};

</script>

<template>
  <Button @click="$router.push('/')" label="Home" />
  <div>Create new message</div>
  <div>
    <div>Contact list:</div>
    <div v-for="number in numbers">
      {{number}}
    </div>
    <InputText ref="input" type="number" v-model="number" @keydown="keyDownEvent" />
  </div>
</template>

<style scoped>
</style>
