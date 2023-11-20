from django.db import models
from tinymce.models import HTMLField




class Homepage_Recent_project_data(models.Model):
    project_name = models.CharField( max_length=50, help_text="Make Sure Project name is less than 50 chars")
    project_link = models.CharField(max_length=250, help_text="Make Sure your link start only with 'www' only and if your link chars>250 shorten url please")
    project_image = models.ImageField(upload_to='portfolio/display/')


    def __str__(self):
        return self.project_name
    
    class Meta: 
        verbose_name_plural = 'Recent Project of Home Page'





'''
portfolio
'''

class Portfolio(models.Model):
    project_name = models.CharField(max_length=50, help_text="Enter Your Project Name ex. PisotInformatics")
    project_link = models.CharField(max_length=250, help_text="Enter domain name of Your Project. ex - www.xyz.com", null=True, blank=True)
    device = models.CharField(max_length=50, help_text="Only Choose one --> Mobile, Web or Desktop")
    project_image = models.ImageField( upload_to='portfolio/')

    def __str__(self) :
        return self.project_name or self.project_name


'''
GALLERY
'''

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    class Meta: 
        verbose_name = 'Gallery Image'