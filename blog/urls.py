from django.urls import path
from . import views 
# importing Django's function path and all of our views from the blog application

urlpatterns = [
    path('', views.post_list, name='post_list'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

# assigning a view called post_list to the root URL, This pattern will tell 
# Django that views.post_list is the right place to go if someone enters your 
# website at the base address