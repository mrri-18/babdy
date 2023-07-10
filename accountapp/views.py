from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from accountapp.models import Helloworld
def hello_world(request):

    if request.method == "POST": #POST METHOD를 요청받을 경우
         temp = request.POST.get('hello_world_input')  # hello_world_input 변수의 데이터를 가져와라

         new_hello_world=Helloworld()
         new_hello_world.text=temp
         new_hello_world.save() #db에 객체가 저장됨.
         hello_world_list=Helloworld.objects.all()

         # 텍스트라는 이름에 내용은 POST METHOD! CONTEXT= 데이터 꾸러미, post method가 뜬다= 정상적으로 post 요청을 보내고 응답을 받은 것
         return HttpResponseRedirect(reverse('accountapp:hello_world')) #account/hello_world로 재접속하게하는 response를 보내줌.
         #return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list}) #request에 대한 응답
    else:
        hello_world_list = Helloworld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})


