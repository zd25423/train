# coding:utf-8
import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'
response = requests.get(url,verify=False)
print(response.text)
# stations = re.findall(u'')