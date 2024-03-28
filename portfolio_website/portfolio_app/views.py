from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
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

        if title_search:
            projects = projects.filter(title__icontains=title_search)

        if tech_search:
            query = None
            for tech in tech_search:
                if query is None:
                    query = projects.filter(technologies__icontains=tech)
                else:
                    query = query | projects.filter(technologies__icontains=tech)
            projects = query

    return render(request, 'portfoliomodule/projectslist.html', {'projects': projects})
