from django.shortcuts import render
from career_and_intern.models import *




def career_with_us(request):
    data = Career_With_Us.objects.all()
    return render(request, 'career_and_intern/career_with_us.html', {'records':data})

def six_weeks_intern(request):
    six_weeks_data = Six_Weeks_Intern.objects.all()
    return render(request,"career_and_intern/6weeks_intern.html",{'six_weeks_intern_data':six_weeks_data})

def hope_program(request):
    hope_data = Hope_Program.objects.all()
    # print(hope_data)
    return render(request,"career_and_intern/hope_program.html", {'hope_data':hope_data})

def tech_discovery(request):
    tech_data = Tech_Descovery.objects.all()
    return render(request, 'career_and_intern/tech_discovery.html', {'tech_data': tech_data})



def trainee_placement(request):
    data = Traniee_with_us.objects.all()
    
    return render(request, 'career_and_intern/trainee_placement.html', {'data':data})
