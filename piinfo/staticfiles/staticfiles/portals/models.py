from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Elive_today(models.Model):
    title_of_this_page = models.CharField( max_length=200)
    page_description = HTMLField()
    website_domain_link = models.CharField(max_length=150, blank=True, null=True)
    class Meta: 
        # verbose_name = 'Elive Today'
        verbose_name_plural = 'Elive Today'

class Chandigarh_web(models.Model):
    title_of_this_page = models.CharField( max_length=200)
    page_description = HTMLField()
    website_domain_link = models.CharField(max_length=150, blank=True, null=True)
    class Meta: 
        verbose_name_plural = 'Chandigarh Web'

class Class_ikart(models.Model):
    title_of_this_page = models.CharField( max_length=200)
    page_description = HTMLField()
    website_domain_link = models.CharField(max_length=150, blank=True, null=True)

    class Meta: 
        verbose_name_plural = 'Class ikart'
