from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model

class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_slug = models.SlugField(max_length=100, unique = True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = 'creator', null = False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    

    def get_absolute_url(self):
        return reverse('group_wall', kwargs={'slug': self.group_slug})
    
    def __repr__(self):
        return f'{self.group_name}{self.pk}'

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
        if not self.group_slug:
            self.group_slug = slugify(self.group_name)
        super().save(*args, **kwargs)


class GroupPosts(models.Model):
    post = models.ForeignKey('Group', on_delete=models.CASCADE, related_name = 'group', null=True)
    text = models.TextField()
    post_slug = models.SlugField(unique=True)
    file = models.ImageField(upload_to='post/', blank = True, null = True, default = None)
    time_created = models.DateTimeField(auto_now_add = True)
    time_updated = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = 'postCreator', null = True)
    # post = models.ForeignKey('Group', on_delete=models.CASCADE, related_name = 'group')
    # tag = models.ManyToManyField('Tag'related_name = 'tag')

    def get_absolute_url(self):
        return reverse('groups', kwargs={'slug': self.post_slug})

    def save(self, *args, **kwargs):
        if not self.post_slug:
            self.post_slug = slugify(self.text[:15])
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-time_created']
