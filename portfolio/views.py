from django.shortcuts import render, redirect, render, get_object_or_404
from django.utils import timezone
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


@login_required
def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
        
    else:
        form = ProjectForm()
    
    return render(request, 'project_edit.html', {'form': form})


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'project_edit.html', {'form': form})


@login_required
def project_draft_list(request):
    projects = Project.objects.filter(published_date__isnull=True).order_by('title')
    return render(request, 'project_draft_list.html', {'projects': projects})


@login_required
def project_publish(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.publish()
    return redirect('project_detail', pk=pk)


@login_required
def project_remove(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete() #every django model can be deleted w/ this method
    return redirect('project_list')