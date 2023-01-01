from pyecharts.charts import Map
from pyecharts.options import *
import json
f_map = open('E:\programme\Python\practice\EpidemicMap.txt','r',encoding='UTF-8')
data=f_map.read()
f_map.close()
data=json.loads(data)
# province_data is a list
province_data=data['areaTree'][0]['children']
# fomat the list province_data and save to a new list
province_list=list()
for province in province_data:
    name=province['name']+'省'
    confirm=province['total']['confirm']
    province_list.append((name,confirm))
map=Map()
map.add('confirm',province_list)
print(province_list)
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True
    )
)

map.render('map.html')
