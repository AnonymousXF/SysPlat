# -*- coding: utf-8 -*-
import pandas as pd
from collections import OrderedDict


class AnalysisNessus:
    """
    Analysis Nessus Scan Result ( csv file )
    """
    def __init__(self, csv_file, vul_level):
        """
        initial
        :param csv_file: str, Nessus扫描结果csv文件路径
        :param vul_level: str, 分析 >= vul_level 的漏洞结果，Critical/High/Medium/Low/None
        """
        self.data_frame = pd.read_csv(csv_file)

        levels = ['Critical', 'High', 'Medium', 'Low', 'None']
        self.vul_level = levels[:levels.index(vul_level)+1]

    def analysis(self):
        """
        筛选出符合要求的漏洞信息
        :return:
        """
        # 只取 Plugin ID、Risk、Name 三列信息
        df = self.data_frame.loc[:, ['Plugin ID', 'Risk', 'Name']].copy()

        # 筛选出vul_level中相应漏洞等级的条目，并去除重复Plugin ID的条目
        result = OrderedDict()
        for level in self.vul_level:
            result[level] = df.loc[(df['Risk'].str.contains(level)), :].drop_duplicates(['Plugin ID'])

        return result

    @staticmethod
    def get_values_of_column(data_frame, column_name):
        """
        获取某一列的所有值
        :param data_frame: DataFrame, DataFrame对象
        :param column_name: str, 列标题
        :return: list
        """
        return data_frame[column_name].get_values().tolist()
