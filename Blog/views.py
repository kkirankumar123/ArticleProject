from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from Blog.models import POST
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView)
from django.contrib.auth.mixins import (LoginRequiredMixin,UserPassesTestMixin)\

from django.core.exceptions import PermissionDenied

from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse


# Create your views here.

"""
def home(request):
    articles = POST.objects.all()
    context = {
        "posts": articles
    }
    return render(request, 'blog/home.html', context)
"""


@login_required()
def about(request):
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = POST
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["date_posted"]




class PostDetailView(DetailView):
    model = POST
    template_name = "blog/post_detail.html"
    context_object_name = "object"

class PostCreateView(CreateView):
    model = POST
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    context_object_name = "form"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = POST
    fields = ["title","content"]
    template_name = "blog/post_form.html"
    context_object_name = "form"
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # read the current object which we want to update
        post = self.get_object()

        # validate who send request and who created object
        if self.request.user ==  post.author:
            return True
        return False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
        )



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = POST
    success_url = '/'
    template_name = "blog/post_cofirm_delete.html"
    context_object_name = "object"
    login_url = 'login'

    def test_func(self):
        # read the current object which we want to update
        post = self.get_object()

        # validate who send request and who created object
        if self.request.user ==  post.author:
            return True
        return False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
        )


class UserPostListView(ListView):
    model = POST  #  Post.objects.all()
    template_name = "blog/user_posts.html"
    context_object_name = "posts"  #  [ ] |  [{k:v,...},{},{},..]
    # ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return POST.objects.filter(author=user).order_by("-date_posted")

def responsive_view(request):
    return render(request,'blog/responsive.html')

def djangoview(request):
    if request.method == 'GET':
        return render(request,'Blog/djangoques.html')


def pythonview(request):
    if request.method == 'GET':
        return render(request,'Blog/pythonques.html')










