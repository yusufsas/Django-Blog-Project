from django.urls import path
from . import views


app_name='blog'

urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    path('category/<slug:slug>',views.blogs_by_category,name='blogs_by_category'),
    path('search/',views.blog_search,name='search'),
    
    path('about',views.about,name='about'),
]

