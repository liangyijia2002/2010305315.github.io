"""
Date: 2021.3.22
Author: Justin

要点说明：
Map 地图
分多个系列填充颜色
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
   

c = (
    Map()
    .add("华人", 
         [('Russia',998000),('Thailand',7153240),('France',230515),('Indonesia',7566200),
          ('Malaysia',7070500),('America',3376031),('Singapore',2684936),('Canada',1612173),
          ('Peru',1300000),('Vietnam',1263570),('the Philippines',1146250),('Burma',1101314),
          ('Australia',700000),('Japan',519561),('Cambodia',343855),('Britain',296623),
          ('India',189470),('Laos',185765),('Brazil',151649),('New Zealand',147570),
          ('Netherlands',144928),('Korea',137790),('Panama',100000),], 
         maptype="world",
         is_map_symbol_show=False, # 不描点
    )
   
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="海外华人分布图"),
        visualmap_opts=opts.VisualMapOpts(max_=8000000,min_=80000),
    )
)

c.render('./output/海外华人分布图.html')