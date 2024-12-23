from django.shortcuts import render,HttpResponse
from django.contrib import messages
from home.models import Contact

def index(request):
    context={
        "variable":"Hello Ram G"
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is Home page")

def about(request):
    #return HttpResponse("This is About page")
     return render(request,'about.html')


def ice(request):
    #return HttpResponse("This is Servicese page")
     return render(request,'ice.html')
def cake(request):
    #return HttpResponse("This is Servicese page")
     return render(request,'cake.html')

def contact(request):
     if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          Phone=request.POST.get('Phone')
          Subject=request.POST.get('Subject')
          contact=Contact(name=name,email=email,Phone=Phone,Subject=Subject)
          contact.save()
          messages.success(request,'Your request have send')

    #return HttpResponse("This is Contact page")
     return render(request,'contact.html')
