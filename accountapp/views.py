from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.hashers import check_password

from accountapp.decorator import account_ownership_required
# Create your views here.
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership=[account_ownership_required, login_required]


def change_pw(request,pk):
    context = {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                return redirect("accounts:hello_world")

    return render(request,"accountapp/updatee.html")


class AccountCreateView(CreateView):
    model = User #장고 기본 제공 모델
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #class에서 리버스를 그대로 사용할 수 없음.
    template_name = 'accountapp/create.html'
class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'
    paginate_by=10
    def get_context_data(self, **kwargs):
        object_list=Article.objects.filter(writer=self.get_object())#현재 같은 작성자인 아티클들만 필터링
        return super(AccountDetailView,self).get_context_data(object_list=object_list, **kwargs)
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')#일반 함수에 사용하는 데코레이터를 method에도 사용할 수 있도록 함.
class AccountUpdateView(UpdateView):
    model = User #장고 기본 제공 모델
    context_object_name = 'target_user'
    template_name = 'accountapp/updatee.html'


    def get_success_url(self):
        return reverse_lazy('accountapp:hello_world')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


