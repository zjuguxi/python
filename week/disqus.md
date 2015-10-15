# 配置Disqus
10/15/2015 12:22:58 PM 

配置Disqus是目前为止让我花费时间最多的，中间经历了大量坑、却又跳不出来。还好在同学的帮助下通过修改book.json的方式实现。所以如果有跟我遇到相同情况的朋友，请注意，第一时间修改book.json试试。

## 背景
在学会了用Sourcetree管理Github上的仓库、以及将Github与Gitbook关联之后，按照课程要求需要给自己的Gitbook输出的电子书配置上Disqus这个第三方评论功能。之前我帮助老婆公司网站配置过，有点印象，因此并没觉得是个很难的事情。

## 安装

1. 首先注册Disqus账号，然后点击右上角的齿轮标志，再点击**Add Disqus To Site**。
![step1](http://i.imgur.com/1hWVD5a.jpg)
2. 点击**Start Using Engage**，进入配置界面。
![](http://i.imgur.com/3r81Kza.jpg)
3. 填写信息。这一步很简单。
![step3](http://i.imgur.com/Ib5s25z.jpg)
4. 这一步我已经配置好，所以不重复操作。此时你应该已经可以进入Manage页面了。点击**Edit Setting**
![step4](http://i.imgur.com/2QdpRPe.jpg)
5. 在Basic中将一下两项写好。
![step5](http://i.imgur.com/V4T5oWn.jpg)
6. 在Advanced中，将`gitbook.com`和`gitbooks.io`填写入Trusted Domains，确保电子书输出的网址被Disqus信任。
![step6](http://i.imgur.com/nhvVk6W.jpg)

至此，Disqus站点上的前序配置已经完成，剩下的是重头戏了。

## 配置

1. 创建一个book.json文档，放在根目录下。

    这里有个小方法，在Gitbook的电子书编辑页面，点击**Add Plugin**，Gitbook会自动生成一个book.json，这样无需手动添加了。

![](http://i.imgur.com/dXTDXd4.jpg)

2. 将[这里](https://github.com/liangchaob/itdmb-python/blob/master/book.json)的代码复制到你的book.json中，并修改中间配置信息为你自己的。

代码如下：（**请勿直接复制代码！！！**）

    {"title": "itdmb-python",
    "version": "15.10.14",
    "description": "python速查手册",
    "author": "liangchao <liangchaob@163.com>",
    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "itdmb-python"
        }
    } 
}

**注意，上方有半个大括号在代码框以外，这也是一个容易掉坑的地方，请一定完整输入代码！！**

## 使用
完成以上步骤后，commit+push将代码提交至仓库，很快Gitbook上就能看到Disqus的评论栏了。

## 体验
看了其他同学的发言，觉得大家把这个问题复杂化了。不用安装git，不用安装node.js，也不用安装gitbook，一切只要web端完成+SoureceTree（你有可能用的是Github桌面客户端，一样）提交即可。

因此，在完成任务之前，看过多同路人的半吊子方法论，似乎对自己并无帮助。我就看很多教程说先安装npm再配置disqus觉得很困惑：明明是全部都在web端配置好的，为什么要在本地安装一个npm呢？事实证明，确实是并不需要的。

只要想好原理是什么，就能绕过这些弯路了。