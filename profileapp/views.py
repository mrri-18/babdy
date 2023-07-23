from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile=form.save(commit=False) #폼 내용을 임시저장
        temp_profile.user=self.request.user
        temp_profile.save()
        return super().form_valid(form)
    def get_success_url(self):
        #프로필(모델)의 user pk를 넘겨줌.
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'
    def get_success_url(self):
        #프로필(모델)의 user pk를 넘겨줌.
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})