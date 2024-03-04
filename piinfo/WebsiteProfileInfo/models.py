from django.db import models




class WebsiteProfileData(models.Model):
    phone = models.CharField( max_length=13, help_text = "Enter Phone Number with Country Code.")
    email = models.CharField( max_length=150, help_text = "Email of the Company")
    company_address = models.CharField( max_length=150, help_text = "Enter Address that you want to show in footer. ")

    def __str__(self):
        return 'Company Contact Details'
    class Meta: 
       verbose_name_plural = 'Website Profle Info'


class SocialProfileLink(models.Model):
    youtube_link = models.CharField(max_length=150, blank = True,  default="https://www.pisoftinformatics.com", help_text = "Enter Youtube link that starts with https. ex: https://www.youtube.com/xyz ")
    linkedin_link = models.CharField(max_length=150, blank = True,default="https://www.pisoftinformatics.com" , help_text = "Enter Linkedin link that starts with https. ex: https://www.linkedin.com/xyz ")
    twitter_link = models.CharField(max_length=150, blank = True, default="https://www.pisoftinformatics.com" , help_text = "Enter Twitter link that starts with https. ex: https://www.twitter.com/xyz ")
    facebook_link = models.CharField(max_length=150, blank = True,default="https://www.pisoftinformatics.com" , help_text = "Enter Facebook link that starts with https. ex: https://www.facebook.com/xyz ")

    def __str__(self):
        return "Social Profile Links "
    class Meta: 
       verbose_name_plural = 'Social Media Profile Links'