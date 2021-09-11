from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from blog.models import Contact,BlogComment
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
def index(request):
    allPosts =Post.objects.all()
    my_dict={'allPosts':allPosts}
    return render(request,'blog/index.html',context=my_dict)
def contact(request):
    
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        Message=request.POST['text']
        if len(name)<2 or len(phone)<10 or len(email)<3 or len(Message)<10:
            messages.error(request,"Please Fill the form Appropriatly")
        else:
            contact=Contact( Name=name,phone_no=phone,email=email,problem=Message)
            contact.save()
            messages.success(request,"Form Submitted Sucessfully")
    return render(request,'blog/contact.html')
def about(request):
    return render(request,'blog/about.html')
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
        messages.warning(request,"Please Check your Search And Refine it")
    else:
        allPosts=Post.objects.filter(title__icontains=query)
        #allPostsContent=Post.objects.filter(content__icontains=query)
        #allPosts=allPoststitle.union(allPostsContent)
    params={'allPosts':allPosts,'query':query}
    return render(request,'blog/search.html',params)
def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)>10:
            messages.warning(request,"Username should be of length less than 10")
            return redirect('/') 
        if pass1!=pass2:
            messages.warning(request,"Your Passward is Not Maching")
            return redirect('/') 
        if not username.isalnum():
            messages.warning(request,"Your Username only contain Letters and Numbers")
            return redirect('/') 
        myuser=User.objects.create_user(username=username,email=email,password=pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"You are now User of this Blog Page")
        return redirect('/')
    else: 
        return HttpResponse("404- page not found")
def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass1=request.POST['loginpass1']
        user =authenticate(username=loginusername,password=loginpass1)
        if user is not None:
            login(request,user)
            messages.success(request,"You are sucessfully loged in")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials , please try again")
            return redirect('/')
    else:
        return HttpResponse('404 -- Not Found')
def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully Loged Out")
    return redirect('/')
def blogpage(request):
    post =Post.objects.filter().first()
    comment=BlogComment.objects.filter(post=post)
    my_dict={'post':post,'comments':comment}
    return render(request,'blog/blogpage.html',context=my_dict)
def postComment(request):
    if request.method=="POST":
        comments=request.POST['comment']
        user=request.user
        postSno=request.POST['postSno']
        post=Post.objects.get(S_no=postSno)
        comment=BlogComment(comment=comments,user=user,post=post)
        comment.save()
        messages.success(request,"Your Comment is Posted Sucessfully")
    return redirect(request,'blog/blogpage.html')
