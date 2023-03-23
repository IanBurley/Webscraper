import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Open file for writing
with open('output.txt', 'w') as f:

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f.write(f'At time : {current_time} IST\n')
        
        response = requests.get('https://finance.yahoo.com/crypto/')
        text = response.text
        html_data = BeautifulSoup(text, 'html.parser')
        headings = html_data.find_all('tr')[0]
        headings_list = []
        for x in headings:
            headings_list.append(x.text)
        headings_list = headings_list[:10]
        
        data = []
        
        for x in range(1, 6):
            if len(html_data.find_all('tr')) <= x:
                break
            row = html_data.find_all('tr')[x]
            column_value = row.find_all('td')
            dict = {}
            
            for i in range(10):
                if i >= len(column_value):
                    continue
                dict[headings_list[i]] = column_value[i].text
            data.append(dict)
            
        for coin in data:
            f.write(str(coin)+'\n')
            f.write('\n')
        
        time.sleep(60)