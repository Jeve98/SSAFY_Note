<template>
  <h1>App.vue</h1>
  <MyComponent/>
  <Parent/>
</template>

<script setup>
  import MyComponent from './components/MyComponent.vue';
  import Parent from '@/components/Parent.vue';
</script>

<style scoped>
  h1{
    color: red;
  }
</style>
