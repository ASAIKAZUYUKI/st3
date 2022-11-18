import streamlit as st
from PIL import Image

#数値計算やデータフレーム操作に関するライブラリをインポートする
import numpy as np
import pandas as pd

#図やグラフを図示するためのライブラリをインポート
#import matplotlib.pyplot as plt
#matplotlib inline

#import sklearn #機械学習のライブラリ
#from sklearn.decomposition import PCA #主成分分析

# githubの練習
# branch
#branchの練習


import csv
import os
import math

markdown = """
## グラフと表の表示
"""

st.write(markdown)

df = pd.read_csv('1.csv',header=None)

st.line_chart(df)
st.dataframe(df)

st.title('Check Box')
col = st.columns(3)
c0 = col[0].checkbox(label='0')
c1 = col[1].checkbox(label='1')
c2 = col[2].checkbox(label='2')
 
stocks = []
if c0:
    stocks.append(0)
if c1:
    stocks.append(1)
if c2:
    stocks.append(2)
st.line_chart(df[stocks])
st.dataframe(df[stocks])

