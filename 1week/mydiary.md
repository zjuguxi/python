# 我的日记

完成一个极简交互式日记系统,需求如下:
- 一次接收输入一行日记
- 保存为本地文件
- 再次运行系统时,能打印出过往的所有日记

## 尝试一
运用笨方法学python中ex16的方法对文件进行读写

    # coding:utf-8
    # mydiary

    from sys import argv
    # 参数
    script, diary = argv
    
    # 打开diary文档
    target = open(diary, 'a')
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

- 实现每次接收输入一行日记
- 可以保存为本地文件diary.txt
- **但还没有实现再次运行时打印过往日记**

## 尝试二
增加了运行时打印过往日记的代码：

    # 打开并读取文件内容
    data = open(diary.txt).read()
    # 如果txt中有内容，则打印，否则显示提示语、
    if len(data) > 0:
        print data
    elif len(data) == 0：
        print "This diary is empty."

- 可以实现全部功能
- **但是文字部分没有分行，`raw_input`输入的内容全在同一行**

## 尝试三
在将`target.write(line1)`改为`target.write("\n" + line1)`，即在每次输入内容前换行，实现每次输入的内容单独成行的效果。

## 最终代码
    
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