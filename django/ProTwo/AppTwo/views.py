from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import NewUserForm
from django.http import HttpResponse
# Create your views here.

def index(Request):
    return HttpResponse('<em>Second App</em>')
    # return render(request,'appTwo/help.html')

def help(request):
    helpdict = {'help_insert' : 'Help Page1'}
    return render(request,'appTwo/help.html',context = helpdict)    

def users(request):
    user_list = User.objects.order_by('fname')
    user_dict = {'users':user_list}
    return render(request,"appTwo/users.html",context=user_dict)

def addusers(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('Error Form Invalid!')
    return render(request,"appTwo/signup.html",{'form':form})
