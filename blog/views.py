from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
#Note: we use decorators for function based views and mixins for class based views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#For displaying the list, details in the page
#Django uses specific classes to perform those actions
from django.views.generic import (
     ListView,
     DetailView,
     CreateView,
     UpdateView,
     DeleteView
)

def home(request):
    # context = {
    #     'posts':Post.objects.all()
    # }
    #render function returns the  HttpResponse
    #render(request,what should be linked, context (ie, the data to be displayed. Can be optional))
    return render(request,'blog/home.html')

def blog(request):
    context = {
        'posts':Post.objects.all()
    }
    #render function returns the  HttpResponse
    #render(request,what should be linked, context (ie, the data to be displayed. Can be optional))
    return render(request,'blog/blog.html',context)


class PostListView(ListView):
    model = Post
    #Default template is: appName/ModelName_viewType.html ie, blog/post_list.html
    template_name = 'blog/blog.html'
    #By default the listView calls the list as Object List but since we called it post in the home function
    #we are going to use that
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    #Default template is: appName/ModelName_viewType.html ie, blog/post_list.html
    template_name = 'blog/user_posts.html'
    #By default the listView calls the list as Object List but since we called it post in the home function
    #we are going to use that
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    #The default template_name in this case will be: blog/post_detail.html
    model = Post

#For instance, here mixin is used for redirecting the user to login page if they want to write post without login
#Just like decorators in function
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# only the user who wrote the post can update that specific post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request,'blog/about.html',{'title':'About'})


def packagelist(request):
    return render(request, 'blog/packagelist.html',{'title': 'Packages'})

def contactus(request):
    return render(request,'blog/contact.html',{'title':'Contact Us'})
