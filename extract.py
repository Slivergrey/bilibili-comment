# coding=utf-8
"""
此文件用于提取收集来的网页信息，生成所有评论的csv文件，方便后续分析
"""
import test
import csv
from bs4 import BeautifulSoup
import re
import pandas as pd

f = open("4-01_BV1364y1S7f7.html", "r", encoding='utf-8')
content = f.read()
# soup= BeautifulSoup(content,"html.parser")
pattern_uid = '<div class="con "><div class="user"><a data-usercard-mid='
pattern_name = re.compile(r'class="name"')
pattern_name_end = re.compile('</a>')
pattern_level = re.compile('<i class="level l')
pattern_comment = re.compile('<p class="text">')
pattern_comment_end = re.compile('</p>')
pattern_comment_time = re.compile('<span class="time">')
pattern_comment_like = re.compile('<span class="like "><i></i><span>')
pattern_comment_info_end = re.compile('</span>')
user_info_temp = []
comment_info = []
index = 0
# info[0]=uid info[1]=name info[2]=level info[3]=comment info[4]=like
for m in re.finditer(pattern_uid, content):
    #    print(content[m.end():m.end() + 10])
    index = m.end() + 1
    while content[index] != '"':
        index = index + 1
    str_temp = content[m.end() + 1:index]
    user_info_temp.append(str_temp)

    match = pattern_name.search(content, index)
    index = match.end()
    while content[index] != '>':
        index = index + 1
    match = pattern_name_end.search(content, index)
    str_temp = content[index + 1:match.start()]
    user_info_temp.append(str_temp)

    match = pattern_level.search(content, index)
    user_info_temp.append(content[match.end()])

    index = match.end()
    match = pattern_comment.search(content, index)
    index = match.end()
    match = pattern_comment_end.search(content, index)
    str_temp = content[index: match.start()]
    user_info_temp.append(str_temp)

    match = pattern_comment_time.search(content, index)
    index = match.end()
    match = pattern_comment_info_end.search(content, index)
    str_temp = content[index: match.start()]
    user_info_temp.append(str_temp)

    match = pattern_comment_like.search(content, index)
    index = match.end()
    match = pattern_comment_info_end.search(content, index)
    if index == match.start():
        str_temp = '0'
    else:
        str_temp = content[index: match.start()]
    user_info_temp.append(str_temp)
    comment_info.append(test.deepcopy(user_info_temp))
    user_info_temp.clear()
print(comment_info)
headers = ['UID', 'username', 'level', 'comment', 'time', 'like']
writer = pd.DataFrame(columns=headers, data=comment_info)
writer.to_csv('4-01_BV1364y1S7f7.csv', encoding='utf-8')
