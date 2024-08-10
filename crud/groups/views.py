from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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

    def get_queryset(self):
        return GroupPosts.objects.filter(post__group_slug = self.kwargs.get('slug'))


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