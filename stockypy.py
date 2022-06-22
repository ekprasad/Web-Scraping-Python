
import requests
from bs4 import BeautifulSoup as bs
import random
import csv
#from urllib.parse import urlencode

#url=f"https://www.screener.in/company/{stock_name}/consolidated/"#proxies={"http":current_proxy,"https":current_proxy})
#opening csv file
file = open("now.csv","a")
#writer=csv.writer(file)
#name,Market Cap,Current Price,High / Low,Stock P/E,Book Value,Dividend Yield,ROCE,ROE,Face Value,Date
keys=[]
#keys= ["S.No", "Name","Date","Market Cap","Current Price","High / Low","Stock P/E", "Dividend Yield","ROCE"]
writer = csv.DictWriter(file, fieldnames=keys)
a=random.randint(1,4)
stock_list1=["RELIANCE","NMDC","BPCL", "AVANTIFEED"]
for stock_name in range(a):
 stock_list=random.choices(list(stock_list1), k=random.randint(1,4))
for stock_name in stock_list:
   
    rl_link=(requests.get(f"https://www.screener.in/company/{stock_name}/consolidated/"))#proxies={"http":current_proxy,"https":current_proxy})

    soup1 = bs(rl_link.content,"html.parser")
    #fetching company_name, date with closing price
    name = soup1.find("div", class_="flex-row flex-wrap flex-align-center flex-grow").h1.text
    print(name)
    
    price=soup1.find("div",class_="flex flex-align-center").span.text.strip("\b ")
    time=soup1.find("div",class_="ink-600 font-size-11 font-weight-500").text.split()
    #print(price.encode("ascii","ignore"))
    str=price.replace("\u20b9","Rs.")
    print(str,end=" ")
    print("[",' '.join(time),"]")
    #writing company_name, date with closing price in csv file
    #writer.writerow([name])
    #writer.writerow([time])

    #fetching stock deatils
    rl_data=soup1.find("div",class_="company-ratios").find_all('li')
    stock_dict={}
    stock_dict["name"]=stock_name
    for data in rl_data:
        label = data.find("span", class_="name").text.strip()
        val=data.find("span",class_="number").text.strip()
        stock_dict[label]=val
   # stock_dict_df = pd.DataFrame(stock_dict)
    print(stock_dict) 
    keys=stock_dict.keys()
    value=stock_dict.values()
    
     
    #writinging stock deatils to csv file
    keys=[stock_dict.keys]
    print(keys)
    writer.writeheader()
    #writer.row(value)

        
    #print(keys)
    #writer = csv.DictWriter(file, fieldnames=keys)


    #writer.writerow({"S.No":"1"})
   # writer.writerow(stock_dict)
   
    