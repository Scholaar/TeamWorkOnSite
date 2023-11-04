<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="container">
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <!-- <RouterLink to="/task">Task</RouterLink> -->
    </nav>
    <RouterView />
  </div>
</template>

<style lang="less">
body{
  padding: 0;
  margin: 0;
}
.container{
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  nav{
    display: flex;
    flex-direction: row;
    background-color: rgb(209, 209, 209);
    a{
      padding: 1rem;
      text-decoration: none;
      color: #000;
      &:hover{
        color: #666;
      }
    }
  }
}
</style>