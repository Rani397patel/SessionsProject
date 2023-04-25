import requests
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    request.session.set_test_cookie()
    print('Cookies are set for Initial-request..!')
    return HttpResponse('<h1>Index page of Cookies..</h1><hr/><h2>Request check_view/url...</h2>')
def check_view(request):
    if request.session.test_cookie_worked():
        print('Cookies are working properly')
        request.session.delete_test_cookie()
        return HttpResponse('<h1>Cookie Checking Page Working Properly..!!!</h1><hr />')
    else:
        print('Cookies are NOT working properly')
        return HttpResponse('<h1>Cookie Checking Page NOT-Working Properly..!!!</h1><hr />')

