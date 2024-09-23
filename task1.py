import requests
import json

from matplotlib import pyplot as plt

#"https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240916&end=20240920&valcode=usd&json"

reply = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240916&end=20240920&valcode=usd&json")

#print(reply)
#print(reply.headers)
#print(reply.text)

reply_json = json.loads(reply.text)

#print(reply_json)

output_dict = {}
for item in reply_json:
    #print(item)
    #print("!!!")
    output_dict[item['exchangedate']] = item['rate']
    #print(output_dict)

fig, ax = plt.subplots()
ax.plot(output_dict.keys(), output_dict.values())
#values_list = sorted(output_dict.items())
plt.show()