from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class BlockPath(MiddlewareMixin):
    def process_request(self, request):

        print('路径', request.path)
        ok = ['/tj_shopping/', '/checkout/']
        if (not request.user.is_authenticated) and (request.path in ok):
            print('------------------------重定向')
            return redirect('/')

