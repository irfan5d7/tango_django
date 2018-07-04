from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rango.Views.bing_search import run_query
from rango.Views.index import index
from rango.models import Category
from rango.Forms import *
from rango.views import *
def add_category(request):
    form = CategoryForm()
    template_name = 'add_category.html'
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print(form.errors)
    return render(request,'add_category.html',{'form':form})

def show_category(request,category_name_slug):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    query = None
    if request.method == 'POST':
        query = request.POST
        query =request.POST['query'].strip()

    if query:
        result_list = run_query(query)
        context_dict['result_list'] = result_list
        context_dict['query'] = query
    try:
        category = Category.objects.get(slug = category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category).order_by('-views')
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    if not context_dict['query']:
        context_dict['query'] = category.name
    return render(request, 'category.html', context_dict)
