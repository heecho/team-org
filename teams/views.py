from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from projects.models import Project, Department
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	teams = Department.objects.all()
	return render(request, 'teams/home.html', {'teams':teams})
	#return HttpResponse('This is your index of departments')

def new(request):
	return render(request, 'teams/new.html', {})

def create(request):
	d = Department()
	d.name = request.POST['name']
	d.capacity = float(request.POST['capacity'])*19.6*12*8
	d.save()
	dept_id = d.id
	return HttpResponseRedirect(reverse('teams:show', args = (dept_id,)))

def show(request, dept_id):
	team = Department.objects.get(pk=dept_id)
	headcount = round(team.capacity/(19.6*12*8)*2)/2
	project_list = team.project_set.all().order_by('-id')
	return render(request, 'teams/show.html', {'team': team, 'projects':project_list, 'headcount':headcount})