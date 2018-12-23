#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018/8/21
Desc    : 任务逻辑
"""

import subprocess
from models.cron import CronLog
from websdk.db_context import DBContext


def exec_shell(cmd):
    """执行shell命令函数"""
    sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = sub.communicate()
    ret = sub.returncode
    if ret == 0:
        return ret, stdout.decode('utf-8').split('\n')
    else:
        return ret, stdout.decode('utf-8').replace('\n', '')


def exec_cmd(cmd, job_id):
    """执行CMD命令,记录日志"""
    recode, stdout = exec_shell(cmd)
    print('cmd', recode, stdout)
    with DBContext('w') as session:
        session.add(
            CronLog(job_id=job_id, status='success' if recode == 0 else 'faild', task_cmd=cmd, task_log=str(stdout)))
        session.commit()
    if recode != 0:
        print('[Error] (%s) failed' % cmd)
        exit(407)
    print('[Success] (%s) success' % cmd)
    return stdout


if __name__ == '__main__':
    pass
