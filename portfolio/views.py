from django.shortcuts import render,get_object_or_404
from .models import Project
def home(request):
 return render(request,'portfolio/home.html',{'projects':Project.objects.filter(featured=True)})
def project_detail(request,slug):
 return render(request,'portfolio/project_detail.html',{'project':get_object_or_404(Project,slug=slug)})
