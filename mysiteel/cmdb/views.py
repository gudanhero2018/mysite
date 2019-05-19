from django.shortcuts import render
from cmdb import models
from django.shortcuts import HttpResponse
# Create your views here.
user_list=[
    {"user":"jack","pwd":"abc"},
    {"user":"Tom","pwd":"ABC"},
]

def index(request):
    #return HttpResponse('Hello Django!')
    #return render(request,"index.html",)
    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        models.UserInfo.objects.create(user=username,pwd=password)
    user_list=models.UserInfo.objects.all()
        #temp={"user":username,"pwd":password}
        #user_list.append(temp)
        #print(username,password)
    return render(request,"index.html",{"data":user_list})