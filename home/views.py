from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from accounts.models import Account
from home.models import HomeArticleModel, HomeCarouselModel
from home.forms import CreateHomeForm, ReviewsFrom


#
# class HomeView(ListView):
#     model = HomeArticleModel
#     template_name = "home.html"
#     context_object_name = 'home_post'

#

def home_list(request,):
    context = {}
    home1 = HomeArticleModel.objects.all()
    home = HomeCarouselModel.objects.all()

    context = {
        'home_post': home1,
        'home_blog': home
    }

    return render(request, "home.html", context)


def paginate(request):
    contact_list = HomeArticleModel.objects.all()
    paginator = Paginator(contact_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'paginate.html', {'page_obj': page_obj})



def home_create(request):
    if request.method == "POST":
        instance = CreateHomeForm(request.POST or None, request.FILES or None)
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')

        if instance.is_valid():
            obj = instance.save(commit=False)
            author = Account.objects.filter(email=user.email).first()
            try:
                author = Account.objects.get(email=user.email)
            except:
                return Account.DoesNotExist
            obj.author = author
            obj.save()
        # messages.success(request, f'Ссылка добавлена')
    else:
        instance = CreateHomeForm()

    return render(request, 'CRUD/create.html', {'form': instance})


def detail_home_view(request, pk):
    context = {}
    blog_post = get_object_or_404(HomeArticleModel, pk=pk)
    context['blog_post'] = blog_post

    return render(request, 'CRUD/detail.html', context)


def detail_home_carousel(request, pk):
    context = {}
    blog_post = get_object_or_404(HomeCarouselModel, pk=pk)
    context['blog_post'] = blog_post

    return render(request, 'CRUD/detail.html', context)


def edit_home_view(request, pk):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:login')

    home_post = get_object_or_404(HomeArticleModel, pk=pk)

    # if blog_post.author != user:
    #     return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = CreateHomeForm(request.POST or None, request.FILES or None, instance=home_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
            return redirect("home:home_blog")
    form = CreateHomeForm(
        initial={
            'title': home_post.title,
            'body': home_post.body,
            'image': home_post.image,
        }
    )

    context['form'] = form
    return render(request, 'CRUD/update.html', context)




class AddReview(View):


    # def post(self, request, pk):
    #     print(request.POST)
    #     return redirect('/')

    # def post(self, request, pk):
    #     form = ReviewsFrom(request.POST)
    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.article_id = pk
    #         form.save()
    #     return redirect('/')


    def post(self, request, pk):
        form = ReviewsFrom(request.POST)
        article = HomeArticleModel.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = article
            form.save()
        return redirect('/')