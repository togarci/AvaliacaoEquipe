<template>
    <div id="body">
        <header class="header">
            <div class="iconContainer">
                <font-awesome-icon color="#FFF" backgroundColor="#016795" size="2x" :icon="['fas', 'user-circle']" />
            </div>
        </header>
        <div class="center">
            <aside>
                <Menu/>
            </aside>
            <section>
                <router-view />
            </section>
        </div>
    </div>
</template>

<script>
import Menu from '@/components/Menu.vue'

export default {
    components: {
        Menu
    }
}
</script>

<style>
</style>
