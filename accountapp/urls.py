from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    change_pw

app_name="accountapp" #지정-> hello_wolrd 경로로 접근할 때
urlpatterns = [
    path('create/',AccountCreateView.as_view(),name='create'), #클래스 기반은 함수와 함께
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    # detail에 접근하기 위해서는 pk(user id)가 필요함. pk라는 이름의 int 정보를 받겠다
    path('detail/<int:pk>',AccountDetailView.as_view(),name='detail'),
    #path('update/<int:pk>',AccountUpdateView.as_view(),name='update'),
    path('updatee/<int:pk>',change_pw, name='updatee'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]