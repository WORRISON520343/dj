from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World!</h1><img src='https://tse3-mm.cn.bing.net/th/id/OIP-C.bQartF8CZxVcNZ04OcGlAwHaEK?rs=1&pid=ImgDetMain'>")