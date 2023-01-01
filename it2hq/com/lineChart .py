import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts
# 一、read the data file and format data
usf = open('E:\programme\Python\practice\mg.txt','r',encoding='UTF-8')
us_data=usf.read()
us_data=us_data.replace('jsonp_1629344292311_69436(','')
us_data=us_data[:-2]
# json to dict
us_data=json.loads(us_data)
us_trend=us_data['data'][0]['trend']
us_x_data=us_trend['updateDate'][0:300:1]
us_y_data=us_trend['list'][0]['data'][0:300:1]
usf.close()


jaf = open('E:\programme\Python\practice\Japan.txt','r',encoding='UTF-8')
ja_data=jaf.read()
ja_data=ja_data.replace('jsonp_1629350871167_29498(','')
ja_data=ja_data[:-2]
# json to dict
ja_data=json.loads(ja_data)
ja_trend=ja_data['data'][0]['trend']
ja_x_data=ja_trend['updateDate'][0:300:1]
ja_y_data=ja_trend['list'][0]['data'][0:300:1]
print(ja_x_data)
print(ja_y_data)
jaf.close()

# 二、create linechart
line=Line()

line.add_xaxis(us_x_data)
line.add_yaxis('Confirmed in the US',us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('Confirmed in the Japan',ja_y_data)
line.set_global_opts(
#     title
    title_opts=TitleOpts(title='2020 data of padmic',pos_left='center',pos_bottom='1%')

)



line.render()