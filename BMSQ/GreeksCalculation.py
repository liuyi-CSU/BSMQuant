#-*-coding:utf-8-*-
#！/usr/bin/env python

#
# Function for Greeks
# Devin
#
import math
import numpy as np
from BMSQuant import d1f, N, dN


def BSM_delta(St, K, t, T, r, sigma):
    '''欧式看涨期权DELTA'''
    #---看涨价值关于指数St的偏导
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
    # 返回值：欧式看涨delta
    d1 = d1f(St, K, t, T, r, sigma)
    delta = N(d1)
    return delta

def BSM_gamma(St, K, t, T, r, sigma):
    '''欧式看涨期权gamma'''
    d1 = d1f(St, K, t, T, r, sigma)
    gamma = dN(d1) / (St * sigma * math.sqrt(T - t))
    return gamma

def BSM_theta(St, K, t, T, r, sigma):
    '''欧式看涨期权theta'''
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    theta = -(St * dN(d1) * sigma / (2 * math.sqrt(T - t))+ r * K * math.exp(-r * (T - t)) * N(d2))
    return theta

def BSM_rho(St, K, t, T, r, sigma):
    '''欧式看涨期权rho'''
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    rho = K * (T - t) * math.exp(-r * (T - t)) * N(d2)
    return rho

def BSM_vega(St, K, t, T, r, sigma):
    '''欧式看涨期权vega'''
    d1 = d1f(St, K, t, T, r, sigma)
    vega = St * dN(d1) * math.sqrt(T - t)
    return vega

