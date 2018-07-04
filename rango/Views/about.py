from django.shortcuts import render
from django.template import RequestContext


def about(request):
    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
        request.session.delete_test_cookie()
    context = RequestContext(request)
    visit = int(request.COOKIES.get('visits', '1'))
    context_dict = {'count': visit}
    return render(request, 'about.html', context_dict, context)