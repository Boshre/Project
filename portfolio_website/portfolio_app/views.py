from django.shortcuts import render,redirect

# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'portfoliomodule/index.html')
def projectslist(request):
     return render(request, 'portfoliomodule/projectslist.html')
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