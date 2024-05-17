from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from functools import reduce


from .models import Project

# Create your views here.
def index(request):
    return render(request, 'portfoliomodule/index.html')

def projectslist(request):
    projects = Project.objects.all()
    return render(request, 'portfoliomodule/projectslist.html', {'projects': projects})

def project(request, project_id):
    try:
        targetProject = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return redirect('projectslist')

    context = {'project': targetProject}
    return render(request, 'portfoliomodule/project.html', context)

def contactMe(request):
     return render(request, 'portfoliomodule/contactMe.html')


@csrf_exempt
def filter_projects(request):
    projects = Project.objects.all()

    if request.method == "POST":
        title_search = request.POST.get('title_search', '')
        tech_search = request.POST.getlist('tech')

        queries = []  # List to store individual Q objects

        if title_search:
            queries.append(Q(title__icontains=title_search))

        if tech_search:
            tech_queries = [Q(technologies__icontains=tech) for tech in tech_search]
            queries.append(Q(reduce(lambda x, y: x | y, tech_queries)))

        if queries:
            query = reduce(lambda x, y: x & y, queries)
            projects = projects.filter(query)

    return render(request, 'portfoliomodule/projectslist.html', {'projects': projects})

from .forms import ProjectForm

@csrf_exempt
def add_project(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'portfoliomodule/projectslist.html', {'projects': projects})
    else:
        form = ProjectForm()
    return render(request, 'portfoliomodule/add_project.html', {'form': form})
    

@csrf_exempt
def update_project(request, project_id):
    projects = Project.objects.all()
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return render(request, 'portfoliomodule/projectslist.html', {'projects': projects})
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfoliomodule/update_project.html', {'form': form})

def delete_project(request, project_id):
    projects = Project.objects.all()
    project = Project.objects.get(id=project_id)
    project.delete()
    return render(request, 'portfoliomodule/projectslist.html', {'projects': projects})
