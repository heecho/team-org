from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
	return HttpResponse('This is your home page')
	
def index(request):
	return HttpResponse('This is your index of projects')

def add_project(request):
	return HttpResponse('add project form')

def create_project(request):
	proj_info = {}
	proj_info['name'] = request.POST['name']
	proj_info['status'] = request.POST['status']
	proj_info['dev_type'] = request.POST['dev_type']
	proj_info['market'] = request.POST['market']
	proj_info['year'] = request.POST['fiscal_year']
	proj_info['decription'] = request.POST['description']
	proj_info['acquisition'] = request.POST['acquisition']
	proj_info['ee'] = request.POST['ee_days']
	proj_info['fw'] = request.POST['fw_days']
	proj_info['sw'] = request.POST['sw_days']
	proj_info['opt'] = request.POST['opt_days']
	proj_info['des'] = request.POST['des_days']
	return HttpResponse('this is your new project')
