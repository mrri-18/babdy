from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorator import account_ownership_required
# Create your views here.
from accountapp.models import Helloworld
from accountapp.templates.accountapp.forms import AccountUpdateForm

has_ownership=[account_ownership_required, login_required]

@login_required
def hello_world(request):
    if request.method == "POST":  # POST METHOD를 요청받을 경우
        temp = request.POST.get('hello_world_input')  # hello_world_input 변수의 데이터를 가져와라
        new_hello_world = Helloworld()
        new_hello_world.text = temp
        new_hello_world.save()  # db에 객체가 저장됨.

        # 텍스트라는 이름에 내용은 POST METHOD! CONTEXT= 데이터 꾸러미, post method가 뜬다= 정상적으로 post 요청을 보내고 응답을 받은 것
        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # account/hello_world로 재접속하게하는 response를 보내줌.
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list}) #request에 대한 응답
    else:
        hello_world_list = Helloworld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})




class AccountCreateView(CreateView):
    model = User #장고 기본 제공 모델
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #class에서 리버스를 그대로 사용할 수 없음.
    template_name = 'accountapp/create.html'
class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')#일반 함수에 사용하는 데코레이터를 method에도 사용할 수 있도록 함.
class AccountUpdateView(UpdateView):
    model = User #장고 기본 제공 모델
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') #class에서 리버스를 그대로 사용할 수 없음.
    template_name = 'accountapp/update.html'
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'