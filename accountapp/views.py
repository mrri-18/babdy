from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    if request.method == "POST": #POST METHOD를 요청받을 경우
         # 텍스트라는 이름에 내용은 POST METHOD! CONTEXT= 데이터 꾸러미, post method가 뜬다= 정상적으로 post 요청을 보내고 응답을 받은 것
         return render(request, 'accountapp/hello_world.html', context={'text':'POST METHOD!'}) #request에 대한 응답
    else:
        return render(request, 'accountapp/hello_world.html', context={'text':'GET METHOD!'})


