from django.shortcuts import render, redirect,HttpResponseRedirect
from records.models import *
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.

def henquiry(request):
  
   

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        education = request.POST.get('education')
        intrest = request.POST.get('intrest')
        college = request.POST.get('college')

        print(name,'\n\n\n\n')
        
        data = HEnquiry(name = name, phone = phone, email=email, intrested_in = intrest,
                             education = education, collage = college)
    
        data.save()
        messages.success(request, "Form Submitted Successfully.......")
        
        
        
    return render(request, 'records/henquiry.html')
 




def apply_job(request):
    if request.method == "POST" and request.FILES['resume']:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        experience =request.POST.get('experience') 
        skills = request.POST.get('skills')
        qualification = request.POST.get('qualification')       
        remarks = request.POST.get('remarks')
        address = request.POST.get('address')
        position_applied_for = request.POST.get('position')
        # resume = request.FILES.get('resume')
        
        myfile = request.FILES['resume']
        fs = FileSystemStorage()
        filename = fs.save('resume/'+myfile.name, myfile)
        uploaded_file_url = fs.url('resume/'+filename)

        # print(resume, " \n\n\n\n")

        data_save = Apply_Job(full_name = name, phone_number = phone, email = email,  
                              position_applied_for  = position_applied_for,
                                qualification= qualification, remarks = remarks, address= address,
                                  gender= gender, experience = experience, skills = skills, resume = myfile)
        data_save.save()
        return render(request, 'records/apply_job.html', {'uploaded_file_url': uploaded_file_url})
    
    
    return render(request, 'records/apply_job.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        

    
        contact_data = Contact_data(name = name, email = email,phone=phone, subject = subject, message = message)
        contact_data.save()
        messages.success(request, "We Will Contact You Soon.......")
    return render(request, 'records/contact.html')







def registration(request):
    try:
        date_ = datetime.datetime.today()
        a = date_.strftime('%d-%m-%y')
        
        if request.method == 'POST':
            name = request.POST.get('name')
            father_name = request.POST.get('fathername')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            caddress = request.POST.get('caddress')
            module = request.POST.get('module')
            pursuing_details = request.POST.get('pursuingdetails')
            training_program = request.POST.get('trainingprogram')
            payment = request.POST.get('payment')
           
        send_data = Registration(name = name, father_name = father_name, phone=phone,
                                 email=email, address=address, caddress=caddress,
                                 module=module, pursuing_details=pursuing_details,
                                   training_program=training_program, payment_method=payment, date = a)
        send_data.save()
    except Exception as e:
        print(e)
        
    return render(request, 'records/registration.html')












def free_demo(request):
    # modules = ['finance','education','automobile','health']

    data = modules.objects.using('data').all()
    
    if request.method== 'POST':
        company_name = request.POST.get('company')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        module = request.POST.get('module')
        
        print(company_name, phone, email, module)
        request.session['user_details'] = {'company_name': request.POST.get('company'), 'phone': request.POST.get('phone'), 'email': request.POST.get('email'), 'phone':request.POST.get('phone'), 'module':request.POST.get('module')}   
        request.session.save() 
        print(request.session.items())
        return redirect('module')
    return render(request, 'records/free_demo.html', {'data':data})



def module(request):
    # Fetch headers from the database
    #  = Header.objects.all()
    headers = Header.objects.using('data').all()


    # Build the hierarchy
    header_dict = {}  # Use a dictionary for quick access by ID
    root_headers = []
    # print(request.session.items())
    for header in headers:
        header_dict[header.id] = header

        if header.parent_id: 
            parent = header_dict.get(header.parent_id)
            if parent:
                children = list(getattr(parent, 'children').all())
                if not children:
                    setattr(parent, 'children', children)
                children.append(header)
            else:
                root_headers.append(header)
        else:
            root_headers.append(header)

    context = {
        'root_headers': root_headers,
    }
     
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_checkboxes')
        demo_page_data = request.session.get('user_details', {})
        print(demo_page_data)
        combined_data_instance = Demo_Data(
            company_name=demo_page_data.get('company_name', ''),
            phone=demo_page_data.get('phone', ''),
            email=demo_page_data.get('email', ''),
            module=demo_page_data.get('module', ''),
            header_ids=selected_items
        )
        combined_data_instance.save()
       

    return render(request, 'records/module/module.html', context)