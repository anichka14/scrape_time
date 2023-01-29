"""[B]26.01. Скласти програму, яка читає точний час з сайту
https://www.timeanddate.com/worldclock/ukraine/kyiv
та перевіряє, чи відповідає час на локальному комп’ютері точному часу. Показати
отриманий результат.
Час можна дізнатись у тегу <span>:
<span id=ct class=h1>12:00:00</span>"""


from datetime import datetime
from lxml import html
import requests


url = 'https://www.timeanddate.com/worldclock/ukraine/kyiv'

response = requests.get(url)  # відкриваємо ресурс за даними URL
tree = html.fromstring(response.content)
time = tree.xpath('//*[@id="ct"]/text()')[0]
print(time, " - час на сайті")

local_time = datetime.now().time()
local_time = local_time.strftime("%H:%M:%S")
print(local_time, " - локальний час")
print(time == local_time)

