# 《Automate the boring stuff》学习心得

经过一个多月的懒懒散散的学习，终于啃完这本600多页的Python实战类教科书。在《Automate the boring stuff》（以下简称Automate）中比较重要的内容是，掌握Python基本语法和数据结构，学习一些内建库，同时了解和应用一部分解决职场问题非常方便的第三方库。

由于早先已经学过了《笨方法学Python》，基本语法语法掌握告一段落，因此开头几章比较顺利。下面我标记出（对我而言）比较重要的几个章节，供参考。

《Automate》使用Python3，如果需要多版本共存，可以查看我早先写的如何安装和配置Pyenv的文章。

## [Chapter 5 - Dictionaries and structureing data](https://automatetheboringstuff.com/chapter5/)
Python中Dictionary的用法非常重要，从这里开始，就成为本书中最常使用的数据结构。而用来操作Dictionary的几个函数（如keys/values/get等）则需要多写几行代码来记住用法。

后半章的结构化数据我还没弄非常明白，只是跟着教程完成了Project，有机会要在看一下（写本文的时候，我又看了一遍Dictionary部分，果然忘了好多）。

## [Chapter 7 - Pattern Matching with Regular Expressions](https://automatetheboringstuff.com/chapter7/)
本章学习正则表达式的用法，为后面批量操作文件和写爬虫打好基础。内容稍微有点不好理解，并且需要记忆的地方很多。由于Python2到Python3中升级了部分语法（例如格式化字符**%**统一变成了format.()，不再需要记忆数据类型），因此需要注意目前使用的python版本。

这一章内容多而繁琐，又比较抽象，可能需要多花点时间。

## [Chapter 11 – Web Scraping](https://automatetheboringstuff.com/chapter11/)
爬虫是全书的核心重点之一，也是Python最常用的功能之一。requests/BeautifulSoup这两个库是这个章节中最重要的部分，前者用来下载需要的数据，后者用来解析HTML标签。这两个库构成了本书中设计的简单爬虫的发动机。

## [Chapter 14 - Working with CSV Files and JSON Data](https://automatetheboringstuff.com/chapter14/)
标题内容虽然是CSV和JSON两类数据文件的使用，其实本章节讲的是API的使用（各类服务的API多以JSON等格式来输出数据）。章节不难，但是需要理解数据是怎样通过API来到本地、继而用一些method对数据进行加工和输出。这一章比较有趣，可以举一反三。

## [Chapter 18 – Controlling the Keyboard and Mouse with GUI Automation](https://automatetheboringstuff.com/chapter18/)
本章对普通读者用处可能不大，但生活中却经常见到和使用。朱老师说他正在做的安卓app的向导部分，即使用了本章内容。完整学完这一章，对于类似程序会有一个新的认识，能够理解软件背后的基本原理。

以上五章是这本书的难点和重点，其他章节或者仅涉及Python基础语法，或者仅介绍了一些并不算常用的库（可以现用现学，不用着急背下来）。如果能将这五章内容搞懂，基本上也就理解了全书最紧要的部分。

对我而言，本书最大的收获之一，就是搞明白了一些之前不懂的原理，并且知道了Python到底能做哪些事，为后面的Flask学习打下了基础。