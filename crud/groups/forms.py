from django import forms
from .models import Group, GroupPosts

class CreateGroupForm(forms.ModelForm):
    group_name = forms.CharField(label = '', widget = forms.TextInput(attrs = {'placeholder': 'enter group name'}))
    group_slug = forms.SlugField(label='', required=False , widget=forms.TextInput(attrs = {'placeholder': 'you may change basic slug'}))
    class Meta:
        model = Group
        fields = ['group_name', 'group_slug']


class CreatePostForm(forms.ModelForm):
    text = forms.CharField(label = '', widget = forms.Textarea(attrs = {'placeholder': 'enter text of your post', 'cols': 50, 'rows': 5, 'style': 'resize: none;'}))
    class Meta:
        model = GroupPosts
        fields = ['text']