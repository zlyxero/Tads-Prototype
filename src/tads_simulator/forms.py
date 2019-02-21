from django.forms import ModelForm
from .models import Projects

class ProjectsForm(ModelForm):
	''' form for adding a new project '''

	class Meta:
		model = Projects
		fields = ['project_name', 'project_technology', 'cumulative_profit']


		
