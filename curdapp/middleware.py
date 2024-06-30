# curdapp/middleware.py

from django.http import HttpResponseNotFound

class DisableFaviconMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ['/favicon.ico', '/favicon.png']:
            return HttpResponseNotFound()
        return self.get_response(request)
