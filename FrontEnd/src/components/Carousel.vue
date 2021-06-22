<template>
	<div class="container-carousel">
		<div class="step-carousel">
			<span  v-for="ls in lenStep" :key="ls" :class="ls === (step + 1) && 'activeStep'" ></span>
		</div>
		<div id="carousel">
			<slot></slot>
		</div>
		<div class="footer-carousel">
			<div class="btn-container-carousel">
				<button @click="back">Voltar</button>
				<button @click="next">{{ lblBtnContinuar }}</button>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'carousel',
	data() {
		return {
			lblBtnContinuar: 'Próximo',
			step: 0,
			lenStep: 0,
			widthCarouselItem: 0
		}
	},
	methods: {
		next() {
			if (this.step < (this.lenStep - 1)) {
				this.step += 1;
				let carousel = document.querySelector('#carousel');
				carousel.style.transform = `translateX(-${ this.widthCarouselItem * this.step }px)`;
				
			} else if (this.step === (this.lenStep - 1)) {
				this.$emit('handleSubmit')
			}
		},
		back() {
			if (this.step > 0) {
				this.step -= 1;
				let carousel = document.querySelector('#carousel');
				carousel.style.transform = `translateX(-${ this.widthCarouselItem * this.step }px)`;
			}
		}
	},
	watch: {
		step(newValue, oldValue) {
			if (newValue === (this.lenStep - 1)) {
				this.lblBtnContinuar = 'Finalizar';
			} else {
				this.lblBtnContinuar = 'Próximo';
			}

			this.$emit('handleChangeStep', newValue);
		}
	},
	mounted() {
		this.widthCarouselItem = document.querySelector('.carousel-item').clientWidth;
		this.lenStep = document.querySelectorAll('.carousel-item').length;
	}
}
</script>

<style scoped>
	.container-carousel {
		display: flex;
		flex-direction: column;
		overflow-x: hidden;
		align-items: center;
		width: 100%;
	}
	.step-carousel {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20px;
		width: 100px;
	}
	span {
		width: 15px;
		height: 15px;
		background-color: #016795;
		border-radius: 20px;
	}
	.activeStep {
		width: 25px;
		height: 25px;
	}
	#carousel {
		display: flex;
		flex-wrap: nowrap;
		max-width: 100%;
		transition: transform 0.5s ease-in-out;
	}
	.footer-carousel {
		display: flex;
		width: 100%;
		justify-content: flex-end;
	}
	.btn-container-carousel {
		display: flex;
		justify-content: space-between;
		margin-top: 20px;
		width: 200px;
	}
	button {
		height: 35px;
		width: 90px;
		font-weight: bolder;
		border: none;
		border-radius: 5px;
		cursor: pointer;
	}
	button:nth-child(2) {
		color: white;
		background-color: #016795;
	}
</style>