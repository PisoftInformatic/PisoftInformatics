from django.db import models
from tinymce.models import HTMLField
# Create your models here.


'''

WEB SERVICES

'''
class Web_Services_Header(models.Model):
    Graphic_Design_Heading = models.CharField(max_length=150)
    Graphic_Design_Description = HTMLField()


    Web_Design_Heading = models.CharField(max_length=150)
    Web_Design_Description = HTMLField()
    
    
    Domain_Register_Heading = models.CharField(max_length=150)
    Domain_Register_Description = HTMLField()
    
    
    Web_Hosting_Heading = models.CharField(max_length=150)
    Web_Hosting_Description = HTMLField()
    
    
    Web_Marketing_Heading = models.CharField(max_length=150)
    Web_Marketing_Description = HTMLField()




class Graphic_Design_Card(models.Model):
    heading = models.CharField(max_length=150, help_text='<150 Chars', null=True, blank=True, default='')
    sub_heading = models.CharField(max_length=100, null=True, blank=True, default='')
    description = HTMLField(null=True, blank=True, default='')
    def __str__(self):
        return self.heading or self.sub_heading

class Web_Design_Card(models.Model):
    heading = models.CharField(max_length=150, help_text='<150 Chars', null=True, blank=True, default='')
    sub_heading = models.CharField(max_length=100, null=True, blank=True, default='')
    description = HTMLField(null=True, blank=True, default='')
    def __str__(self):
        return self.heading or self.sub_heading

    
class Domain_Registration_Card(models.Model):
    heading = models.CharField(max_length=150, help_text='<150 Chars', blank=True, default='')
    sub_heading = models.CharField(max_length=100, blank=True, default='')
    description = HTMLField( blank=True, default='')
    def __str__(self):
        return self.heading or self.sub_heading



class Web_Marketing_Card(models.Model):
    heading = models.CharField(max_length=150, help_text='<150 Chars', null=True, blank=True, default='')
    sub_heading = models.CharField(max_length=100, null=True, blank=True, default='')
    description = HTMLField(null=True, blank=True, default='')
    def __str__(self):
        return self.heading or self.sub_heading




class Web_Hosting_Card(models.Model):
    heading = models.CharField(max_length=150, help_text='<150 Chars', null=True, blank=True, default='')
    sub_heading = models.CharField(max_length=100, null=True, blank=True, default='')
    description = HTMLField(null=True, blank=True, default='')
    def __str__(self):
        return self.heading or self.sub_heading
