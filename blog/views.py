from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


# def post_list_views(request):
#     post_list = Post.objects.filter(status="pub").order_by('-date_time_modified')
#     return render(request, 'blog/post_list.html', {'post_list': post_list})


class PostListViews(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-date_time_modified')


# def post_detail_views(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

#
# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#                                         # before use the form
#                                         # post_title = request.POST.get('title')
#                                         # post_text = request.POST.get('text')
#                                         # user = User.objects.all()[0]
#                                         # Post.objects.create(title=post_title, text=post_text, author=user, status='pub', )
#         else:  # Get request
#             form = PostForm()
#
#     return render(request, 'blog/post_create.html', context={'form': form})


class PostCreate(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#     return render(request, 'blog/post_create.html', context={'form': form})
class PostUpdate(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
#
# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})

class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

