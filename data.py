#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

from random import randint


class Data:
    def __init__(self, title=None, values=None, xAxis=None, legend=None, unit=None, special=None):
        self.title = title  # 标题
        self.values = values  # 图表数据
        self.xAxis = xAxis  # 图例名称【一般折线，柱形图需要】
        self.legend = legend  # 横坐标数据【一般折线，柱形图需要】
        self.unit = unit  # 单位【可选】
        self.special = special  # 特殊图标保留参数


class SourceDataDemo:

    @property
    def line(self):
        data = Data()
        data.title = '折线图示例'
        data.values = [
            {'name': '指数1', 'values': [randint(1, 10) for _ in range(7)]},
            {'name': '指数2', 'values': [randint(1, 10) for _ in range(7)]},
        ]
        data.legend = [key['name'] for key in data.values]
        data.xAxis = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        data.unit = '单位：随机数'
        return data

    @property
    def bar(self):
        data = Data()
        data.title = '柱形图示例'
        data.values = [
            {'name': '股票A', 'values': [randint(15, 30) for _ in range(7)]},
            {'name': '股票B', 'values': [randint(15, 30) for _ in range(7)]},
            {'name': '股票C', 'values': [randint(15, 30) for _ in range(7)]},
        ]
        data.legend = [key['name'] for key in data.values]
        data.xAxis = ['一月', '二月', '三月', '四月', '五月', '六月']
        data.unit = '单位：元'
        return data

    @property
    def bar_y(self):
        data = Data()
        data.title = '柱形图示例-横柱'
        data.values = [
            {'name': '股票A', 'values': [(i + 1) * 10 for i in range(7)]},
            {'name': '股票B', 'values': [(i + 1) * 8 for i in range(7)]},
        ]
        data.legend = [key['name'] for key in data.values]
        data.xAxis = ['一月', '二月', '三月', '四月', '五月', '六月']
        data.unit = '单位：元'
        return data

    @property
    def bar_polar(self):
        data = Data()
        data.title = '柱形图示例-极坐标'
        data.values = [
            {'name': '股票A', 'values': [randint(15, 30) for _ in range(7)]},
            {'name': '股票B', 'values': [randint(15, 30) for _ in range(7)]},
            {'name': '股票C', 'values': [randint(15, 30) for _ in range(7)]},
        ]
        data.legend = [key['name'] for key in data.values]
        data.xAxis = ['一月', '二月', '三月', '四月', '五月', '六月']
        data.unit = '单位：元'
        return data

    @property
    def bar_waterfall(self):
        data = Data()
        data.title = '柱形图示例-瀑布'
        data.values = [
            {'name': '总费用', 'value': 5500},
            {'name': '房租', 'value': 2400},
            {'name': '水电费', 'value': 300},
            {'name': '交通费', 'value': 600},
            {'name': '伙食费', 'value': 2000},
            {'name': '日用品数', 'value': 200},
        ]
        data.legend = [key['value'] for key in data.values]
        data.xAxis = [key['name'] for key in data.values]
        data.special = [0 if i == 1 else data.legend[0] - sum(data.legend[1:i]) for i in range(1, len(data.legend) + 1)]
        data.unit = '生活费'
        return data

    @property
    def pie(self):
        data = Data()
        data.title = '饼图示例'
        data.values = [
            {'name': '直接访问', 'value': 335},
            {'name': '邮件营销', 'value': 310},
            {'name': '联盟广告', 'value': 234},
            {'name': '视频广告', 'value': 130},
            {'name': '搜索引擎', 'value': 1548}
        ]
        data.legend = [key['name'] for key in data.values]
        data.unit = '访问数'
        return data

    @property
    def pie_doughnut(self):
        data = Data()
        data.title = '饼图示例-环形'
        data.values = [
            {'name': '直接访问', 'value': 335},
            {'name': '邮件营销', 'value': 310},
            {'name': '联盟广告', 'value': 234},
            {'name': '视频广告', 'value': 130},
            {'name': '搜索引擎', 'value': 1548}
        ]
        data.legend = [key['name'] for key in data.values]
        data.unit = '访问数'
        return data

    @property
    def china(self):
        data = Data()
        data.title = '地图示例'
        data.values = [
            {'name': '四川', 'value': 239},
            {'name': '浙江', 'value': 231},
            {'name': '福建', 'value': 203},
            {'name': '江苏', 'value': 185},
            {'name': '湖南', 'value': 152},
            {'name': '山东', 'value': 131},
            {'name': '安徽', 'value': 100},
            {'name': '广东', 'value': 89},
            {'name': '河北', 'value': 87},
            {'name': '湖北', 'value': 84},
            {'name': '吉林', 'value': 75},
            {'name': '上海', 'value': 70},
            {'name': '江西', 'value': 64},
            {'name': '广西', 'value': 64},
            {'name': '贵州', 'value': 64},
            {'name': '北京', 'value': 63},
            {'name': '云南', 'value': 53},
            {'name': '重庆', 'value': 49},
            {'name': '河南', 'value': 48},
            {'name': '陕西', 'value': 38},
            {'name': '山西', 'value': 37},
            {'name': '辽宁', 'value': 33},
            {'name': '新疆', 'value': 25},
            {'name': '内蒙古', 'value': 23},
            {'name': '黑龙江', 'value': 20},
            {'name': '天津', 'value': 19},
            {'name': '甘肃', 'value': 13},
            {'name': '海南', 'value': 9},
            {'name': '青海', 'value': 7},
            {'name': '宁夏', 'value': 4},
            {'name': '西藏', 'value': 0},
        ]
        data.unit = '人口'
        return data

    @property
    def wordcloud(self):
        data = Data()
        data.title = '词云示例'
        data.values = [
            {"name": "图瓦卢", "value": 47},
            {"name": "罗马尼亚", "value": 52},
            {"name": "朝鲜", "value": 90},
            {"name": "古巴", "value": 84},
            {"name": "科威特", "value": 99},
            {"name": "卡塔尔", "value": 37},
            {"name": "美国", "value": 2},
            {"name": "伊拉克", "value": 32},
            {"name": "多米尼克国", "value": 3},
            {"name": "塞舌尔", "value": 20},
        ]
        data.unit = ''
        return data


class SourceData(SourceDataDemo):
    ...
