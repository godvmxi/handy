# Create your views here.

from django.shortcuts import render_to_response
from models import PoorGays
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

def latest_gays(request):
    gays_list = PoorGays.objects.order_by('-name')[:10]
    return render_to_response('latest_gays.html', {'gays_list': gays_list})
def show_add_page(request):
    print 'I am here'
    print request.method
    c = {}

    return render_to_response("add_gay.html",c,context_instance=RequestContext(request))

def post_add_gays(request):
    if request.method == 'POST':
        print 'POST ADD Action-> POST'
        post =  request.POST
        print 'Post Data-->++ %s  %s'%(post.get('name'),post.get('age'))
        print request.POST
        p = PoorGays(name=post.get('name'),age=post.get('age'))
        p.save()
        # ... view code here
        return HttpResponseRedirect('/')
        return render_to_response("index.html")
    elif request.method == 'GET' :
        print 'POST ADD Action-> GET'
        return render_to_response("index.html")
    else :
        post =  request.POST
        print 'POST ADD Action-> ?? %s' %request.method
        print 'Post Data-->-- %s  %s'%(post.get('name'),post.get('age'))
        return HttpResponseRedirect('/')




def indexPage(request):
    print 'index page-->%s'%request.method
    return render_to_response('extend.html')
    return render_to_response('index.html')


