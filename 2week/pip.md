# 安装pip及其他包

tkinter还是没解决，也还没看别人的解决方案。看不懂先不看了，继续打基础去看笨方法。

目前学到了ex46，之前关于类的ex42的加分题3没有做。类这个概念现在与其说理解、不如说接受，因为很难将class这个东西与认知系统里面已经存在的近似物匹配起来，所以就强行插入这个概念吧。对我来说这样反而更简单一点——类这个东西，就强行记住是干啥的，背下来就行了，然后多抄几段代码，多读几段代码，研究它的工作原理。

## 不鸡巴废话了

我发现还是要说脏话，才比较好凸显我对学习过程中遇到的各式障碍的态度——如毛主席所说，『战略上藐视，战术上重视』。

要安装下面几个玩意：

1. pip – [http://pypi.python.org/pypi/pip](http://pypi.python.org/pypi/pip)
2. distribute – [http://pypi.python.org/pypi/distribute](http://pypi.python.org/pypi/distribute)
3. nose – [http://pypi.python.org/pypi/nose/](http://pypi.python.org/pypi/nose/)
4. virtualenv – [http://pypi.python.org/pypi/virtualenv](http://pypi.python.org/pypi/virtualenv)



## 安装pip

最近买了个阿里云服务器，因此除了python之外，还顺便学了一点Linux，背了几个常用命令。其实关于命令行的学习，之前已经接触了一些，但是没有聚焦在Linux上，因此Linux常用工具和命令都没有涉及。服务器安装了CentOS，虽然是个空机器，但各种软件已经集成进去，因此wget之类，直接可用。

然而我在Mac上按照[某中文教程](http://blog.csdn.net/fancylovejava/article/details/39140373)安装pip的时候，直接使用wget命令，在Mac上提示`command not found`。

操你妈的，又缺零件！！！

由此导致了我向朱老师抱怨Mac还不如Linux好用，双方进行了一番争论，并像往常一样以『是是是朱老师说的是』这样认真诚恳的态度结束争论，老老实实手动下载`get-pip.py`到本地（习惯性放到桌面上），然后`python get-pip.py`，出现以下提示：

``` python
$ sudo python get-pip.py
Password:

The directory '/Users/apple/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.

The directory '/Users/apple/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.

Requirement already up-to-date: pip in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pip-7.1.2-py2.7.egg
```

插一句嘴：注意Markdown在引用代码时候的一个细节，\` \` 用于在文章中插入一句代码，而\```  \``` 则用于插入整个代码块。我插入上述代码块的时候还折腾了一下下。 

阅读提示后，发现是文件夹权限问题，desktop的上级文件夹不属于当前用户。于是使用最高权限`sudo python get-pip.py`，依旧出现上述问题。朱老师后来提示我，如果是系统权限就用`sudo`，如果是文件权限就用`chmod`，所以估计`sodu`不是解决方案，改用`chmod`。

``` python
$ chmod get-pip.py
usage:	chmod [-fhv] [-R [-H | -L | -P]] [-a | +a | =a  [i][# [ n]]] mode|entry file ...
	chmod [-fhv] [-R [-H | -L | -P]] [-E | -C | -N | -i | -I] file ...

$ python get-pip.py
Requirement already up-to-date: pip in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pip-7.1.2-py2.7.egg
```

这下提示少了很多废话（上面提示权限的那一坨），随便搜了一下这句话，在stackoverflow找到个哥们跟我遇到[一模一样的问题](http://stackoverflow.com/questions/22278138/where-is-pip-installed-to-when-using-get-pip-py)。又在[这篇文章](http://blog.sina.com.cn/s/blog_8808cae20102viej.html)里看到出现『already up-to-date』就是已经安装好了的标志，于是停止折腾（这几行字泥马从一开始就有啊），估计Mac的Python自带pip了吧。

## 安装distribute

在搜索 Mac 安装distribute过程中，看到[这篇文章](http://blog.csdn.net/ichuzhen/article/details/24640299)讲解了一下几个包管理工具，发现distribute似乎过时了（最新版本0.7.3更新日期是2013年7月5日），现在老司机都用setuptools，于是擅自做主，放弃distribute，改安装setuptools。

## 安装setuptools

