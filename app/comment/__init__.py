# -*- coding:utf8 -*-
'''
index page.
'''
__all__ = []
__version__ = '0.0.1'
__author__ = 'GalaIO'

from flask import Blueprint
import app

# 通过实例化一个 Blueprint 类对象可以创建蓝本。
comment = Blueprint('comment', __name__)
# 动态加载到app的路由链表中
app.fetchRoute(comment, '/comment')

from . import views