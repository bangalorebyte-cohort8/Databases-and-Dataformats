from requests import get
import json
import sqlite3

class Markit():
	def company_search(self, company_name):
		q={'input': company_name}
		s ="http://dev.markitondemand.com/Api/v2/Lookup/json/"
		res = get(s,q)
		r = res.json()
		print(r)
		formal_name = r[0]["Name"]
		ticker_symbol=(r[0]["Symbol"])
		exchange = r[0]["Exchange"]
		return formal_name, ticker_symbol, exchange

	def get_quote(self, ticker_symbol):
		q={'symbol': ticker_symbol}
		s = "http://dev.markitondemand.com/Api/v2/Quote/json/"
		res = get(s,q)
		r = res.json()
		print(r)
		lastprice = r['LastPrice'] #price is type of float, converting to number will remove the decimal values
		print(lastprice, type(lastprice))
		return lastprice



# for testing
if __name__ == '__main__':
	m = Markit()
	name = input('enter the company name ')
	name = name.upper()
	print(name)
	formal_name, ticker_symbol, exchange = m.company_search(name)
	print("formal name ", formal_name)
	print("ticker symbol ", ticker_symbol)
	print("exchnage ", exchange)
	last_price = m.get_quote(ticker_symbol)
	print("last stock price ", last_price)
