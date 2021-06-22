<template>
    <div id="container-form">
        <div class="content">
			<card>
				<div class="row a-center">
					<font-awesome-icon color="#016795" backgroundColor="#016795" size="2x" :icon="['fas', 'user-circle']" />
					<p class="pessoa-nome">{{ `Membro 1 / ${lblSoftSkill}` }}</p>
				</div>
			</card>
            <carousel @handleSubmit="salvaAutoAvaliacao" @handleChangeStep="handleStep">
                <carousel-item>
                    <card v-for="(pergunta, index) in perguntas.entrega" :key="index">
                        <p>{{ `${index + 1} -  ${pergunta}` }}</p>
						<b>Resposta: </b>
                        <div class="row respostas">
                            <el-radio v-for="(resposta, i) in respostas" v-model="dataEntrega[index]" :key="i" :label="resposta">{{ resposta }}</el-radio>
                        </div>
                    </card>
                </carousel-item>
                <carousel-item>
                    <card v-for="(pergunta, index) in perguntas.autonomia" :key="index">
                        <p>{{ `${index + 1} -  ${pergunta}` }}</p>
						<b>Resposta: </b>
                        <div class="row respostas">
                            <el-radio v-for="(resposta, i) in respostas" v-model="dataAutonomia[index]" :key="i" :label="resposta">{{ resposta }}</el-radio>
                        </div>
                    </card>
                </carousel-item>
                <carousel-item>
                    <card v-for="(pergunta, index) in perguntas.proatividade" :key="index">
                        <p>{{ `${index + 1} -  ${pergunta}` }}</p>
						<b>Resposta: </b>
                        <div class="row respostas">
                            <el-radio v-for="(resposta, i) in respostas" v-model="dataProatividade[index]" :key="i" :label="resposta">{{ resposta }}</el-radio>
                        </div>
                    </card>
                </carousel-item>
                <carousel-item>
                    <card v-for="(pergunta, index) in perguntas.colaboracao" :key="index">
                        <p>{{ `${index + 1} -  ${pergunta}` }}</p>
						<b>Resposta: </b>
                        <div class="row respostas">
                            <el-radio v-for="(resposta, i) in respostas" v-model="dataColaboracao[index]" :key="i" :label="resposta">{{ resposta }}</el-radio>
                        </div>
                    </card>
                </carousel-item>
            </carousel>
        </div>
    </div>
</template>

<script>
import Carousel from '@/components/Carousel'
import CarouselItem from '@/components/CarouselItem';
import Card from '@/components/Card';
import generalMixin from '@/mixins/generalMixin.js';

export default {
    mixins: [
        generalMixin
    ],
    components: {
        Carousel,
        CarouselItem,
        Card
    },
    data() {
        return {
			listSoftSkills: [
				'Entrega de Resultados',
				'Autonomia',
				'Proatividade',
				'Colaboração'
			],
			lblSoftSkill: 'Entrega de Resultados',
            dataEntrega: {
                0: null,
                1: null,
                2: null
            },
            dataAutonomia: {
                0: null,
                1: null,
                2: null
            },
            dataProatividade: {
                0: null,
                1: null,
                2: null
            },
            dataColaboracao: {
                0: null,
                1: null,
                2: null
            }
        }
    },
    methods: {
        validate() {
            for(let value in this.dataEntrega) {
                if (!this.dataEntrega[value]) {
                    return false;
                }
            }
            for(let value in this.dataAutonomia) {
                if (!this.dataAutonomia[value]) {
                    return false;
                }
            }
            for(let value in this.dataProatividade) {
                if (!this.dataProatividade[value]) {
                    return false;
                }
            }
            for(let value in this.dataColaboracao) {
                if (!this.dataColaboracao[value]) {
                    return false;
                }
            }

            return true;
        },
        salvaAutoAvaliacao() {
            let isValid = this.validate();
            if (isValid) {
                console.log('passou');
            } else {
                alert('Verique se todas as perguntas foram respondidas')
            }
        },
		handleStep(step) {
			this.lblSoftSkill = this.listSoftSkills[step];
		}
    }
}
</script>

<style scoped>
    #container-form {
        display: flex;
        flex-direction: column;
        height: auto;
        width: 100%;
        padding: 30px;
        align-items: center;
    }
    .content {
        width: 70%;
        overflow: hidden;
    }
    .respostas {
        margin-top: 15px;
    }
	b {
		margin: 5px 0px 5px 0px;
		color: #559835;
	}
	.pessoa-nome {
		margin-left: 10px;
	}
</style>
