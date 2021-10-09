#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：process-mining -> main.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
import pandas


def input_csv(file_path, sep=";"):
    event_log = pandas.read_csv(file_path, sep=sep)
    num_events = len(event_log)
    num_cases = len(event_log.case_id.unique())
    print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))


if __name__ == "__main__":
    input_csv("../../data/input/running-example.csv")