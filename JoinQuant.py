#!/usr/bin/env python
# coding:utf8

"""
https://www.joinquant.com/api
"""


def set_benchmark(security):
    """
    默认我们选定了沪深300指数的每日价格作为判断您策略好坏和一系列风险值计算的基准.
    您也可以使用set_benchmark指定其他股票/指数/ETF的价格作为基准。注意：这个函数只能在initialize中调用。
    :param security:
    :return:
    """
    pass


def set_order_cost(cost, type):
    """
    指定每笔交易要收取的手续费, 系统会根据用户指定的费率计算每笔交易的手续费
    :param cost:
    :param type:
    :return:
    """
    pass


def set_commission(object):
    pass


def set_slippage(object):
    """
    设定滑点，回测/模拟时有效.
    :param object:
    :return:
    """
    pass


def set_option(name, value):
    """
    设置 真实价格、成交量比例、期货保证金比例 选项,
    其中name=’use_real_price’时必须在initialize中调用，其它name没有这样的限制。
    :param name:
    :param value:
    :return:
    """


def set_universe(security_list):
    pass


def get_price(security, start_date=None, end_date=None, frequency='daily', fields=None,
              skip_paused=False, fq='pre', count=None):
    """
    获取一支或者多只股票的行情数据, 按天或者按分钟，这里请在使用时注意防止未来函数
    :param security:
    :param start_date:
    :param end_date:
    :param frequency:
    :param fields:
    :param skip_paused:
    :param fq:
    :param count:
    :return:
    """
    pass


def history(count, unit='1d', field='avg', security_list=None, df=True, skip_paused=False,
            fq='pre'):
    """
    回测环境/模拟专用API
    查看历史的行情数据。
    :param count:
    :param unit:
    :param field:
    :param security_list:
    :param df:
    :param skip_paused:
    :param fq:
    :return:
    """
    pass


def attribute_history(security, count, unit='1d',
                      fields=['open', 'close', 'high', 'low', 'volume', 'money'],
                      skip_paused=True, df=True, fq='pre'):
    """
    回测环境/模拟专用API
    查看某一支股票的历史数据, 可以选这只股票的多个属性, 默认跳过停牌日期.
    当取天数据时, 不包括当天的, 即使是在收盘后
    :param security:
    :param count:
    :param unit:
    :param fields:
    :param skip_paused:
    :param df:
    :param fq:
    :return:
    """
    pass


def get_current_data():
    """
    回测环境/模拟专用API
    获取当前单位时间（当天/当前分钟）的涨跌停价, 是否停牌，当天的开盘价等。
    回测时, 通过 API 获取到的是前一个单位时间(天/分钟)的数据, 而有些数据, 我们在这个单位时间是知道的,
    比如涨跌停价, 是否停牌, 当天的开盘价. 我们添加了这个API用来获取这些数据.
    :return:
    """
    pass


def get_extras(info, security_list, start_date='2015-01-01', end_date='2015-12-31', df=True,
               count=None):
    """
    得到多只标的在一段时间的如下额外的数据:
    is_st: 是否是ST，是则返回 True，否则返回 False
    acc_net_value: 基金累计净值
    unit_net_value: 基金单位净值
    futures_sett_price: 期货结算价
    futures_positions: 期货持仓量
    :param info:
    :param security_list:
    :param start_date:
    :param end_date:
    :param df:
    :param count:
    :return:
    """
    pass


def get_fundamentals(query_object, date=None, statDate=None):
    """
    查询财务数据，详细的数据字段描述请点击财务数据文档查看
    :param query_object:
    :param date:
    :param statDate:
    :return:
    """
    pass


def get_index_stocks(index_symbol, date=None):
    """
    获取一个指数给定日期在平台可交易的成分股列表，请点击指数列表查看指数信息
    :param index_symbol:
    :param date:
    :return:
    """
    pass


def get_industry_stocks(industry_code, date=None):
    """
    获取在给定日期一个行业的所有股票，行业分类列表见数据页面-行业概念数据。
    :param industry_code:
    :param date:
    :return:
    """
    pass


def get_concept_stocks(concept_code, date=None):
    """
    获取在给定日期一个概念板块的所有股票，概念板块分类列表见数据页面-行业概念数据。
    :param concept_code:
    :param date:
    :return:
    """
    pass


def get_all_securities(types=[], date=None):
    """
    获取平台支持的所有股票、基金、指数、期货信息
    :param types:
    :param date:
    :return:
    """
    pass


def get_security_info(code):
    """
    获取股票/基金/指数的信息.
    :param code:
    :return:
    """
    pass


def order(security, amount, style=None, side='long', pindex=0):
    """
    security: 标的代码
    amount: 交易数量, 正数表示买入, 负数表示卖出
    style: 参见order styles, None代表MarketOrder
    side: ‘long’/’short’，开空单还是多单。默认为多单，股票、基金暂不支持开空单。
    pindex: 在使用set_subportfolios创建了多个仓位时，指定subportfolio 的序号,
    从 0 开始, 比如 0 指定第一个 subportfolio, 1 指定第二个 subportfolio，默认为0。
    :param security:
    :param amount:
    :param style:
    :param side:
    :param pindex:
    :return:
    """
    pass


def order_target(security, amount, style=None, side='long', pindex=0):
    """
    买卖标的, 使最终标的的数量达到指定的amount
    security: 标的代码
    amount: 期望的最终数量
    style: 参见order styles, None代表MarketOrder
    side: ‘long’/’short’，平空单还是多单。默认为多单，股票、基金暂不支持开空单。
    pindex: 在使用set_subportfolios创建了多个仓位时，指定subportfolio 的序号,
    从 0 开始, 比如 0为 指定第一个 subportfolio, 1 为指定第二个 subportfolio，默认为0。
    :param security:
    :param amount:
    :param style:
    :param side:
    :param pindex:
    :return:
    """
    pass


def order_value(security, value, style=None, side='long', pindex=0):
    pass


def order_target_value(security, value, style=None, side='long', pindex=0):
    pass


def cancel_order(order):
    pass


def get_open_orders():
    pass


def get_orders():
    pass


def get_trades():
    pass


# 按月运行
def run_monthly(func, monthday, time='open', reference_security=""):
    pass


# 按周运行
def run_weekly(func, weekday, time='open', reference_security=""):
    pass


# 每天内何时运行
def run_daily(func, time='open', reference_security=""):
    pass


def record(**kwargs):
    pass


def send_message(message, channel='weixin'):
    pass


def write_file(path, content, append=False):
    pass


def read_file(path):
    pass
