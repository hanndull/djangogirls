from django.urls import path
from . import views 
# importing Django's function path and all of our views from the blog application

urlpatterns = [
    path('', views.post_list, name='post_list'), 
]

# assigning a view called post_list to the root URL, This pattern will tell 
# Django that views.post_list is the right place to go if someone enters your 
# website at the base address