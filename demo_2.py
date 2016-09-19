#!/usr/bin/env python
# coding:utf8

"""
一个实用的策略，根据历史价格做出判断
- 如果上一个时间点价格高出五天平均价1%，则全仓买入
- 如果上一个时间点嘉哥低于五天平均价，则空仓卖出
"""


def initialize(context):
    # 000001 平安银行
    g.security = "000001.XSHE"
    # 设定沪深300作为基准
    set_benchmark("000300.XSHG")


def handle_data(context, data):
    security = g.security
    close_data = attribute_history(security, 5, '1d', ['close'])
    # 取得过去五天的平均价格
    MA5 = close_data['close'].mean()
    # 取得上一时间点价格
    current_price = close_data['close'][-1]
    # 取得当前的现金
    cash = context.portfolio.cash

    if current_price > 1.01 * MA5:
        # 全仓买入
        order_value(security, cash)
        log.info("Buying %s" % (security))
    elif current_price < MA5 and context.portfolio.positions[security].sellable_amount > 0:
        # 如果上一时间点价格低于五天平均价，则空仓卖出
        order_target(security, 0)
        log.info("Selling %s" % (security))

    # 画出上一时间点价格
    record(stock_price=current_price)
