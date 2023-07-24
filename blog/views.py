from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from .forms import PostCreatForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    post = Post.objects.all()
    paginator = Paginator(post, 9)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {
        "title": "Home",
        'posts': post,
        'page':page
    }
    return render(request, 'blog/home.html', context ) 


def about(request):
    context = {
        "title": "about",
    }
    return render(request, 'blog/about.html', context )


def contact(request):
    context = {
        "title": "contact",
    }
    return render(request, 'blog/contact.html', context )  


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment.all()
    
    
    # paginator comment
    paginator = Paginator(comments, 4)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    # end paginator comment    
    
    
    
    if request.method == 'POST':
        user = request.user

        body = request.POST.get('body')

        comment = Comment(name=user, post=post, body=body)

        comment.save()

        return redirect('detail',post_id)
    
    
    context = {
        'title':post,
        'post': post,
        'comments':post.comment.all(),
        'page':page
    }
    return render(request, 'blog/post_detail.html', context )


@login_required(login_url='login')
def meep_like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            
        # return redirect("detail", post_id=post.id)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, ("You must be logged in to like ...."))
        redirect("detail")
        
        
        
def search(request):
    if request.method == 'POST':
        
        search = request.POST['search']
        
        searched_content = Post.objects.filter(content__contains = search)
        searched_title = Post.objects.filter(title__contains = search)
        # searched_author = Post.objects.filter(author__contains = search)
        
        serch_by = searched_content or searched_title 
        return render(request, 'blog/search.html', {'search':search, 'searched':serch_by})
    else:
        post = Post.objects.all()
        return render(request, 'blog/search.html', {'posts':post})
        
        
def error_404(request, exception):
    return render(request , 'blog/error404.html')




class PostCreatView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'content', 'image']
    template_name = 'blog/new_post.html'
    form_class = PostCreatForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    # context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data here
        context['title'] = 'Create New Post'
        return context




class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = PostCreatForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

    # context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data here
        context['title'] = 'Edit Post'
        return context
    



class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

    
    