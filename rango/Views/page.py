from django.http import HttpResponse
from django.shortcuts import redirect

from rango.Forms import *
from rango.Views import show_category
from rango.views import *
def add_page(request,category_name_slug):
    template_name = 'add_page.html'
    try:
        category = Category.objects.get(slug = category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category :
                page = form.save(commit = False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request,category_name_slug)
        else :
            print(form.errors)
    context_dict = {'form':form,'category':category}
    return render(request,'add_page.html',context_dict)


def track_url(request):
    page_id = None
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']

    if page_id:
        try:
            page = Page.objects.get(id = page_id)
            page.views += 1
            page.save()
        except:
            return HttpResponse("Page id {0} not found".format(page_id))
    return redirect(page.url)
