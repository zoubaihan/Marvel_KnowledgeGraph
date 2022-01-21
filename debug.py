# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: Lenovo
@Email: 21212010059@m.fudan.edu.cn
@Created: 2021/12/19
------------------------------------------
@Modify: 2021/12/19
------------------------------------------
@Description:
"""
from KGQA.ltp import get_target_array
from neo_db.query_graph import get_KGQA_answer
question = "小辣椒的爱人的敌人的朋友是谁"
json_data = get_KGQA_answer(get_target_array(str(question)))
