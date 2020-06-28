学习笔记
1.作业提交：
git add .
git commit -m "代码提交的说明"
git push -u origin master
2.抓取的过程中会遇到反爬的情况，需要在header中添加cookie。
    对于scrapy来说，在settings中设置，将COOKIES_ENABLED = False注释打开，表示不用默认的cookie,
    将自定义cookie信息添加到DEFAULT_REQUEST_HEADERS下.
3.xpath匹配
    从当前位置向下匹配查找时，每一级标签都要写出，一直写到目标标签.
    extract的作用:从选择器(已经匹配到结果的选择器)中返回要提取的内容
