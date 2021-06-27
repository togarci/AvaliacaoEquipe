import { skillAnswerService } from "../services/skillAnswerService";

const serviceSkillAnswer = new skillAnswerService();

export default {
    data() {
        
    },
    methods: {
        getSkillAnswers() {
            serviceSkillAnswer.getAllSkillAnswer()
            .then(resp => console.log(resp))
            .catch(e => this.$toasted.show('Error to get skills and answers'));
        }
    }
}