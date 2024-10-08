from django.urls import path
from django.conf.urls.static import static
from crud import settings
from . import views


urlpatterns = [
    # path('group/<slug:slug>/', views.Group.as_view(), name = 'group')
    path('', views.ListGroups.as_view(), name = 'groups'),
    path('create_group/', views.CreateGroup.as_view(), name = 'create_group'),
    path('<slug:slug>/', views.GroupWall.as_view(), name = 'group_wall'),
    path('<slug:slug>/edit/', views.GroupEdit.as_view(), name = 'group_edit'),
    path('<slug:slug>/create_post/', views.CreatePost.as_view(), name = 'create_post'),
    path('<slug:slug_group>/<slug:slug_post>/edit/', views.EditPost.as_view(), name = 'edit_post')
]