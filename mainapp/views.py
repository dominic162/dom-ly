from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from mainapp import models,forms
import string,random
import urllib

def short():
    letters=string.ascii_lowercase
    return(''.join(random.choice(letters) for i in range(6)))

@login_required(login_url='/login')
def dashboard(request):
    context={
        'form':forms.urlmanipulate(),
    }
    if request.method=="POST":
        context['form']=forms.urlmanipulate(request.POST)
        if request.POST['originalurl']!='' and request.POST['shorturl']!='':
            usr=request.user
            originalurl=request.POST['originalurl']
            context['originalurl']=originalurl
            shorturl=request.POST['shorturl']
            context['shorturl']=shorturl
            try:
                element=models.urlshort.objects.get(short_url=shorturl)    
                context['error']='That URL is already taken. Try a different custom url or leave blank to auto generate'
            except:
                obj=models.urlshort(original_url=originalurl,short_url=shorturl,user=usr)
                obj.save()
                context['success']=True
                context['shorturl']=urllib.parse.quote(shorturl)
        elif request.POST['originalurl']!='':
            originalurl=request.POST['originalurl']
            context['originalurl']=originalurl
            usr=request.user
            generated=False
            while not generated:
                shorturl=short()
                try:
                    element=models.urlshort.objects.get(short_url=shorturl)
                except:
                    obj=models.urlshort(original_url=originalurl,short_url=shorturl,user=usr)
                    obj.save()
                    generated=True
            context['shorturl']=urllib.parse.quote(shorturl)
            context['success']=True
        else:
            context['error']='Enter a valid url to shorten'
    return render(request,'home.html',context)

def redr(request,query=None):
    check=get_object_or_404(models.urlshort,short_url=query)
    url_to_go=check.original_url
    return HttpResponseRedirect(url_to_go)

def error404(request):
    return render(request,'404.html')