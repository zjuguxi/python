# Git命令

> 刚开始学习Python的时候，我希望能够尽最大可能的窄化学习内容，于是命令行这些能省就省，版本管理也用图形化界面的SourceTree。周六下午的深圳线下聚会中，深圳教练`弓和箭`说，这些还是要学的，于是准备用一天时间（依然不想）学习一下Git最简单的几个命令。

## 目标
脱离图形化界面的SoureceTree，并实现双推（分别将新版本文件推送至Github和Gitbook）和多推(包括加分题160推)。

## 初始化后的几个基础命令
```
git init # 仓库初始化
git add # 添加文件到暂存(这里可以依次add很多次修改，然后一次commit就全部提交。同一个文件有多次修改、每次修改后都add一次，add命令只将前一次修改添加到暂存区)。
git commit -m"" # -m"xxx"这里是提交日志，就是说本次commit改了些什么
```
## 检查仓库状态，查看修改内容
```
git status # 仓库状态，看是否有文件修改了。
git diff # 查看修改内容（只能在文件被add之前查看区别，一旦被add则无法查看修改内容）。
```
## 在不同文件版本之间跳跃
```
HEAD # 指当前版本。
HEAD^ # 指前一个版本
HEAD^^ # 指前两个版本
HEAD~100 # 指前100个版本
git reset --hard [commit_id] # 指跳跃到某个版本
git log # 查看提交历史，以便回退
git reflog # 查看命令历史，以便前进到未来的某个版本
```
## 撤销修改
```
git checkout -- file # 丢弃工作区的修改
git reset HEAD file # 丢弃缓存区的修改
```
## 删除文件
```
rm file # 删除工作区中的该文件
git rm file # 删除版本库中的该文件
git checkout -- file # 用版本库的版本恢复工作区的版本
```
**上图是我理解的Git命令中几个关键动作的逻辑，不知是否正确，请指教！**
![git reset](http://i.imgur.com/GWEN4yg.jpg)

## 配置SSH
用Git链接Github远程仓库，需要首先配置ssh。我OS X与Win系统双持，因此两个系统都需要单独配置ssh。
[Mac的SSH配制方法](https://help.github.com/articles/generating-ssh-keys/#platform-mac)
[PC的SSH配制方法](https://help.github.com/articles/generating-ssh-keys/#platform-windows)
### 一个小问题
然而在配置PC的SSH时，出现了一个小问题。
按照教程的Step3-1，我用的终端为Git Bash，因此应该输入以下代码：
```
ssh-agent -s
```
但是，得到的结果和教程有区别：
```
SSH_AUTH_SOCK=/tmp/ssh-3aaVdTkjdnG0/agent.7204; export SSH_AUTH_SOCK;
SSH_AGENT_PID=7724; export SSH_AGENT_PID;
echo Agent pid 7724;
```
我忽略之，继续Step3-2,输入：
```
ssh-add ~/.ssh/id_rsa
```
立刻出现了以下错误信息：
```
Could not open a connection to your authentication agent
```
对这种情况完全没有头绪，不清楚问题出在哪里，火速上stackoverflow抱大腿：
[Stackoverflow上的答案](http://unix.stackexchange.com/questions/48863/ssh-add-complains-could-not-open-a-connection-to-your-authentication-agent/48868#48868)
答案告知运行以下代码试试：
```
eval "$(ssh-agent)"
```
随后问题解决！
### 小问题回顾
我又仔细回顾了一下这个问题，发现其实在官方帮助文件[PC的SSH配制方法](https://help.github.com/articles/generating-ssh-keys/#platform-windows)中确实提到过这个方法，但是是在使用Git Bash以外的其他终端的情况下。我使用的恰恰是Git Bash啊，为什么也需要用这种方法打开ssh agent？
> Git版本2.6.1

![ssh agent](http://i.imgur.com/lEd52uW.jpg)
### 遗留问题
每次将本地代码推送至Github的远程仓库时，都问我一遍密码，目前还未解决，只能每次push都输入一遍了。
![ask password](http://i.imgur.com/E1Fuw65.jpg)

## 添加、克隆远程库
```
git remote add origin git@github.com:zjuguxi/python.git # 将本地仓库与远程仓库关联起来
git push origin master 将本地代码推送至远程库
git clone git@github.com:xxx/yyy.git # 从远程仓库克隆到本地

```
## 管理分支
```
git branch # 查看分支
git branch name # 创建分支
git checkout name # 切换分支
git checkout -b name # 创建+切换分支
git merge name # 合并某分支到当前分支
git branch -d name # 删除分支
```

## gitignore
在`.gitignore`文件中配置在工作目录中、但不会被提交的文件
[Python的gitignore](https://github.com/zjuguxi/gitignore/blob/master/Python.gitignore)

## 配置别名
Git命令可以用别名来替代
```
git config --global alias.st stasus # 用st代替status
```
当前用户的Git配置文件在主目录下的一个隐藏文件`.gitconfig`中。
配置别名可以直接修改这个文件，如果出错，可以删掉文件重新通过命令行配置。
```
$ cat .gitconfig
[alias]
    co = checkout
    ci = commit
    br = branch
    st = status
[user]
    name = Your Name
    email = your@email.com
```
## 略过的部分
我通过[廖雪峰的Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)进行学习，虽然已经是精简教程，但是仍然有大量（对我来说）平时用不到的内容，以下为我略过的部分。有兴趣可自行查考。
- 分支管理
	- 解决冲突
	- 分支管理策略
	- Bug分支
	- Feature分支
	- 多人写作
- 标签管理
	- 创建标签
	- 操作标签
- 搭建Git服务器


## 朱老师推荐的Git简明教程
这里再推荐一点补充材料，由朱作君老师推荐的一些更为简练的教程，确实不错，有兴趣可以看一看

http://rogerdudler.github.io/git-guide/index.zh.html

http://yedingding.com/2013/09/11/practical-git-flow-for-startups.html
