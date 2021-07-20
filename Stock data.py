input_directory = "C:/Users/Ege/Dropbox/Python work/self work/efekalp"


import pandas as pd 
from datetime import datetime
from pandas_datareader import data

def get_data(symbol, start_date, end_date):
	dat =  data.DataReader (symbol, "yahoo", start_date, end_date) 
# A ratio created in order to calculate splits and dividents 
	dat ['Ratio'] = dat['Adj Close'] / dat['Close']

	dat ['Open'] = dat['Open'] / dat ['Ratio']
	dat ['High'] = dat['High'] / dat ['Ratio']
	dat ['Low'] = dat['Low'] / dat ['Ratio']
	dat ['Close'] = dat['Close'] / dat ['Ratio']


	return dat

Stocks = ["^GSPC","SWKS","WYNN","QRVO","QCOM","MU","AVGO","NVDA","TXN","IPGP","KLAC","AMAT","MCHP","INTC","WDC","LRCX","AOS","AMD","GLW","APH","APTV","XLNX","A","AVY","AAPL","MGM","TEL","WAT","PKI","ADI","MTD","BWA","ALB","TPR","APD","BA","NKE","LEG","DHR","ILMN","CMI","EMR"]

start = datetime (2016,11,16)

end = datetime.today()

fh = open("one file to rule them all.csv",'w+')

for ticker in Stocks:

	DF = get_data(ticker,start,end)

	for i, date in enumerate(DF.index):
		fh.write('{} {} {:f} {:f} {:f} {:f} {:f} {} \n'.format(ticker,date.strftime('%d.%m.%Y'),DF['Open'][i],DF['High'][i],DF['Low'][i],DF['Close'][i],DF['Volume'][i],DF['Adj Close'][i]))
	
fh.close()

