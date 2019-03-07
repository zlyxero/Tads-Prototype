from django.shortcuts import render, redirect
from .forms import ProjectsForm
from django.views import View

# Create your views here.

def analytics(request):
	''' display Power BI Embeded report '''
	return render(request, 'tads_simulator/analytics.html', {'page_title': 'Sample Analytics'})

class AddProject(View):
	''' display a form to add a new project'''

	def get(self, request):
		form = 	ProjectsForm()

		return render(request, 'tads_simulator/projectsForm.html', {'form':form, 'page_title': 'Submit Project'})

	def post(self, request):
		
		form = ProjectsForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('analytics')

		else:
			return render(request, 'tads_simulator/projectsForm.html', {'form':form, 'page_title': 'Submit Project'})





