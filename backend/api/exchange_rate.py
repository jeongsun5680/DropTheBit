import requests, json
from datetime import datetime

def Exchange_Rate():
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"
    today = datetime.today().strftime("%Y%m%d")
    querystring = {"authkey":"cVVI6zqyibj82ElHwc2TBv37RyNNF29C","searchdate":today, "data":"AP01", "cur_unit":"USD"}
    res = requests.request("GET", url, params=querystring)
    dict_res = res.json()
    return dict_res[0]['deal_bas_r']
