# Create your views here.

from django.shortcuts import render_to_response
from models import PoorGays
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from django import forms

class PoorGaysForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    # age = forms.EmailField(required=False)
    # message = forms.CharField()

def list_gays(request):
    gays_list = PoorGays.objects.order_by('-name')[:10]
    return render_to_response('latest_gays.html', {'gays_list': gays_list})
def show_add_page(request):
    print 'I am here'
    print request.method
    c = {}

    return render_to_response("add_gay.html",c,context_instance=RequestContext(request))

def add_gay(request):
    if request.method == 'POST':
        print 'POST ADD Action-> POST'
        post =  request.POST
        print 'Post Data-->++ %s  %s'%(post.get('name'),post.get('age'))
        print request.POST
        p = PoorGays(name=post.get('name'),age=post.get('age'))
        p.save()
        # ... view code here
        return HttpResponseRedirect('/latest/')
    elif request.method == 'GET' :
        print 'POST ADD Action-> GET'
        form = PoorGaysForm()
        print form.as_table()
        c = {'form':form}
        return render_to_response("add_gay.html",c,context_instance=RequestContext(request))
    else :
        print 'other actions'
        post =  request.POST
        print 'POST ADD Action-> ?? %s' %request.method
        print 'Post Data-->-- %s  %s'%(post.get('name'),post.get('age'))
        return HttpResponseRedirect('/')




def indexPage(request):
    print 'index page-->%s'%request.method
    return render_to_response('extend.html')
    return render_to_response('index.html')


def edit_gay(request,gay_id):
    print 'edit gay'
    print 'gay_id --> %s %s'%(gay_id,type(gay_id))
    if request.method == 'GET' and gay_id != None:
        print 'input gay id-->  %s'%gay_id
        p = PoorGays.objects.filter(id=gay_id)[0]
        print p
        print request.GET

        form = PoorGaysForm(
            initial={'name':p.name,'age':p.age}
        )
        print form.as_table()
        form.name = p.name
        form.age = p.age
        print form.name
        print form.age
        c = {'form':form}
        return render_to_response("edit_gay.html",c,context_instance=RequestContext(request))
        # return render_to_response('edit_gay.html',)
    elif request.method == 'POST':
        print request.POST
        return HttpResponseRedirect('/latest/')
    elif request.method == 'PUT':
        print request
        return HttpResponseRedirect('/latest/')
    else:
        return Http404
    pass