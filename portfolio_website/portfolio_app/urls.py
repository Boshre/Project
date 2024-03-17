from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/',views.projectslist,name="projects"),
    path('contact/',views.contactMe,name="contactMe"),
    path('project/<int:project_id>/', views.project, name='project')
 ]