from django.db import models


'''
Services New
'''

class Services(models.Model):
    page_heading = models.CharField( max_length=50)
    page_description = models.TextField()
    page_box_heading = models.CharField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Service'

        
class Services_box(models.Model):
    card = models.ForeignKey(Services, default=None, on_delete=models.CASCADE)
    box_image = models.FileField(upload_to='erp_solutions/images', help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    box_heading = models.CharField(max_length=70, help_text="Maximum Length 70 Chars.")
    box_description = models.CharField(max_length=250)

    def __str__(self):
        return self.card.page_heading
    class Meta: 
       verbose_name_plural = 'Services Box'
    

'''
Automobile New
'''

class Automobile(models.Model):
    page_heading = models.CharField( max_length=50)
    page_description = models.TextField()
    heading_for_box_section = models.CharField(max_length=250)

    def __str__(self):
        return self.page_heading
class Automobile_Box(models.Model):
    card = models.ForeignKey(Automobile, default=None, on_delete=models.CASCADE)
    box_image = models.FileField(upload_to='erp_solutions/images', help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    box_heading = models.CharField(max_length=70, help_text="Maximum Length 70 Chars.")
    box_description = models.CharField(max_length=250)

    def __str__(self):
        return self.card.page_heading
    


'''
Education New
'''

class Education(models.Model):
    page_heading = models.CharField( max_length=50)
    page_description = models.TextField()
    heading_for_box_section = models.CharField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Education'
class Education_Box(models.Model):
    card = models.ForeignKey(Education, default=None, on_delete=models.CASCADE)
    box_image = models.FileField(upload_to='erp_solutions/images', help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    box_heading = models.CharField(max_length=70, help_text="Maximum Length 70 Chars.")
    box_description = models.CharField(max_length=250)

    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural = 'Education Boxes'

'''
Tours And Travels New
'''

class Tours_Travels(models.Model):
    page_heading = models.CharField( max_length=50)
    page_description = models.TextField()
    heading_for_box_section = models.CharField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Tours And Travels'
class Tours_Travels_Box(models.Model):
    card = models.ForeignKey(Tours_Travels, default=None, on_delete=models.CASCADE)
    box_image = models.FileField(upload_to='erp_solutions/images', help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    box_heading = models.CharField(max_length=70, help_text="Maximum Length 70 Chars.")
    box_description = models.CharField(max_length=250)

    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural = 'Tours and Travel Box'
    

'''
Finance New
'''

class Finance(models.Model):
    page_heading = models.CharField( max_length=50)
    page_description = models.TextField()
    heading_for_box_section = models.CharField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Finance'
class Finance_Box(models.Model):
    card = models.ForeignKey(Finance, default=None, on_delete=models.CASCADE)
    box_image = models.FileField(upload_to='erp_solutions/images',blank=True, help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    box_heading = models.CharField(max_length=70,blank=True,help_text="Maximum Length 70 Chars.")
    box_description = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural = 'Finance Box'

'''
Medical  And HealthCare New
'''

class Medical_Healthcare(models.Model):
    page_heading = models.CharField( max_length=50)
    page_description = models.TextField()
    heading_for_box_section = models.CharField(max_length=250)

    def __str__(self):
        return self.page_heading
    class Meta: 
        verbose_name_plural = 'Medical & HealthCare'

class Medical_Healthcare_Box(models.Model):
    card = models.ForeignKey(Medical_Healthcare, default=None, on_delete=models.CASCADE)
    box_image = models.FileField(upload_to='erp_solutions/images',blank=True, help_text="Make sure your all image have same dimensions and have no background for better Appearence.")
    box_heading = models.CharField(max_length=70,blank=True,help_text="Maximum Length 70 Chars.")
    box_description = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.card.page_heading
    class Meta: 
        verbose_name_plural= 'Medical & HealthCare Boxes'
    
    
    
