from django.db import models

from django.contrib.auth import get_user_model
user = get_user_model()

# Create your models here.

class student(models.Model):
	statuschoices = (
    ("draft", "DRAFT"),
    ("published", "PUBLISHED"),


)
	title = models.CharField(max_length=50)
	email = models.EmailField(max_length=30, default='krbaidik0@gmail.com')
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(user, on_delete= models.CASCADE, default=1 )
	content = models. TextField(max_length=300, null=True)
	slug = models.SlugField(unique=True, null=True)
	image = models.ImageField(null=True, blank=True)
	status = models.CharField(choices= statuschoices, max_length=100, default= 'none')



	def __str__(self):
   		return self.title

