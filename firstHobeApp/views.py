from django.shortcuts import render

def welcome(request):
    return render(request,"welcome.html")

def hello(request):
    print('hello')
    user_name = request.GET['name']
    return render(request,"hello.html",{'userName' : user_name})