from django.shortcuts import render
from .cookie_handler import *
from rango.models import Category, Page


def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')
    context = {'categories': category_list,"pages":pages_list}
    visitor_cookie_handler(request)
    context.update({'count':request.session['visit']})
    response = render(request, 'index.html', context)
    return response

