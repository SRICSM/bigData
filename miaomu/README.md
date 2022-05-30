# 基于Django和Layui搭建的前后端分离苗木数据可视化

#### 介绍
本项目后端使用Django加Mysql, 前端使用Layui和Echarts(ECharts，一个使用 JavaScript 实现的开源可视化库，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等底层依赖矢量图形库 ZRender，提供直观，交互丰富，可高度个性化定制的数据可视化图表, 由百度开源)实现前后端分离渲染,


#### 环境配置
1.  Python3.8
2.  Mysql5.7
3.  Django3.1.2
4 . Scrapy
#### 安装教程

1.  git clone https://gitee.com/blackjackfsociety/miaomu.git
2.  将miaomu/src/目录下的miaomu.zip解压缩

#### 使用说明

1.  解压缩完成后, cd miaomu, 执行命令: scrapy crawl huamu进行数据爬取
2.  数据爬取完成后, 启动Django项目, cd website, 执行命令: python manage.py runserver

