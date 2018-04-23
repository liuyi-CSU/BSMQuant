#-*-coding:utf-8-*-
#！/usr/bin/env python

#
# CRR期权定价
# Devin
#

import math
import numpy as np
from BMSQuant import BSM_call_value

# S0: 指数水品
# K: 执行价格
# r: 无风险短期利率
# sigma: 波动率
# otype: 看涨、看跌类型call/put
# M: 时间间隔

def CRR_option_value(S0, K, T, r, sigma, otype, M = 4):
    '''CRR欧式看涨期权计算'''
    # 时间参数
    dt = T / M
    df = math.exp(-r * dt) # 单位时间内的折扣
    # 二项式参数
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    q = (math.exp(r * dt) - d) / (u - d)
    # 初始化指数水平矩阵
    mu = np.arange(M + 1)
    mu = np.resize(mu, (M + 1, M + 1))
    md = np.transpose(mu)
    mu = u ** (mu - md)
    md = d ** md
    S = S0 * mu * md

    if otype == 'call':
        V = np.maximum(S - K, 0)
    else:
        V = np.maximum(K - S, 0)
    z = 0
    for t in range(M - 1, -1, -1):
        V[0:M - z, t] = (q * V[0:M - z, t + 1] + (1 - q) * V[1:M - z + 1, t + 1]) * df
        z += 1
    return V[0, 0]