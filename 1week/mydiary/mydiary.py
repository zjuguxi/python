# coding:utf-8
# mydiary

from sys import argv
# 参数
script, diary = argv
# 打开diary文档
target = open(diary, 'w')
# 在line1:后面输入内容

line1 = raw_input("line1:\n")
# 写入diary
target.write(line1)
# 打印Done表示任务完成
print "Done!"
# 关闭并保存文件
target.close()

target1 = open(diary, "r")
print target1

target1.close()