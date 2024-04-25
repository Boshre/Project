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

@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        Project.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            technologies=request.POST['technologies'],
            link=request.POST.get('link', '')  
        )
        return redirect('projects')
    return render(request, 'portfoliomodule/add_project.html')
