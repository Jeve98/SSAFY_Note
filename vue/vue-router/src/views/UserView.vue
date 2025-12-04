<template>
    <div>
        User View - {{ userId }}
        <RouterLink :to="{name: 'profile'}">PROFILE</RouterLink>
        <RouterLink :to="{name: 'post'}">POST</RouterLink>
    </div>
    <hr>
    <RouterView/>
    <button @click="home">HOME</button>
</template>

<script setup>
import { useRoute, useRouter, RouterLink, RouterView } from 'vue-router';
import { ref } from 'vue';

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const home = function(){
    router.push({name: 'home'})
}
</script>

<style scoped>

</style>