import axios from 'axios';

export class CoinApi{
    url = 'http://localhost:8000/';

    coinList(){
        return axios.get(this.url).then((response)=> response.data);
    }
}