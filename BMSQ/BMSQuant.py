#-*-coding:utf-8-*-
#！/usr/bin/env python
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'
from scipy.integrate import quad

#
# Helper Functions
#

def dN(x):
    '''x的概率密度函数'''
    return math.exp(-0.5 * x ** 2) / math.sqrt(2 * math.pi)

def N(d):
    '''正态分布函数'''
    return quad(lambda x: dN(x), -20, d, limit=50)[0]

def d1f(St, K, t, T, r, sigma):
    '''BMS模型的d1函数'''
    d1 = (math.log(St / K) + (r + 0.5 * sigma ** 2)
          * (T - t)) / (sigma * math.sqrt(T - t))
    return d1

#
# Valuation Funcions
#

def BSM_call_value(St, K, t, T, r, sigma):
    '''计算BSM欧洲看涨期权价值'''
    # St: float
    # t时刻的股票或质数水准
    # K: float
    # 执行价格
    # t: float
    # 估值日
    # T: float
    # 到期日/（到期日-t）
    # r: float
    # 常熟，无风险短期利率
    # sigma: float
    # 波动率
    # 返回值：t时刻的欧式看涨期权价值
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    call_value = St * N(d1) - math.exp(-r * (T - t)) * K * N(d2)
    return call_value

def BSM_put_value(St, K, t, T, r, sigma):
    '''欧式看跌期权价值'''
    put_value = BSM_put_value(St, K, t, T, r, sigma) - St + math.exp(-r * (T - t)) * K
    return put_value


