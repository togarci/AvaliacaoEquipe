<template>
    <div id="container-form">
        <div class="content">
            <carousel @handleSubmit="salvaAutoAvaliacao">
                <carousel-item>
                    <template>
                        <card>
                            <p>Teste</p>
                        </card>
                        <!-- <card v-for="(pergunta, index) in perguntas.entrega" :key="index">
                            <p>{{ `${index + 1} -  ${pergunta}` }}</p>
                            <div class="row respostas">
                                <el-radio v-for="(resposta, i) in respostas" v-model="dataEntrega[index]" :key="i" :label="resposta">{{ resposta }}</el-radio>
                            </div>
                        </card> -->
                    </template>
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
            dataResults: []
        }
    },
    methods: {
        validate() {
            
        },
        salvaAutoAvaliacao() {
        }
    },
    mounted() {
        this.getSkillAnswers();
    }
}
</script>

<style scoped>
    #container-form {
        display: flex;
        flex-direction: column;
        width: 100%;
        padding: 30px;
        align-items: center;
    }
    .content {
        width: 70%;
    }
    .respostas {
        margin-top: 15px;
    }
</style>
