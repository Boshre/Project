from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/',views.projectslist,name="projects"),
    path('contact/',views.contactMe,name="contactMe"),
    path('project/<int:project_id>/', views.project, name='project'),
    path('filter_projects', views.filter_projects, name='filter_projects'),
        path('add_project/', views.add_project, name='add_project'),
        path('update_project/<int:project_id>', views.update_project, name='update_project'),
        path('delete_project/<int:project_id>', views.delete_project, name='delete_project'),


 ]