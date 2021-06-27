import axios from "axios";

export class skillAnswerService {
    constructor() {}
    
    getAllSkillAnswer() {
        let url = 'api/getAllskills';
        return axios.get(url).then(response => response.data)
    }
}