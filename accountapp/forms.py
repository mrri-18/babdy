from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled=True #id칸을 비활성화 시킴. 서버에 반영되지 않음.
    def change_pw(request):
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
                    return redirect("account:hello_world")
                else:
                    context.update({'error': "새로운 비밀번호를 다시 확인해주세요."})
        else:
            context.update({'error': "현재 비밀번호가 일치하지 않습니다."})

        return render(request, "accountapp/updatee.html", context)