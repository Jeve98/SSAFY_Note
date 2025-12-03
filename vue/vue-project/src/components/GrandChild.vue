<template>
    <div>
        grand child
        message : {{ msg }}
    </div>
</template>

<script setup>
    defineProps({
        msg: String,
    })
</script>

<style scoped>

</style>