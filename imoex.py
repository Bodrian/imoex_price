import requests

#данная функция получает последние катировки акций с московской бирже и записывает их в словарь. пример {GAZP:170}
def price():
	url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json?iss.meta=off&iss.only=marketdata&marketdata.columns=SECID,LAST"
	request = requests.get(url).json()
	price_dic = {}
	for el in request['marketdata']['data']:
		price_dic[str(el[0])] = el[1]
	return price_dic