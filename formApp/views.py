from django.shortcuts import render
from .forms import addStdForm
from .models import addStd
from django.http import HttpResponseRedirect
# Create your views here.
def base(request):
    if request.method=='POST':
        form=addStdForm(request.POST)
        if form.is_valid():
            form.save()
            form=addStdForm()    
    else:
        form=addStdForm()        
    allDbData=addStd.objects.all()
    context={'form':form,'allDbData':allDbData}
    return render(request,'formApp/base.html',context)

def update(request,stdId):
    if request.method=='POST':
        upd=addStd.objects.get(pk=stdId)
        newUpd=addStdForm(request.POST,instance=upd)
        if newUpd.is_valid():
            newUpd.save()
    else:
        upd=addStd.objects.get(pk=stdId)
        newUpd=addStdForm(instance=upd)
    return render(request,'formApp/update.html',{'newUpd':newUpd})



def delete(request,stdId):
    if request.method=='POST':
        dlt=addStd.objects.get(pk=stdId)
        dlt.delete()
        return HttpResponseRedirect('/')
