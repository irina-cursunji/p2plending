
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm

def project_confirmation(request):
    return render(request, 'projects/project_confirmation.html')

def project_list(request):
    projects = Project.objects.filter(is_approved=True)
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.borrower = request.user
            project.is_approved = False  # Set to False until approved
            project.save()
            return redirect('projects:project_confirmation')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    # Optionally restrict editing based on approval status
    if not project.is_approved and project.borrower != request.user:
        return HttpResponseForbidden("You cannot edit this project.")
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:project_confirmation')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'projects/project_form.html', {'form': form})
