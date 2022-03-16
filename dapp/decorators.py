from django.http import HttpResponse
from django.shortcuts import redirect


# def unauthenticated_user(viewFunc): #  viewFunc is function  for login.html
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('dashboard')
#         elif request.user.is_authenticated == None:
#             return redirect('login')
#         else:
#             return viewFunc(request, *args, **kwargs)
#     return wrapper