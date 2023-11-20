from django.shortcuts import render, HttpResponse, get_object_or_404
from erp_solutions.models import *




'''
Services 
'''
def services(request):
    header = Services.objects.all()
    box = Services_box.objects.all()
    return render(request, 'erp_solutions/services.html',{'header':header,'box':box})


'''
Automobile
'''
def automobile(request):
    header = Automobile.objects.all()
    box = Automobile_Box.objects.all()
    return render(request, 'erp_solutions/automobile.html',{'header':header,'box':box})

'''
Education 
'''
def education(request):
    header = Education.objects.all()
    box = Education_Box.objects.all()
    return render(request, 'erp_solutions/education.html',{'header':header,'box':box})

'''
Tours And Travels 
'''
def tours_travels(request):
    header = Tours_Travels.objects.all()
    box = Tours_Travels_Box.objects.all()
    return render(request, 'erp_solutions/tours_and_travels.html',{'header':header,'box':box})

'''
Finance
'''
def finance(request):
    header = Finance.objects.all()
    box = Finance_Box.objects.all()
    return render(request, 'erp_solutions/finance.html',{'header':header,'box':box})

'''
Medical_Healthcare_Box
'''
def medical_healthcare(request):
    header = Medical_Healthcare.objects.all()
    box = Medical_Healthcare_Box.objects.all()
    return render(request, 'erp_solutions/medical_and_healthcare.html',{'header':header,'box':box})