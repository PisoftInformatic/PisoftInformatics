from .models import *  # Import your model representing company information

def footer_data(request):
    try:
        company_info = WebsiteProfileData.objects.first()  # Fetch the company information from your database
        company_social_profile = SocialProfileLink.objects.first()  # Fetch the company information from your database
    except WebsiteProfileData.DoesNotExist and SocialProfileLink.DoesNotExist:
        company_info,company_social_profile = None, None
    return {
        'company_info': company_info,
        'company_social_profile'  : company_social_profile
    }