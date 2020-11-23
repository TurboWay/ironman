#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

from flask import Flask, render_template
from data import SourceData

app = Flask(__name__)

source = SourceData()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/line')
def line():
    data = source.line
    return render_template('line.html', title=data.title, data=data.values, legend=data.legend, xAxis=data.xAxis,
                           unit=data.unit)


@app.route('/bar')
def bar():
    data = source.bar
    return render_template('bar.html', title=data.title, data=data.values, legend=data.legend, xAxis=data.xAxis,
                           unit=data.unit)


@app.route('/bar_y')
def bar_y():
    data = source.bar_y
    return render_template('bar_y.html', title=data.title, data=data.values, legend=data.legend, xAxis=data.xAxis,
                           unit=data.unit)


@app.route('/bar_polar')
def bar_polar():
    data = source.bar_polar
    return render_template('bar_polar.html', title=data.title, data=data.values, legend=data.legend, xAxis=data.xAxis,
                           unit=data.unit)


@app.route('/bar_waterfall')
def bar_waterfall():
    data = source.bar_waterfall
    return render_template('bar_waterfall.html', title=data.title, data=data.values, legend=data.legend,
                           xAxis=data.xAxis, special=data.special,
                           unit=data.unit)


@app.route('/pie')
def pie():
    data = source.pie
    return render_template('pie.html', title=data.title, data=data.values, legend=data.legend, unit=data.unit)


@app.route('/pie_doughnut')
def pie_doughnut():
    data = source.pie_doughnut
    return render_template('pie_doughnut.html', title=data.title, data=data.values, legend=data.legend, unit=data.unit)


@app.route('/china')
def china():
    data = source.china
    return render_template('china.html', title=data.title, data=data.values, unit=data.unit)


@app.route('/wordcloud')
def wordcloud():
    data = source.wordcloud
    return render_template('wordcloud.html', title=data.title, data=data.values, unit=data.unit)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
