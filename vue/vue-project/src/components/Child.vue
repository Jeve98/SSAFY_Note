<template>
    <div>
        child
        msg : {{ msg }}
        <GrandChild :msg="msg"/>
    </div>
</template>

<script setup>
    import GrandChild from './GrandChild.vue';
    defineProps({msg: String})
</script>
    
<style scoped>

</style>