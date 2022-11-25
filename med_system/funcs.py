from urllib.parse import quote
from django.http import HttpRequest, HttpResponse

def get_and_add_cookie(request: HttpRequest, to_add: str, resp: HttpResponse) -> HttpResponse:
    to_add = quote(to_add, safe='!#/')
    cookie = request.COOKIES.get('nav', '')
    idx = cookie.find(to_add)
    if (idx == -1):
        cookie += to_add
    else:
        cookie = cookie[:idx + len(to_add)]
    resp.set_cookie('nav', cookie, samesite='Strict')
    return resp