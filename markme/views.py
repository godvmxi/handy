# Create your views here.

from django.shortcuts import render_to_response
from models import PoorGays
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

def latest_gays(request):
    book_list = PoorGays.objects.order_by('-name')[:10]
    return render_to_response('latest_gays.html', {'book_list': book_list})
def show_add_page(request):
    print 'I am here'
    print request.method
    c = {}

    return render_to_response("add_gay.html",c,context_instance=RequestContext(request))

def post_add_gays(request):

    print 'post_add_gays ????????????????'
    post =  request.POST
    print 'Post Data--> %s  %s'%(post.get('name'),post.get('age'))
    print request.POST
    # ... view code here
    return render_to_response("index.html")


    if request.POST == 'POST':
        print 'post_add_gays ????????????????'
        post =  request.POST
        print 'Post Data--> %s  %s'%(post.get('name'),post.get('age'))
        print request.POST
        # ... view code here
        return render_to_response("index.html")
    elif request.POST == 'GET' :
        print 'post add gay get ???'
        return HttpResponseRedirect('/')
        return render_to_response("index.html")
    else :
        return HttpResponseRedirect('/')




def indexPage(request):
    print 'index page'
    return render_to_response('index.html')


