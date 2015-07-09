from django.db import models
from django.contrib.auth.models import User
#from django.forms import ModelForm

# Create your models here.

STATUS = (('PREGATE', 'Pre-Gate'), ('GATE1', 'Gate 1'), ('GATE2', 'Gate 2'), ('GATE3', 'Gate 3'), ('GATE4', 'Gate 4'), ('CLOSED', 'Launched'),)
DEV_TYPE = (('NPI', 'New Product Introdcution'), ('PI', 'Product Improvement'), ('SUPPORT', 'Support'), ('SPL', 'SPL'), ('OTHER', 'Other'),)
MARKET = (('OUTDOOR', 'Outdoor'), ('INDOOR', 'Indoor'), ('CONTROLS', 'Controls'), ('LUMENAREA', 'Lumenarea'), ('LUMENALPHA', 'Lumenalpha'),)

class Department(models.Model):
	name = models.CharField(max_length=200)
	capacity = models.IntegerField(blank=True)
	
	def __str__(self):
		return self.name

class Project(models.Model):
	departments = models.ManyToManyField(Department, through = 'Dept_Hours')
	name = models.CharField(max_length=200)
	status = models.CharField(max_length=200, choices = STATUS)
	dev_type = models.CharField(max_length=200, choices = DEV_TYPE)
	market = models.CharField(max_length=200, choices = MARKET)
	fiscal_year = models.CharField(max_length=4, blank=True)
	description = models.TextField(blank=True)
	pubdate = models.DateField(auto_now_add=True)
	acquisition = models.BooleanField()
	fast_track = models.BooleanField()
	
	def __str__(self):
		return self.name

class Dept_Hours(models.Model):
	department = models.ForeignKey(Department)
	project = models.ForeignKey(Project)
	hours = models.IntegerField(blank=True)

# class ProjectForm(ModelForm):
# 	class Meta:
# 		model = Project
# 		fields = ['name', 'status', 'dev_type', 'market', 'departments', 'fiscal_year', 'description','acquisition', 'fast_track']


	# ee_days = models.IntegerField(blank=True)
	# fw_days = models.IntegerField(blank=True)
	# sw_days = models.IntegerField(blank=True)
	# optic_days = models.IntegerField(blank=True)
	# design_days = models.IntegerField(blank=True)


'''BEGIN;
CREATE TABLE "projects_department" ("id" integer NOT NULL PRIMARY KEY AUTOINCREM
ENT, "name" varchar(200) NOT NULL, "capacity" integer NOT NULL);
CREATE TABLE "projects_dept_hours" ("id" integer NOT NULL PRIMARY KEY AUTOINCREM
ENT, "hours" integer NOT NULL, "department_id" integer NOT NULL REFERENCES "proj
ects_department" ("id"));
CREATE TABLE "projects_project" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT
, "name" varchar(200) NOT NULL, "status" varchar(200) NOT NULL, "dev_type" varch
ar(200) NOT NULL, "market" varchar(200) NOT NULL, "fiscal_year" varchar(4) NOT N
ULL, "description" text NOT NULL, "pubdate" date NOT NULL, "acquisition" bool NO
T NULL, "fast_track" bool NOT NULL);
CREATE TABLE "projects_dept_hours__new" ("id" integer NOT NULL PRIMARY KEY AUTOI
NCREMENT, "hours" integer NOT NULL, "department_id" integer NOT NULL REFERENCES
"projects_department" ("id"), "project_id" integer NOT NULL REFERENCES "projects
_project" ("id"));
INSERT INTO "projects_dept_hours__new" ("hours", "project_id", "id", "department
_id") SELECT "hours", NULL, "id", "department_id" FROM "projects_dept_hours";
DROP TABLE "projects_dept_hours";
ALTER TABLE "projects_dept_hours__new" RENAME TO "projects_dept_hours";
CREATE INDEX "projects_dept_hours_bf691be4" ON "projects_dept_hours" ("departmen
t_id");
CREATE INDEX "projects_dept_hours_b098ad43" ON "projects_dept_hours" ("project_i
d");

COMMIT;'''