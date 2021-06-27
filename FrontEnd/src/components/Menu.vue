<template>
	<el-menu default-active="home" class="el-menu-vertical-demo" :router="true" :collapse="isCollapse">
		<el-menu-item index="home">
			<i class="el-icon-s-home"></i>
			<span slot="title">Início</span>
		</el-menu-item>
		<!-- <el-menu-item index="validacao">
			<i class="el-icon-finished"></i>
			<span slot="title">Validação</span>
		</el-menu-item> -->
		<el-menu-item index="form">
			<i class="el-icon-document"></i>
			<span slot="title">Formulario</span>
		</el-menu-item>
		<el-menu-item index="login">
			<i class="el-icon-switch-button"></i>
			<span slot="title">Sair</span>
		</el-menu-item>
	</el-menu>
</template>

<script>

export default {
	name: 'menu',
	components: {
	},
	data() {
		return {
			isCollapse: true
		}
	},
	methods: {
		handleOpen(key, keyPath) {
			console.log(key, keyPath);
		},
		handleClose(key, keyPath) {
			console.log(key, keyPath);
		},
		openMenu() {
			this.isCollapse = false;
		},
	}
}
</script>

<style>
	.el-menu-vertical-demo:not(.el-menu--collapse) {
		width: 200px;
		min-height: 400px;
	}
</style>
