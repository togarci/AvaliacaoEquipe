import axios from 'axios';

export class LoginService {
    constructor() {}
    
    login(data) {
        let url = `http://localhost:8082/api/login`
        axios.post(url, data).then(resp => {
            console.log(resp);
        })
    }
}