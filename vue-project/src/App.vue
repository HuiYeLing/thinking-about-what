<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import MyButton from './components/MyButton.vue'
import Radios from './components/Radios.vue';
</script>

<template>
  



  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <router-view></router-view>
      <router-link to="/HelloWorld">HelloWorld</router-link>
      <router-link to="/MyButton">Button</router-link>
      <router-link to="/Radios">Radio</router-link>
       <!-- 添加的路由链接 -->
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>

  <div>
    <my-button />
  </div>

    <el-radio-group v-model="selectedOption">
      <el-radio-button label="Option 1"></el-radio-button>
      <el-radio-button label="Option 2"></el-radio-button>
      <el-radio-button label="Option 3"></el-radio-button>
    </el-radio-group>

    
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>