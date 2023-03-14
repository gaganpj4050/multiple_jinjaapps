from django.shortcuts import render

# Create your views here.
def virat_print(request):
    d={'name':'virat kohli','age':34}
    return render(request,'virat_print.html',context=d)