from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from projects.models import Department, Project, Dept_Hours
from django.core.urlresolvers import reverse
#from django.forms import ModelForm


# Create your views here.
def main(request):
	return HttpResponse('This is your home page')

def index(request):
	return HttpResponse('This is your index of projects')

def new(request):
	teams = Department.objects.all()
	return render(request, 'projects/new.html', {'teams': teams})

def create(request):
	p = Project()
	p.name = request.POST['name']
	p.status = request.POST['status']
	p.market = request.POST['market']
	p.dev_type = request.POST['dev_type']
	p.fiscal_year = request.POST['year']
	if request.POST['fast'] == 'on':
		p.fast_track = True
	else:
		p.fast_track = False
	if request.POST['acquisition']=='on':
		p.acquisition = True
	else:
		p.acquisition = False
	print p.fast_track
	print p.acquisition
	p.description = request.POST['description']
	p.save()
	teams = dict(request.POST)['teams']
	for x in teams:
		d=Department.objects.get(pk=x)
		dH = Dept_Hours(department = d, project=p)
		dH.save()
	#return HttpResponse('add time here')
	return HttpResponseRedirect(reverse('projects:add',args = (p.id,)))

# def new(request):
# 	p = ProjectForm()
# 	#teams = Department.objects.all()
#  	return render(request, 'projects/new2.html', {'form': p})


# def create(request):
# 	proj = ProjectForm(request.POST)
# 	new_proj = proj.save(commit=False)
# 	new_proj.save()
# 	teams = dict(request.POST)['departments']
# 	print teams
# 	p = Project.objects.get(pk=new_proj.id)
# 	for team in teams:
# 		d = Department.objects.get(pk=team)
# 		dh = Dept_Hours(department = d, project = p)
# 		dh.hours = 0
# 		dh.save()

# 	#proj.save_m2m()
# 	return HttpResponseRedirect(reverse('projects:add',args = (new_proj.id,)))

def add_time(request, proj_id):
	p = Project.objects.get(pk=proj_id)
	teams = p.departments.all()
	return render(request, 'projects/add.html', {'teams': teams, 'project':p})
	#return HttpResponse('add time here')

def assign(request, proj_id):
	dhs = Dept_Hours.objects.filter(project=proj_id)
	for dh in dhs:
		dh.hours = request.POST['hours']
		dh.save()
	return HttpResponseRedirect(reverse('projects:show', args = (proj_id,)))

def show(request, proj_id):
	return HttpResponse('show project')