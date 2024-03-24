from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'portfoliomodule/index.html')
def projectslist(request):
     return render(request, 'portfoliomodule/projectslist.html',{'projects':__getProjects()})
def project(request, project_id):
    
    # Static data for projects
    project1 = {'id': 1, 'title': 'Interactive Web Application', 'description': 'A dynamic web application that allows users to interact in real-time.', 'technologies': 'Django, JavaScript, WebSocket', 'link': '/project/1'}
    project2 = {'id': 2, 'title': 'Machine Learning Analysis', 'description': 'This project involves a machine learning algorithm for data analysis and prediction.', 'technologies': 'Python, Scikit-Learn, Pandas', 'link': '/project/2'}
    
    # Find the target project based on ID
    targetProject = None
    if project1['id'] == project_id: targetProject = project1
    if project2['id'] == project_id: targetProject = project2

    # Redirect to projects list if project not found
    if targetProject is None: return redirect('projects_list')
    
    # Pass the target project to the template
    context = {'project': targetProject}
    return render(request, 'portfoliomodule/project.html', context)

def contactMe(request):
     return render(request, 'portfoliomodule/contactMe.html')

def __getProjects():
    return [
        {'id': 1, 'title': 'Interactive Web Application', 'description': 'A dynamic web application that allows users to interact in real-time.', 'technologies': 'Django, JavaScript, WebSocket', 'link': '/project/1'},
        {'id': 2, 'title': 'Machine Learning Analysis', 'description': 'This project involves a machine learning algorithm for data analysis and prediction.', 'technologies': 'Python, Scikit-Learn, Pandas', 'link': '/project/2'},
        {'id': 3, 'title': 'Mobile App Development', 'description': 'A cross-platform mobile application developed using Flutter.', 'technologies': 'Flutter, Dart', 'link': '/project/3'},
        {'id': 4, 'title': 'Data Visualization Tool', 'description': 'A tool for visualizing complex datasets interactively.', 'technologies': 'React, D3.js', 'link': '/project/4'}
    ]

@csrf_exempt
def filter_projects(request):
    projects = __getProjects()
    if request.method == "POST":
        title_search = request.POST.get('title_search', '')
        tech_search = request.POST.getlist('tech')  

        if title_search:
            projects = [proj for proj in projects if title_search.lower() in proj['title'].lower()]

        if tech_search:
            projects = [proj for proj in projects if any(tech in proj['technologies'] for tech in tech_search)]

    return render(request, 'portfoliomodule/projectslist.html', {'projects': projects})

