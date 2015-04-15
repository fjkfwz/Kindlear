# Kindlear
Kindle Ear自动部署工具
#使用Kindle Ear搭建RSS推送平台
>Github项目仓库：https://github.com/cdhigh/KindleEar

>Kindle Ear是一个运行在Google App Engine(GAE)上的Kindle个人推送服务器，生成排版精美的杂志模式MOBI格式自动每天推送至您的kindle，
此网站应用目前的功能有：
1.支持类似calibre的recipe格式的自定义RSS收集，需要写代码，需要有一点点python基础
2.自定义RSS，不需要python基础，直接输入RSS链接和标题即可自动推送
3.多账号管理，也就是支持多kindle
4.带图的杂志格式MOBI
5.自动每天定时推送
6.强大而且方便的邮件中转服务
注：如果您要求不高，自定义RSS推送功能能应付一般应用，如果要求排版和完美，可以参照books目录下的文件自己增加一个文件， 在您懂python的前提下，您可以完全的操控网页，可以生成您需要的最完美的MOBI文件。

##Kindle Ear部署步骤
>1.申请GAE账号并创建一个application。 https://appengine.google.com/
2.下载GAE SDK。 https://developers.google.com/appengine/downloads?hl=zh-CN
3.安装Python 2.7 如果已经安装了，跳过此步骤
4.下载本应用的所有文件，放到一个特定的目录
5.将我的项目clone下来，``项目地址：https://github.com/fjkfwz/Kindlear`` 解压后将目录改名为kindleear，放到uploader目录下， 双击uploader.bat按照提示输入GAE认证信息及项目名即可上传
