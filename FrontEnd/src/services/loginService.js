import axios from 'axios';

export class LoginService {
    constructor() {}
    
    login(data) {
        let url = `users/login`;
        return axios.post(url, data).then(resp => resp.data)
    }
}