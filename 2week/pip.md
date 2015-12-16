# 安装pip及其他包

tkinter还是没解决，也还没看别人的解决方案。看不懂先不看了，继续打基础去看笨方法。

目前学到了ex46，之前关于类的ex42的加分题3没有做。类这个概念现在与其说理解、不如说接受，因为很难将class这个东西与认知系统里面已经存在的近似物匹配起来，所以就强行插入这个概念吧。对我来说这样反而更简单一点——类这个东西，就强行记住是干啥的，背下来就行了，然后多抄几段代码，多读几段代码，研究它的工作原理。

## 不鸡巴废话了

我发现还是要说脏话，才比较好凸显我对学习过程中遇到的各式障碍的态度——如毛主席所说，『战略上藐视，战术上重视』。

最近买了个阿里云服务器，因此除了python之外，还顺便学了一点Linux，背了几个常用命令。其实关于命令行的学习，之前已经接触了一些，但是没有聚焦在Linux上，因此Linux常用工具和命令都没有涉及。服务器安装了CentOS，虽然是个空机器，但各种软件已经集成进去，因此wget之类，直接可用。

然而我在Mac上按照[某中文教程](http://blog.csdn.net/fancylovejava/article/details/39140373)安装pip的时候，直接使用wget命令，在Mac上提示`command not found`。

操你妈的，又缺零件！！！

由此导致了我向朱老师抱怨Mac还不如Linux好用，双方进行了一番争论，并像往常一样『是是是朱老师说的是』结束争论，老老实实手动下载`get-pip.py`到本地（习惯性放到桌面上），然后`python get-pip.py`，出现以下提示：

`

$ sudo python get-pip.py

Password:

The directory '/Users/apple/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.

The directory '/Users/apple/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.

Requirement already up-to-date: pip in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pip-7.1.2-py2.7.egg

`

