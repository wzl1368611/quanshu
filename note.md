# DJANGO 项目实战日志
- 一个diango项目至少要包含一个应用
路由 videos bbs question
ORM
写模型 映射到数据库
自己有数据库，把数据库生成模型
命令：python manage.py inspectdb > novel/models.py

 <!--
<li><a target="_blank" href="{% url 'content' novel.novelid %} " title={{ novel.novelname|safe }} class="msgBorder"><img src="http://img.quanshuwang.com/image/9/9055/9055s.jpg" width="120" height="150"></a><img src="{% static 'images/only2.png' %}" class="topss png_bg"><a href="http://www.quanshuwang.com/book_9055.html" title="盗墓笔记" class="clearfix">盗墓笔记</a>类别：<a href="/list/9_1.html">恐怖灵异</a><br>作者：<a href="/modules/article/authorarticle.php?author=%C4%CF%C5%C9%C8%FD%CA%E5">南派三叔</a></li>
    -->
    
在html加staticfiles的话需要设置：
     'libraries': {
              'staticfiles': 'django.templatetags.static',
            },
TODO 搜索页面，分类页面


### todo
- 只有使用Python manage.py runserver 0.0.0.0:8000才有效

