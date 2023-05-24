from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from Auth.forms import UserRegistrationForm
from Auth.models import Users
from globalUtils import HandleUploadedFile


#
# def auth(request):
#     form = UserRegistrationForm()
#     return render(request, 'Auth/regin.html',{'form': form})

def index(request):
    if request.method == "POST":
        if 'signin_button' in request.POST:
            return HttpResponse("Вошел")

        elif 'register_button' in request.POST:
            return HttpResponse("Зарегался")

    return render(request, 'Auth/login.html')


# class UserRegistrationView(View):
#
#
#     def get(request, **kwargs):
#         return render(request, '../templates/Auth/login.html', context={'form': UserRegistrationForm})
#
#
#     def post(request, **kwargs):
#         form = UserRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             print('Flag 1')
#             form.save(commit=True)
#             #try:
#             #    Users.save()
#             #except:
#             #    print(1)
#         nickName = request.POST.get("login")
#         eMail = request.POST.get("email")
#         #path = HandleUploadedFile(request.FILES['Photo'],
#         #                          'static/users/img/',
#         #                          request.FILES['Photo'].name)
#
#         context = {
#             'nick': nickName,
#             'eMail': eMail,
#             #'photo': '/' + path,
#         }
#         return render(request, '../templates/Profile/profile.html', context=context)


