from pyecharts.charts import Line
from pyecharts.options import TitleOpts
line=Line()
line.add_xaxis(['china','am','japan'])
line.add_yaxis('gdp',[100,30,10])
# global configuration
line.set_global_opts(
    title_opts=TitleOpts(title="global GDP",pos_left='center')
)
line.render()
