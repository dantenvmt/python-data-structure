import bs4
import mysql.connector
import pandas as pd
import os
from sqlalchemy import create_engine
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import requests
import random
import time
a = input()

useragent = ["Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko)",
"Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
]
l = (random.choice(useragent)) 
headers = {"User-Agent": l, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
r = requests.get("https://www.crunchbase.com/organization/"+ a, headers= headers )

#connect database
mydb = mysql.connector.connect(
	host = "localhost",	
	user = "root",
	password = "1234",
	auth_plugin='mysql_native_password'
	)
mycursor = mydb.cursor(buffered=True,dictionary=True)
mycursor.execute("CREATE DATABASE IF NOT EXISTS test")
#html parser
pagesoup = soup(r.text,"html.parser")
containers = pagesoup.findAll("section-layout", {"cbtableofcontentsitem": "Overview"})
container = containers[0]
txt = container.findAll("span", {"class":"wrappable-label-with-info ng-star-inserted"})
left = txt[0]

num = container.findAll("span",{"class":"bigValueItemLabelOrData flex-none layout-column layout-align-center-start"})

right = txt[1]
#text strip
asg = left.text.strip()
ash = right.text.strip()
asf = num[0].text.strip()
ase = num[1].text.strip()
#data
leftcont = container.findAll("span",{"class":"cb-text-color-medium field-label flex-100 flex-gt-sm-25 ng-star-inserted"})
lastleft = container.findAll("span",{"class":"cb-text-color-medium field-label flex-100 flex-gt-sm-25 last-field ng-star-inserted"})
rightcont = container.findAll("span",{"class": "field-value flex-100 flex-gt-sm-75 ng-star-inserted"})
lastright = container.findAll("span",{"class":"field-value flex-100 flex-gt-sm-75 last-field ng-star-inserted"})
#excel
c = [asg.replace(" ", "_").replace("(","").replace(")",""),ash.replace(" ", "_").replace("(","").replace(")","")]
d = [asf,ase]

#print(c)
#print(d)
g = []
h = []
for i in range(len(leftcont)):
    asd = leftcont[i].text.strip().replace(" ", "_").replace("-", "_")
    asc = rightcont[i].text.strip()
    g.append(asd)
    h.append(asc)	
e =[]
f =[]

for i in range(len(lastleft)):
	asb =lastleft[i].text.strip().replace(" ", "_").replace("-", "_")
	asa = lastright[i].text.strip()
	e.append(asb)
	f.append(asa)
print(e)
print(f)
i = ["company_name"]
k = [a]
ge = i + g + e + c
print(ge)
hf = k + h + f + d
data = [hf]
df = pd.DataFrame(data, columns = ge)
print(df)
#insert database
engine = create_engine('mysql+pymysql://root:1234@localhost/test')
with engine.connect() as conn, conn.begin():
	mycursor.execute("use test")
	mycursor.execute("create table if not exists data (company_name varchar(255), Description varchar(255),	Industries varchar(255),	Headquarters_Location varchar(255),	Headquarters_Regions varchar(255),	Founded_Date varchar(255),	Founders varchar(255),	Operating_Status varchar(255), Funding_Status varchar(255),	Last_Funding_Type varchar(255), Number_of_Employees varchar(255),	Also_Known_As varchar(255),	Legal_Name varchar(255),	Child_Hubs varchar(255),	Hub_Tags varchar(255),	IPO_Status varchar(255),	Stock_Symbol varchar(255),	Company_Type varchar(255),	Number_of_Exits int,	Website varchar(255),	Facebook varchar(255),	LinkedIn varchar(255),	Twitter varchar(255),	Phone_Number varchar(255),	Number_of_Acquisitions int,	Number_of_Investments int, CB_Rank_Company varchar(255),	Sub_Organization_of varchar(255),	Total_Funding_Amount varchar(255), Contact_Email varchar(255)	)")
	mycursor.execute("SELECT * FROM data WHERE company_name = %s", (a,))
	data1=mycursor.fetchone()
	if data1 is None:
		df.to_sql('data', conn, if_exists='append', index=False)
	else:
		print(a + " existed in database" )

#financial
r2 = requests.get("https://www.crunchbase.com/organization/"+ a +"/funding_financials", headers= headers )

#html parser
pagesoup2 = soup(r2.text,"html.parser")
fundingcontainer = pagesoup2.findAll("list-card", {"class": "ng-star-inserted"})
fundingtext = fundingcontainer[0]
date = fundingtext.findAll("span", {"class": "component--field-formatter field-type-date ng-star-inserted"})
transactionname = fundingtext.findAll("a", {"class": "link-primary component--field-formatter field-type-identifier ng-star-inserted"})

numberofinvestor = fundingtext.findAll(["a","span"], {"class": ["link-primary component--field-formatter field-type-integer ng-star-inserted", 'component--field-formatter field-type-integer ng-star-inserted']})
moneyraised = fundingtext.findAll("span", {"class": "component--field-formatter field-type-money ng-star-inserted"})
leadinvestor = fundingtext.findAll("span", {"class": "component--field-formatter field-type-identifier-multi"})

m = []
#dataframe
for i in range(len(date)):
	datestrip = date[i].text.strip().replace(",","")
	transtrip = transactionname[i].text.strip()
	numstrip = numberofinvestor[i].text.strip()
	moneystrip = moneyraised[i].text.strip()
	leadstrip = leadinvestor[i].text.strip()
	m.append([a,datestrip,transtrip,numstrip,moneystrip,leadstrip])
data1 = m
df1 = pd.DataFrame(data1, columns = ["company_name", "date","trans_name","numberofinvestor","moneyraised","leadinvestor"])
print(df1)
#database
engine2 = create_engine('mysql+pymysql://root:1234@localhost/test')
with engine2.connect() as conn, conn.begin():
	mycursor.execute("use test")
	mycursor.execute("create table if not exists fundinground (company_name varchar(255), date varchar(255), trans_name varchar(255), numberofinvestor varchar(255), moneyraised varchar(255), leadinvestor varchar(255))")	
	mycursor.execute("SELECT * FROM fundinground WHERE company_name = %s", (a,))
	data2=mycursor.fetchone()
	if data2 is None:
		df1.to_sql('fundinground', conn, if_exists='append', index=False)
	else:
		print(a + " existed in database" )
#link
r3 = requests.get("https://www.crunchbase.com/organization/"+ a +"/people", headers= headers )

#html parser
pagesoup3 = soup(r3.text,"html.parser")		
boss = pagesoup3.findAll("image-list-card", {"class": "ng-star-inserted"})
teammember = boss[1]
bossname = teammember.findAll("a", {"class": "link-primary"})
boardadviser = boss[2]
boardname = boardadviser.findAll("a", {"class": "link-primary"})
n=[]
p=[]
for i in range(len(bossname)):
	bossstrip = bossname[i].text.strip()
	bossstrip1 = bossname[i].text.strip().replace(" ","-").lower()
	n.append(bossstrip)
	p.append(bossstrip1)
print(n)
o = []
for i in range(len(boardname)):
	boardstrip = boardname[i].text.strip()
	boardstrip1 = boardname[i].text.strip().replace(" ","-").lower()
	o.append(boardstrip)
	p.append(boardstrip1)
print(o)
#Number of Current Team Members Number of Board Members / Advisors
no = n + o
print(p)
#link
 
for i in range(len(p)):
	time.sleep(20)
	q = []
	s = []
	l = (random.choice(useragent)) 
	headers = {"User-Agent": l, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
	r4 = requests.get("https://www.crunchbase.com/person/" + p[i], headers= headers )
	print(headers)
	pagesoup4 = soup(r4.text,"html.parser")
	socialmedia = pagesoup4.findAll("div", {"class": "section-layout-content"})
	link = socialmedia[0].findAll("a", {"class": "link-primary component--field-formatter field-type-link layout-row layout-align-start-end ng-star-inserted"})
	for j in range(len(link)):
		hyperlink = link[j]
		social = hyperlink.get('href')
		name = hyperlink.get('title')
		namereplace = name.replace("View On ","")
		s.append(social)
		q.append(namereplace)
	print(q)
	print(s)
