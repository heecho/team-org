import requests
from django.contrib.auth.models import User
from projects.models import Department, Project
from django.utils import timezone


def create_department(name, capacity):
	dept = Department()
	dept.name = name
	#capacity = headcount*19.6(working days per month)*12 months
	dept.capacity = capacity
	dept.save()

def check_existing_dept(name, capacity):
	existing = Department.objects.all()
	if not existing.filter(name = name).exists():
		create_department(name, capacity)
	else:
		dept = Department.objects.get(name = name)

def create_project(proj_info):
	p = Project()
	p.name = proj_info['name']
	p.status = 	proj_info['status']
	p.dev_type = proj_info['dev_type']
	p.market = proj_info['market']
	p.fiscal_year = proj_info['year']
	p.description = proj_info['decription']
	p.acquisition = proj_info['acquisition']
	p.ee_days = proj_info['ee']
	p.fw_days = proj_info['fw']
	p.sw_days = proj_info['sw']
	p.optic_days = proj_info['opt'] 
	p.design_days = proj_info['des']
	p.save()
	p.departments = 

