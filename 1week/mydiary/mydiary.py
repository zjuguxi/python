# coding:utf-8
# mydiary

from sys import argv
# 参数
script, diary = argv

# 打开并读取文件内容
data = open("diary.txt").read()
# 如果txt中有内容，则打印，否则显示提示语、
if len(data) > 0:
    print data
elif len(data) == 0:
    print "This diary is empty."


# 打开diary文档
target = open(diary, 'a')
# 在line1:后面输入内容
line1 = raw_input("line1:")
# 写入diary
target.write("\n" + line1)
# 打印Done表示任务完成
print "Done!"
# 关闭并保存文件
target.close()

target1 = open(diary, "r")
print target1

target1.close()