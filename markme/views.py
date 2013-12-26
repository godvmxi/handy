# Create your views here.

from django.shortcuts import render_to_response
from models import PoorGays
from django.http import HttpResponse, Http404

def latest_gays(request):
    book_list = PoorGays.objects.order_by('-name')[:10]
    return render_to_response('latest_gays.html', {'book_list': book_list})
def add_gay(request):
    print 'I am here'
    print request.method
    if request.method =='GET':
        return render_to_response("add_gay.html",{})
    elif request == 'POST':
        print 'POST actions'
        return HttpResponse(content='help me hheh eheh',status=200)
    else:
        return Http404('404')

    return HttpResponse(content='help me hheh eheh',status=200)
    # if request.method == request.GET :
    #     print 'add gay Get request'
    #     return  'try to get add gays'
    # elif request,memoryview== request.POST :
    #     print 'add gay Post request'
    #     return  'try to get post gays'
    # else :
    #     print 'Wrong request method'


