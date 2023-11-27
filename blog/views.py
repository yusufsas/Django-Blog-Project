from django.shortcuts import render,get_list_or_404
from. models import Post,Comment,Categories

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def post_list(request):
    categories=Categories.objects.all()
    object_list=Post.published.all()
    paginator =Paginator(object_list,20)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'post/list.html',{'posts':posts,'page':page,'categories':categories})
def post_detail(request,year,month,day,post):
    #post=get_list_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    post=Post.published.get(slug=post)
    categories=Categories.objects.all()
    return render(request,'post/detail.html',{'post':post,'categories':categories})    
    
    

def blogs_by_category(request,slug):
    

    categories=Categories.objects.all()
    
    posts=Post.published.filter(categories__slug=slug)

    return render(request,'post/list.html',{'posts':posts,'categories':categories})
# Create your views here.



def blog_search(request):
     
    if (request.method=='POST'):
        searched=request.POST['searched']
        posts=Post.published.filter(title__contains=searched)
        categories=Categories.objects.all()
        return render(request,'post/list.html',{'posts':posts,'categories':categories,'searched':searched})
    else:

        categories=Categories.objects.all()
        return render(request,'post/list.html',{'categories':categories})
    

def about(request):


    categories=Categories.objects.all()
    return render(request,'post/about.html',{'categories':categories})

   