from django.urls import path
from . import views 

urlpatterns = [
    path('projects', views.project_list, name='project_list'), 
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/drafts/', views.project_draft_list, name='project_draft_list'),
    path('project/<pk>/publish/', views.project_publish, name='project_publish'),
    path('project/<pk>/remove', views.project_remove, name='project_remove'),
]

    #path('projects', views.post_list, name='post_list'), 