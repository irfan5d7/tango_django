from django.shortcuts import render

from rango.Views.bing_search import run_query


def search_bing(request):
    result_list = []
    template_name = 'search.html'
    if request.method =="POST":
        query = request.POST['query'].strip()
        if query:
            result_list = run_query(query)
    return render(request,'search.html',{'result_list':result_list})