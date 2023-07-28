from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorator import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


# Create your views here.
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment=form.save(commit=False)
        temp_comment.article=Article.objects.get(pk=self.request.POST['article_pk']) #create.html에서 article_pk 정의
        temp_comment.writer=self.request.user
        temp_comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        #프로필(모델)의 user pk를 넘겨줌.
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk}) #object=article인 상황
@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})