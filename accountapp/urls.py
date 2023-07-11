from django.urls import path,include

from accountapp.views import hello_world, AccountCreateView

app_name="accountapp" #지정-> hello_wolrd 경로로 접근할 때
urlpatterns = [
    path('hello_world/',hello_world,name='hello_world'), # account 하위 주소인 hello_world 주소로 접근하면 view를 보여주겠다 함수 기반은 그냥 함수명만 써줘도 괜찮
    path('create/',AccountCreateView.as_view(),name='create'), #클래스 기반은 함수와 함께
]