from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.
# 视图文件
from novel.models import Charpter, Novel


def index(request):
    novels = Novel.objects.filter(type=1)[:6]
    for novelitem in list(novels):
        print('小说名称分别是：', novelitem.novelname)
    print(type(novels))
    print('novels是：', novels)
    context = {
        'novels': novels
    }
    # return HttpResponse(novel.novelname)
    return render(request, 'index.html', context=context)


def content(request, nid):
    # 我只有两本小说的数据，盗墓笔记和霸占你的美，nid为奇数显示盗墓笔记内容，否则为霸占你的美
    if nid % 2 == 1:
        print('-----> 展示内容')
        item = Novel.objects.get(novelname='盗墓笔记')
        articles = Charpter.objects.filter(novelid=5353).order_by('-sid')[:7]
        context = {
            'novel': item,
            'articles': articles
        }
    else:
        item = Novel.objects.get(novelname='霸占你的美')
        articles = Charpter.objects.filter(novelid=67).order_by('-sid')[:7]
        context = {
            'novel': item,
            'articles': articles
        }
        print('-----> 展示霸占你的美内容')
    # 显示小说的详情页
    return render(request, 'content.html', context=context)


def sort(request, nid, page):
    # 显示不同类别的type 和 sort的小说
    # 显示所有章节列表的类容
    novels = Novel.objects.filter(type=nid)

    # contact_list = Contact.objects.all()
    paginator = Paginator(novels, 42)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'novels': novels,
        'page_obj': page_obj
    }
    return render(request, 'sort.html', context=context)


def detail(request, nid):
    # 显示每一章节的内容
    article = Charpter.objects.get(charpterid=nid)
    oldStr = article.content
    # label.text = StrOld.ToString().Replace(" ", "&nbsp;").Replace(Convert.ToString((char)10 ), "&nbsp;" ).Replace(Convert.ToString((char)13 ), "<br>" );
    oldStr = oldStr.replace("'", "''")
    oldStr = oldStr.replace("<", "&lt;")
    oldStr = oldStr.replace(">", "&gt;")
    oldStr = oldStr.replace("\n", "<br>")
    oldStr = oldStr.replace("\t", " &nbsp;&nbsp;&nbsp;")
    oldStr = oldStr.replace("\"", "&quot;")
    context = {
        'article': article,
        'content': oldStr,
    }
    return render(request, 'detail.html', context=context)


def charpter(request, nid):
    # 显示所有的章节
    data = Charpter.objects.filter(novelid=nid).order_by('-charpterid')
    novel = Novel.objects.get(novelid=nid)
    context = {
        'charpters': data,
        'novel': novel,
    }
    return render(request, 'read.html', context=context)


def search_form(request):

    return render(request,'search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            novels = Novel.objects.filter(novelname__icontains=q)
            return render(request,'search_results.html',{'novels': novels, 'query': q})
    return render(request,'search_form.html',{'errors': errors})



