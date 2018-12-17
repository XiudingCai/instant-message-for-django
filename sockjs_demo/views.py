# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_sockjs_server.lib.client import SockJsServerClient


def index(request):
    context = RequestContext(request)

    template = "sockjs_demo/index.html"


    return render_to_response(template, context)

def send_test_message(request):
    context = RequestContext(request)
    a = SockJsServerClient()
    # channel = a.gen_channel()
    a.gen_c_token('user2')
    test_message = dict()
    test_message['channel'] = 'user2'
    test_message['data'] = dict()
    test_message['data']['user_name'] = "Sergey Kravchuk"
    test_message['data']['user_id'] = 1
    a.publish_message(test_message, 'MQ1')
    # rec = a.get_connections('user')
    # print(rec)

    template = "sockjs_demo/send_test_message.html"
    return render_to_response(template, context)
