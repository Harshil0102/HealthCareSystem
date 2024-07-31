from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Home.models import Appointment, Payment, Service, payment_service
# from Home.models import Appointment
from accounts.models import *
from accounts.forms import ProfileUpdateForm,UserUpdateForm

from django.http import JsonResponse
from .models import Service, payment_service

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

# Appointment view files
@login_required(login_url='/accounts/login')
def add_appointment(request):
     if request.method == 'POST':
        patient = request.user
        doctor = request.POST.get('doctor-data')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')
        doc = User.objects.get(id=doctor)
        appointment = Appointment(patient=patient, doctor=doc, date=date, time=time, reason=reason)
        appointment.save()
        messages.success(request, 'Appointment created successfully!')
        return redirect('/all_appointment')

     doctors = User.objects.filter(role='2')
     return render(request, 'add_appointment.html',{'doctors': doctors})


def about_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    return render(request, 'about_appointment.html', {'appointment': appointment})

def edit_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    if request.method == 'POST':
        
        d = request.POST.get('doctor-data')
        appointment.doctor = User.objects.get(id=d) 
        appointment.date = request.POST.get('date')
        appointment.time = request.POST.get('time')
        appointment.reason = request.POST.get('reason')
        appointment.save()

        messages.success(request, 'Appointment updated successfully!')
        if request.user.role == '1':
            return redirect('/all_appointment')
        else:
            return redirect('/all_appointment')
    doctors = User.objects.filter(role='2')

    return render(request, 'edit_appointment.html', {'appointment': appointment,'doctors': doctors})

def delete_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    messages.success(request, 'Appointment deleted successfully!')
    if request.user.role == '1':
        return redirect('/all_appointment')
    else:
        return redirect('/all_appointment')
    


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

    
def all_appointment(request):
    role = request.user.role
    if role == '1':
        appointments = Appointment.objects.filter(patient=request.user)
    elif role == '2':
        appointments = Appointment.objects.filter(doctor=request.user,status='approved')
    else:
        appointments = Appointment.objects.all()

    # Search functionality
    search_query = request.GET.get('search_prd')
    if search_query:
        appointments = appointments.filter(
            Q(doctor__first_name__icontains=search_query) | 
            Q(doctor__last_name__icontains=search_query) |
            Q(patient__first_name__icontains=search_query) |
            Q(patient__last_name__icontains=search_query)
        )

    return render(request, 'all_appointment.html', {'appointments': appointments, 'role': role})

    

# End appointment view files

# Patient view files

def add_patient(request):
    return render(request, 'add_patient.html')

def all_patient(request):
    return render(request, 'all_patient.html')

def about_patient(request):
    return render(request, 'about_patient.html')

def edit_patient(request):
    return render(request, 'edit_patient.html')

# End patient view files

# Doctor view files

def add_doctor(request):
    return render(request, 'add_doctor.html')

def all_doctor(request):
    return render(request, 'all_doctor.html')

def about_doctor(request):
    return render(request, 'about_doctor.html')

def edit_doctor(request):
    return render(request, 'edit_doctor.html')

# End Doctor view files

#  payment view files

def add_payment(request, id):
    if request.method == 'POST':
        serviceId = request.POST.getlist("service_id")
        payment_type = request.POST["payment_type"]
        total_cost = request.POST["total_cost"]
        print(total_cost)
        ap = Appointment.objects.get(id=id)
        payment = Payment(appointment=ap, payment_type=payment_type,user=request.user,total_cost=total_cost).save()
        last_payment = Payment.objects.last()

        for i in serviceId:
            s = Service.objects.get(id=i)
            p = payment_service(payment=last_payment,service=s)
            p.save()
        messages.success(request, 'Payment Successful')
        return redirect('/payment_history')
    template_name = 'add_payment.html'
    service = Service.objects.all()

    return render(request,template_name,{'Service':service,'id':id})



def about_payment(request, id):
    ap = Payment.objects.get(id=id)

    P_service = payment_service.objects.filter(payment=id)
    # print(P_service)
    # for i in P_service:
    #     print(i.service.service_name)
    return render(request, 'about_payment.html',{'Payment':ap,'Service':P_service})


def get_service_cost(request):
    service_id = request.GET.get('service_id')
    service = Service.objects.get(id=service_id)
    return JsonResponse({'service_cost': service.service_cost})

def payment_history(request):
    payment = Payment.objects.filter(user=request.user)
    return render(request, 'payment_history.html',{'Payment': payment})

def all_payment(request):
    return render(request, 'all_payment.html')

#  End Payment view files

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

# profile views 


def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)

def search(request):
    query = request.GET['search_prd']

    if len(query)>250 or len(query)==0:
        allpro = Appointment.objects.none()
    else:
        allpro = Appointment.objects.filter(status__icontains=query)
        # category = Product.objects.filter(c_id__icontains=query)
        # allpro = product.union(category)

    if allpro.count()==0:
        messages.warning(request, 'No search result found. please refine your query.')

    context = {'allpro': allpro, 'query': query}
    return render(request,'search.html', context)