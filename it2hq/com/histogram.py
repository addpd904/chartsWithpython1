from pyecharts.charts import Bar,Timeline
from pyecharts.options import *

# 一、read the data file and format data
f = open('E:\programme\Python\practice\GDP.csv','r',encoding='GB2312')
data=f.read()
data=data.split('\n')
data.pop(0)
data.pop(-1)
f.close()
# format the data to {1960: [['美国', 543], ['英国', 7323]...],1961: [['美国', 543], ['英国', 7323]...]...}
gdp_dict=dict()
for ele in data:
    # remove the space and apostrophe
    ele=ele.strip(' \'')
    # split the str with comma,return a list
    country_list=ele.split(',')
    year=int(country_list[0])
    country=country_list[1]
    gdp=float(country_list[2])
    try:
        gdp_dict[year].append([country,gdp])
    except:
        gdp_dict[year]=[]
        gdp_dict[year].append([country,gdp])
# sort the year
year_list=gdp_dict.keys()
sorted(year_list)

# 二、create histogram
# create timeline
timeline=Timeline()
def mysort(ele):
    return ele[1]
for year in year_list:
    bar = Bar()
    # x:country y:gdp
    x_data = []
    y_data = []
    # get the all country in a particular year
    gdp_list=gdp_dict[year]
    gdp_list.sort(key=mysort,reverse=True)
    gdp_list=gdp_list[0:10:1]
    # in this year,get all gdp and country whose gdp is in the top ten
    for ele1 in gdp_list:
        x_data.append(ele1[0])
        y_data.append(ele1[1]/100000000)
    # reversal x_data and y_data
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    print(x_data)
    print(y_data)
    bar.add_yaxis('gdp',y_data,label_opts=LabelOpts(position='right'))
     # reversal x and y
    bar.reversal_axis()
    bar.set_global_opts(
        # histogram's title
        title_opts=TitleOpts(title=str(year), pos_left='center', pos_bottom='90%')
    )
    timeline.add(bar,str(year))
timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
timeline.render('GDPhistogram.html')


