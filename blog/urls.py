from django.urls import path
from . import views
from .views import (
         PostListView,
         PostDetailView,
         PostCreateView,
         PostUpdateView,
         PostDeleteView,
         UserPostListView
)

urlpatterns = [
#path(path link, view to be displayed, name for the displayed view)
# path('',views.home,name ='blog-home'),
path('home/',views.home,name='home'),
path('',PostListView.as_view(), name='blog-myblog'),
path('user/<str:username>/',UserPostListView.as_view(),name='user-posts'),

path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),

path('post/new/',PostCreateView.as_view(),name='post-create'),
path('about/',views.about, name='blog-about'),
path('package/',views.packagelist, name='blog-package'),
path('contact/',views.contactus,name='blog-contact')
]
