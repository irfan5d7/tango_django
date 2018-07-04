from datetime import datetime
from .session import *

def visitor_cookie_handler(request):
    visits  =  int(request.COOKIES.get('visits','1'))
    last_visit_cookie = request.COOKIES.get('last_visit',str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visit'] = visits
