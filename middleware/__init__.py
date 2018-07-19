from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


# class BlockPath(MiddlewareMixin):
#     def process_request(self, request):
#
#         print('路径', request.path)
#         ok = ['', '', '/main/login', '']
#         if not request.user.is_authenticated and request.path in ok:
#             return redirect('')


# class HeadMiddleware(MiddlewareMixin):
#     def process_response(self, request, response):
#
#         return response
