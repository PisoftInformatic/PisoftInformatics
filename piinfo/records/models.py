from django.db import models

# Create your models here.

class HEnquiry(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField( max_length=254)
    intrested_in = models.CharField(max_length=70)
    education = models.CharField(max_length=100)
    college = models.CharField( max_length=250)

    def __str__(self):
        return self.name or self.email




class Apply_Job(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254) 
    position_applied_for = models.CharField(max_length=100)
    qualification = models.CharField(max_length=90)
    address = models.TextField()
    remarks = models.TextField(  )
    skills = models.TextField()
    gender = models.CharField(max_length=10)
    experience = models.CharField(max_length=100)

    resume = models.FileField( upload_to='career_and_intern/apply_job/resumes')

    def __str__(self):
        return self.full_name or self.email or self.phone_number
    class Meta:
        verbose_name_plural = "Apply Job"

class Contact_data(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    phone = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name or self.email
    class Meta:
        verbose_name_plural = "Contact form Data"
    

class Registration(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    caddress = models.CharField(max_length=50, null=True, blank=True)
    module = models.CharField(max_length=50)
    pursuing_details = models.CharField(max_length=50)
    training_program = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.name or self.email
    class Meta:
        verbose_name_plural = "Registrations"


class Users(models.Model):
    # id = models.IntegerField()
    name = models.CharField( max_length=50)
    mobileno = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'users'
        db_table = 'users'




class modules(models.Model):
    module_name = models.CharField(max_length=50)
    module_price = models.IntegerField()

    def __str__(self):
        return self.module_name

    class Meta:
        verbose_name_plural = 'Modules'
        db_table = 'modules'
