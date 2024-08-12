from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import CreateGroupForm, CreatePostForm
from .models import Group, GroupPosts


class ListGroups(ListView):
    model = Group
    context_object_name = 'group'
    template_name = 'groups/GroupList.html'
    paginate_by = 5

    extra_context = {
        'title': 'List Groups'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creation_url'] = reverse_lazy('create_group')
        return context


class CreateGroup(LoginRequiredMixin, CreateView):
    form_class = CreateGroupForm
    context_object_name = 'form'
    template_name = 'groups/create_group.html'
    success_url = reverse_lazy('groups')

    extra_context = {
        'title': 'Create Group'
    }

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

class GroupWall(ListView):
    model = Group
    template_name = 'groups/group_wall.html'
    paginate_by = 5
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs.get('slug')
        context['creation_url'] = reverse_lazy('create_post', kwargs = {'slug': self.kwargs.get('slug')})
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST' and not request.user.is_authenticated:
            return redirect('login') 
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return GroupPosts.objects.filter(post__group_slug = self.kwargs.get('slug'))

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('likes')
        if post_id:
            user = request.user
            post_instance = get_object_or_404(GroupPosts, pk=post_id)

            if user in post_instance.likes.all():
                post_instance.likes.remove(user)
            else:
                post_instance.likes.add(user)

        return self.get(request, *args, **kwargs)
                


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'groups/create_post.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{Group.objects.get(group_slug = self.kwargs.get("slug")).group_name}: Create Post'
        return context

    def form_valid(self, form):
        form.instance.post = Group.objects.get(group_slug = self.kwargs.get('slug'))
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('group_wall', kwargs = {'slug': self.kwargs.get('slug')})