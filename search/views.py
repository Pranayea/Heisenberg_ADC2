from django.shortcuts import render

# Create your views here.
def searchpage(request):
    if request.method=='POST':
        srch= request.POST['searchpage']
        

    
