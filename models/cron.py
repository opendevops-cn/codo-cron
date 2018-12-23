#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018/8/22
Desc    : 定时任务models
"""
from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper
from datetime import datetime

Base = declarative_base()


def model_to_dict(model):
    model_dict = {}
    for key, column in class_mapper(model.__class__).c.items():
        model_dict[column.name] = getattr(model, key, None)
    return model_dict


class CronLog(Base):
    __tablename__ = 'cron_log'

    ### 定时任务日志表
    log_id = Column('log_id', Integer, primary_key=True, autoincrement=True)
    job_id = Column('job_id', String(30))
    status = Column('status', String(10))
    task_cmd = Column('task_cmd', String(120))
    task_log = Column('task_log', Text())
    exec_time = Column('exec_time', DateTime(), default=datetime.now)
