# Create your views here.

from django.shortcuts import render_to_response
from models import PoorGays
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from django import forms

class PoorGaysForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField()
    age = forms.IntegerField()
    # age = forms.EmailField(required=False)
    # message = forms.CharField()

def list_gays(request):
    gays_list = PoorGays.objects.order_by('-name')[:10]
    return render_to_response('list_gays.html', {'gays_list': gays_list})
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
        return HttpResponseRedirect('/list/')
    elif request.method == 'GET' :
        print 'POST ADD Action-> GET'
        form = PoorGaysForm(initial={'id':0 } )
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
    try:
        gay_id = request.session['gay_id']
    except :
        gay_id = 'can not find gay id'
    return render_to_response('extend.html',{'gay_id':gay_id})
    return render_to_response('index.html')


def edit_gay(request,gay_id):
    print 'gay_id --> %s %s%s'%(gay_id,type(gay_id),request.method)

    if request.method == 'GET' and gay_id != None:
        request.session['gay_id']=gay_id

        print 'input gay id-->  %s'%gay_id
        p = PoorGays.objects.filter(id=gay_id)[0]
        form = PoorGaysForm( initial={'name':p.name,'age':p.age,'id':p.id } )
        c = {'form':form}
        return render_to_response("edit_gay.html",c,context_instance=RequestContext(request))
        # return render_to_response('edit_gay.html',)
    elif request.method == 'POST':
        print request.POST
        print gay_id
        form = PoorGaysForm(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            p= PoorGays.objects.filter(id=cd['id'])[0]
            p.name = cd['name']
            p.age = cd['age']
            p.save()
            return HttpResponseRedirect('/listall/')
        else :
            return Http404


    elif request.method == 'PUT':
        print request
        return HttpResponseRedirect('/list/')
    else:
        return Http404
def delete_gay(request,gay_id):
    if request.method == 'GET':
        print 'delete gay id --> %s '%(gay_id)
        p = PoorGays.objects.filter(id=gay_id)[0]
        print p
        p.delete()
        return HttpResponseRedirect('/')
    else:
        return Http404
def request_cookie(request):
    if "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" %request.COOKIES["favorite_color"])
    else:

        response = HttpResponse("Your do not have favorite color is now,we will set it" )

        # ... and set a cookie on the response
        response.set_cookie("favorite_color",
                            'blue')

        return response
        return HttpResponse("You don't have a favorite color.")
    pass
