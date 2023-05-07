from django.urls import path,include

from accountapp.views import hello_world
app_name="accountapp" #지정-> hello_wolrd 경로로 접근할 때
urlpatterns = [
    path('hello_world/',hello_world,name='hello_world') #hello_world 주소로 접근하면 view를 보여주겠다
]