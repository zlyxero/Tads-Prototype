from django.db import models

# Create your models here.

class Projects(models.Model):
	''' Project record(s) that includes project name, technology used and 
	cumulative profit'''

	project_name = models.CharField(max_length=150)
	project_technology = models.CharField(max_length=150)
	cumulative_profit = models.IntegerField()

	def __str__(self):
		return self.project_name

	class Meta:
		db_table = 'SAMPLE_PROJECTS'
		verbose_name = 'projects'
		verbose_name_plural = 'projects'	