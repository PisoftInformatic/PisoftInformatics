from django.db import models
from tinymce.models import HTMLField





'''
SOFTWARE DEVELOPMENT
'''
class Mobile_Applications(models.Model):
    heading = models.CharField(max_length=150)
    description = HTMLField()

    def __str__(self):
        return self.heading
    class Meta:
        verbose_name_plural = "Mobile Application"

class Web_Applications(models.Model):
    heading = models.CharField(max_length=150)
    description = HTMLField()

    def __str__(self):
        return self.heading
    class Meta:
        verbose_name_plural = "Web Application"

    
class Desktop_Applications(models.Model):
    heading = models.CharField(max_length=150)
    description = HTMLField()

    def __str__(self):
        return self.heading
    class Meta:
        verbose_name_plural = "Desktop Application"



