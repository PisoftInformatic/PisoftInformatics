from django.db import models
from tinymce.models import HTMLField
# Create your models here.


'''

WEB SERVICES

'''
# class Web_Services_Header(models.Model):
#     Graphic_Design_Heading = models.CharField(max_length=150)
#     Graphic_Design_Description = HTMLField()


#     Web_Design_Heading = models.CharField(max_length=150)
#     Web_Design_Description = HTMLField()
    
    
#     Domain_Register_Heading = models.CharField(max_length=150)
#     Domain_Register_Description = HTMLField()
    
    
#     Web_Hosting_Heading = models.CharField(max_length=150)
#     Web_Hosting_Description = HTMLField()
    
    
#     Web_Marketing_Heading = models.CharField(max_length=150)
#     Web_Marketing_Description = HTMLField()




# class Graphic_Design_Card(models.Model):
#     heading = models.CharField(max_length=150, help_text='<150 Chars', null=True, blank=True, default='')
#     sub_heading = models.CharField(max_length=100, null=True, blank=True, default='')
#     description = HTMLField(null=True, blank=True, default='')
#     def __str__(self):
#         return self.heading or self.sub_heading

# class Web_Design_Card(models.Model):
#     heading = models.CharField(max_length=150, help_text='<150 Chars', null=True, blank=True, default='')
#     sub_heading = models.CharField(max_length=100, null=True, blank=True, default='')
#     description = HTMLField(null=True, blank=True, default='')
#     def __str__(self):
#         return self.heading or self.sub_heading

    
# class Domain_Registration_Card(models.Model):
#     heading = models.CharField(max_length=150, help_text='<150 Chars', blank=True, default='')
#     sub_heading = models.CharField(max_length=100, blank=True, default='')
#     description = HTMLField( blank=True, default='')
#     def __str__(self):
#         return self.heading or self.sub_heading



# class Web_Marketing_Card(models.Model):
#     heading = models.CharField(max_length=150, help_text='<150 Chars', null=True, blank=True, default='')
#     sub_heading = models.CharField(max_length=100, null=True, blank=True, default='')
#     description = HTMLField(null=True, blank=True, default='')
#     def __str__(self):
#         return self.heading or self.sub_heading




# class Web_Hosting_Card(models.Model):
#     heading = models.CharField(max_length=150, help_text='<150 Chars', null=True, blank=True, default='')
#     sub_heading = models.CharField(max_length=100, null=True, blank=True, default='')
#     description = HTMLField(null=True, blank=True, default='')
#     def __str__(self):
#         return self.heading or self.sub_heading
    


'''
Web Hosting New
'''

class Web_Hosting(models.Model):
    page_heading = models.CharField( max_length=50, help_text="Main Heading of the Page")
    page_description = models.TextField(help_text="Description of the page. ")
    # heading_for_box_section = HTMLField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Web Hosting'

class Web_Hosting_Box(models.Model):
    card = models.ForeignKey(Web_Hosting, default=None, on_delete=models.CASCADE)
    # box_image = models.FileField(upload_to='erp_solutions/images',blank=True, help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    package = models.CharField(max_length=50,blank=True,help_text="Enter your Package name eg. Platinum, Gold or Basic,Advanced")
    server = models.CharField(max_length=50,blank=True,help_text="Package offers Which Server eg.- linux,windows etc.")
    package_description = HTMLField(max_length=250,blank=True, help_text="more text may create problem in UI. ")
    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural= 'Web Hosting Features and Prices'
    
    
    


'''
Graphic Designing New
'''

class Graphic_Design(models.Model):
    page_heading = models.CharField( max_length=50, help_text="Main Heading of the Page")
    page_description = models.TextField(help_text="Description of the page. ")
    # heading_for_box_section = HTMLField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Graphic Design'

class Graphic_Design_Box(models.Model):
    card = models.ForeignKey(Graphic_Design, default=None, on_delete=models.CASCADE)
    # box_image = models.FileField(upload_to='erp_solutions/images',blank=True, help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    service = models.CharField(max_length=50,blank=True,help_text="Services tha you offers.. eg.- logo,stationary etc.")
    package = models.CharField(max_length=50,blank=True,help_text="Enter your Package name eg. Platinum, Gold or Basic,Advanced")
    package_description = HTMLField(max_length=250,blank=True, help_text="more text may create problem in UI. ")
    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural= 'Graphic Design Features and Prices'
    

'''
Web Designing New
'''

class Web_Design(models.Model):
    page_heading = models.CharField( max_length=50, help_text="Main Heading of the Page")
    page_description = models.TextField(help_text="Description of the page. ")
    # heading_for_box_section = HTMLField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Web Design'

class Web_Design_Box(models.Model):
    card = models.ForeignKey(Web_Design, default=None, on_delete=models.CASCADE)
    # box_image = models.FileField(upload_to='erp_solutions/images',blank=True, help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    package = models.CharField(max_length=50,blank=True,help_text="Enter your Package name eg. Platinum, Gold or Basic,Advanced")
    service = models.CharField(max_length=50,blank=True,help_text="Services tha you offers.. eg.- static, dynamic site, wordress etc.")
    package_description = HTMLField(max_length=350,blank=True, help_text="Note - Only up to 8 Points allowed    ")
    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural= 'Web Design Features and Prices'
    
    

'''
Web Marketing New
'''

class Web_Marketing(models.Model):
    page_heading = models.CharField( max_length=50, help_text="Main Heading of the Page")
    page_description = models.TextField(help_text="Description of the page. ")
    # heading_for_box_section = HTMLField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Web Marketing'

class Web_Marketing_Box(models.Model):
    card = models.ForeignKey(Web_Marketing, default=None, on_delete=models.CASCADE)
    # box_image = models.FileField(upload_to='erp_solutions/images',blank=True, help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    package = models.CharField(max_length=50,blank=True,help_text="Enter your Package name eg. Platinum, Gold or Basic,Advanced")
    service = models.CharField(max_length=50,blank=True,help_text="Services tha you offers.. eg.- static, dynamic site, wordress etc.")
    package_description = HTMLField(blank=True, help_text="more text may create problem in UI. ")
    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural= 'Web Marketing Features and Prices'
    
'''
Domain Register New
'''

class Domain_Register(models.Model):
    page_heading = models.CharField( max_length=50, help_text="Main Heading of the Page")
    page_description = models.TextField(help_text="Description of the page. ")
    # heading_for_box_section = HTMLField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Domain Register'

class Domain_Register_Box(models.Model):
    card = models.ForeignKey(Domain_Register, default=None, on_delete=models.CASCADE)
    # box_image = models.FileField(upload_to='erp_solutions/images',blank=True, help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    package = models.CharField(max_length=50,blank=True,help_text="Enter your Package name eg. Platinum, Gold or Basic,Advanced")
    service = models.CharField(max_length=50,blank=True,help_text="Services tha you offers.. eg.- static, dynamic site, wordress etc.")
    package_description = HTMLField(max_length=350,blank=True, help_text="more text may create problem in UI. ")
    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural= 'Domain Register Features and Prices'
    
    
