from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import RegistrationForm, LoginForm, UpdateAccountForm
from accounts.models import Account


def home_view(request):
    return render(request, 'home.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['form'] = form
    else:
        form = RegistrationForm()

    context['form'] = form
    return render(request, 'register.html', context)
    # return render(request, 'reg-test.html', context)

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


def account_login(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = LoginForm()

    context['login_form'] = form
    return render(request, 'login.html', context)


def signout(request):
    logout(request)
    return redirect('login')


def edit_account_view(request, pk):
    context = {}

    user = request.user
    # print(user)
    if not user.is_authenticated:
        return redirect('accounts:login')

    blog_post = get_object_or_404(Account, pk=pk)
    # print(blog_post.email)

    if str(blog_post.email) != str(user):
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = UpdateAccountForm(request.POST or None, request.FILES or None, instance=blog_post)
        print(form.errors)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
            return redirect("home:home_list")
    form = UpdateAccountForm(
        initial={
            'f_name':blog_post.f_name,
            'l_name': blog_post.l_name,
            'sex': blog_post.sex,
            'date_birthday':blog_post.date_birthday,
        }
    )

    context['form'] = form
    return render(request, 'update_account.html', context)