from django.shortcuts import render

# Create your views here.
def collection(request):
    data=[{'name':'Rahul','age':24,'city':"Betul"},
          {'name':'Ajay','age':50,'city':"Bhopal"}
    ]
    return render(request,'collection.html',{'data':data})




