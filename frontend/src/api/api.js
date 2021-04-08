import axios from 'axios';

export class CoinApi{
    url = 'http://localhost:8000/';

    async coinList(){
        const response = await axios.get(this.url);

        return response.data;
    }
}