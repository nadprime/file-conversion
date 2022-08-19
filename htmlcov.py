from bs4 import BeautifulSoup
import urllib2
import csv

url = 'http://www.-Input_Url_Here-.com'
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
table = soup.select_one("table.data2_s")

headers = [th.text.encode("utf-8") for th in table.select("tr th")]

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])