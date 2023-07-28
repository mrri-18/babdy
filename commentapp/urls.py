from django.urls import path

from articleapp.views import ArticleListView
from commentapp.views import CommentCreateView, CommentDeleteView

app_name='commentapp'
urlpatterns=[
    path('create/',CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]