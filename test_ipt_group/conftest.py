# -*- coding: utf-8 -*-
# @Time : 2020/4/2 10:01
# @Author : wangmengmeng
import pytest
from common.alter_config import AlterConfig


@pytest.fixture(scope="session")
def ipt_group():
    """修改配置项-住院医嘱审查模式 为按组号"""
    ac = AlterConfig()
    ac.alter_sys_config(40003, 1)