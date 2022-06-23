from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from accounts.models import Account
from home.models import HomeArticleModel, HomeCarouselModel, ReviewsModel
from home.forms import CreateHomeForm, ReviewsFrom, HomeDeleteForm


#
# class HomeView(ListView):
#     model = HomeArticleModel
#     template_name = "home.html"
#     context_object_name = 'home_post'

#
@login_required
def home_list(request):
    context = {}
    user = request.user
    count = Account.objects.filter(id=user.id)
    home1 = HomeArticleModel.objects.filter(id=user.id)

    home = HomeCarouselModel.objects.all()

    data = HomeArticleModel.objects.filter(author=user.id)
    paginator = Paginator(data, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'count': count,
        'home_post': home1,
        'home_blog': home,
        'page_obj': page_obj
    }
    return render(request, "home.html", context)


def paginate(request):

    contact_list = HomeArticleModel.objects.all()
    paginator = Paginator(contact_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'paginate.html',context)



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
            return redirect("home")
        # messages.success(request, f'Ссылка добавлена')
    else:
        instance = CreateHomeForm()

    return render(request, 'CRUD/create.html', {'form': instance})


def detail_home_view(request, pk):
    blog_post = get_object_or_404(HomeArticleModel, pk=pk)
    comments = ReviewsModel.objects.filter(article_id=pk)

    if request.method == 'POST':
        form = ReviewsFrom(data=request.POST)
        user = request.user

        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = blog_post
            obj.author = user
            obj.save()
            # return redirect('detail_home_view', pk=blog_post.pk)
            return redirect(f'{request.path}')


    else:
        form = ReviewsFrom()
    context = {
        'blog_post': blog_post,
        'comments': comments
    }

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
    if home_post.author != user:
        return HttpResponse('NOT REGISTOR')

    if request.POST:
        form = CreateHomeForm(request.POST or None, request.FILES or None, instance=home_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
            return redirect("home")
    form = CreateHomeForm(
        initial={
            'title': home_post.title,
            'body': home_post.body,
            'image': home_post.image,
        }
    )

    context['form'] = form
    return render(request, 'CRUD/update.html', context)


def delete_home_view(request, pk):
    context = {}


    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:login')

    home_blog = get_object_or_404(HomeArticleModel, pk=pk)
    if home_blog.author != user:
        return HttpResponse('NOT REGISTOR')

    if request.POST:
        form = HomeDeleteForm(request.POST or None, request.FILES or None, instance=home_blog)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.delete()
            context['success_message'] = "Delete"
            return redirect("home")
    form = HomeDeleteForm(
        initial={
            'title': home_blog.title,
            'body': home_blog.body,
            'image': home_blog.image,
        }
    )

    context['form'] = form
    return render(request, "CRUD/delete.html", context)






# class AddReview(View):


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


    # def post(self, request, pk):
    #     form = ReviewsFrom(request.POST)
    #     article = HomeArticleModel.objects.get(pk=pk)
    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.article = article
    #         form.save()
    #     return redirect('/')


