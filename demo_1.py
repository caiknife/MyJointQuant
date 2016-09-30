#!/usr/bin/env python
# coding:utf8

"""
一个简单但是完整的策略
"""

from JoinQuant import *


def initialize(context):
    g.security = "000001.XSHE"


def handle_data(context, data):
    if g.security not in context.portfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)
