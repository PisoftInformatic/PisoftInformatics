from django.db import models
from tinymce.models import HTMLField

'''

CAREER AND INTERNSHIP

'''

class Tech_Descovery(models.Model):
    heading = models.CharField(max_length=150)
    description = HTMLField()
    class Meta:
        verbose_name_plural = "Tech Discovery"


class Six_Weeks_Intern(models.Model):
    heading = models.CharField(max_length=150)
    description = HTMLField()
    class Meta:
        verbose_name_plural = "Six weeks internship"

class Hope_Program(models.Model):
    heading = models.CharField(max_length=150)
    description = HTMLField()
    class Meta:
        verbose_name_plural = "Hop Program"

class Career_With_Us(models.Model):
    job_title = models.CharField(max_length=30)
    job_profile = models.CharField(max_length=30)
    job_description =HTMLField()
    experience_required_in_years= models.CharField(max_length=30)
    city_location = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Career With Us"

class Traniee_with_us(models.Model):
    trainee_name = models.CharField(max_length=50)
    trainee_placed_company = models.CharField(max_length=100)
    trainee_image = models.ImageField( upload_to='career_and_intern/trainee_with_us')
    class Meta:
        verbose_name_plural = "Trainee With us"
