def get_server_side_cookie(request,cookie,default_val = None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

