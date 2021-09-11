"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views
admin.site.site_header="TechBLOG Admin"
admin.site.site_title="Tech Admin"
admin.site.index_title="Welcome To Tech Blog Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^about/',views.about,name='about'),
    url(r'^blogpage/',views.blogpage,name='blogpage'),
    url(r'^search/',views.search,name='search'),
    url(r'^signup',views.handlesignup,name='signup'),
    url(r'^login',views.handlelogin,name="login"),
    url(r'^logout',views.handlelogout,name="logout"),
    url(r'^postComment',views.postComment,name="post_comment"),
]
