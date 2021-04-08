import pyupbit

print(pyupbit.Upbit)

tickers = pyupbit.get_tickers()
print(tickers)

# 코인 KRW 거래 가능 코인들
coin_upbit_lst = []
for i in tickers:
    if i[0:3] == "KRW":
        coin_upbit_lst.append(i[4:])

print(len(coin_upbit_lst))
