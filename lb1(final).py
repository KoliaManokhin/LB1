from requests import get
from json import loads
from matplotlib import pyplot
from datetime import timedelta, datetime

current_date = datetime.today()
previous_week_date = current_date - timedelta(7)

current_date = current_date.strftime('%Y%m%d')
previous_week_date = previous_week_date.strftime('%Y%m%d')

print(current_date, previous_week_date)

site = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={int(previous_week_date)}&end={int(current_date)}&valcode=usd&json"

print(site)
reply = get(site)

reply_json = loads(reply.text)

output_dict = {}
for item in reply_json:
    output_dict[item['exchangedate']] = item['rate']

fig, ax = pyplot.subplots()
ax.plot(output_dict.keys(), output_dict.values())
pyplot.show()

