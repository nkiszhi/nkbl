
#! /usr/bin/env python
# -*- coding: UTF-8 -*-
'''
负责对这段时间内各种info数量的统计,完成README中的第二个工作
'''

import pandas as pd
import general_dataframe

def get_info():
    info_list = general_dataframe.write_to_dataframe()
    info_list.drop_duplicates()
    info_series = info_list['info'].value_counts()
    df=pd.DataFrame({'info':info_series.index, 'number':info_series.values})
    df.to_csv("infonumber.csv",header=1,index=0)


get_info()
