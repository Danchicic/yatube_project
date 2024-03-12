from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView
from django.urls import reverse

from .models import Post, Group, User
from django.core.mail import send_mail


# Create your views here.

def index(request):
    template = "posts/index.html"

    posts = Post.objects.all().select_related()
    p = Paginator(posts, 10)
    page_number = request.GET.get('page')

    template_page = p.get_page(page_number)
    context = {
        'title': "Это главная страница проекта Yatube",
        'page_obj': template_page,

    }
    return render(request, template, context)


def group_posts(request, group_name):
    template = "posts/group_list.html"
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
        'group_name': group_name
    }
    group = get_object_or_404(Group, address=group_name)
    posts = Post.objects.filter(group__address=group_name)
    context['posts'] = posts
    return render(request, template, context)


def profile(request, username):
    username = User.objects.get(username=username)
    con = Post.objects.select_related().filter(author=username)
    p = Paginator(con, 5)
    page = request.GET.get('page')
    context = {'name': username.get_full_name(),
               "page_obj": p.get_page(page),
               "posts_count": con.count(),
               }

    return render(request, template_name='posts/profile.html', context=context)


def post_detail(request, post_id):
    # get user post
    post = Post.objects.select_related("group").get(id=post_id)
    # get instance of user who writes the post
    post_user = User.objects.get(id=post.author_id)
    # join with users and get post's count of this user
    post_count = Post.objects.select_related().filter(author=post_user).count()
    is_author = Post.objects.get(id=post_id, author_id=post.author_id)
    context = {"post": post, "post_count": post_count, "is_author": is_author}

    return render(request, template_name='posts/post_detail.html', context=context)


class CreatePostView(CreateView):
    model = Post
    fields = ("text", "group")
    successful_url = "post:profile"
    template_name = "posts/create_post.html"

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(self.successful_url, kwargs={'username': self.object.author.username})


class EditPostView(UpdateView):
    model = Post
    fields = ["text", "group"]
    template_name = "posts/create_post.html"

    def get(self, request, **kwargs):
        post_id = int(kwargs.get("post_id"))
        post = get_object_or_404(Post, id=post_id)
        if self.request.user.id == post.author_id:
            return render(request, self.template_name, {"form": {
                "group": str(post.group),
                "text": post.text,
            },
                "is_edit": 1
            })
        return redirect("post:post_detail", post_id)
