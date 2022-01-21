# -*- coding: utf-8 -*-
import pyltp 
import os
from definitions import ROOT_DIR
LTP_DATA_DIR = os.path.join(ROOT_DIR, 'data', 'ltp_data_v3.4.0')
from KGQA.util.log_util import LogUtil
log_util = LogUtil()

def cut_words(words):
    segmentor = pyltp.Segmentor()
    seg_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
    segmentor.load(seg_model_path)
    words = segmentor.segment(words)
    array_str="|".join(words)
    array=array_str.split("|")
    segmentor.release()
    log = "分词后的结果:  [" + ','.join(array) + "]"
    log_util.info(log)
    return array

def words_mark(array):
    # 词性标注模型路径，模型名称为`pos.model`
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
    postagger = pyltp.Postagger()  # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    postags = postagger.postag(array)  # 词性标注
    pos_str = ' '.join(postags)
    pos_array = pos_str.split(" ")
    postagger.release()  # 释放模型
    log = "词性标注后的结果:  [" + ','.join(pos_array) + "]"
    log_util.info(log)
    return pos_array

def get_target_array(words):
    target_pos = ['nh', 'n']
    target_array = []
    seg_array = cut_words(words)
    pos_array = words_mark(seg_array)
    for i in range(len(pos_array)):
        if pos_array[i] in target_pos:
            target_array.append(seg_array[i])

    target_array.append(target_array[0])
    log = "得到的目标词:  [" + ','.join(target_array) + "]"
    log_util.info(log)
    return target_array





