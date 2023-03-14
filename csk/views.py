from django.shortcuts import render

# Create your views here.
def dhoni_print(request):
    d={'name':'MS Dhoni','age':41}
    return render(request,'dhoni_print.html',context=d)