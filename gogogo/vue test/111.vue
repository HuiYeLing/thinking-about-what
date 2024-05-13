<template>
  <div id="app">
    <button @click="increment">{{ count }}</button>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const count = ref(0);
    const increment = () => {
      count.value++;
    };
    return {
      count,
      increment
    };
  }
};
</script>

<style scoped>
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
button {
  font-size: 2em;
  padding: 10px 20px;
}
</style>