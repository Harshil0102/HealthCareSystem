from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('about_appointment/<int:id>', views.about_appointment, name='about_appointment'),
    path('all_appointment/', views.all_appointment, name='all_appointment'),
    path('edit_appointment/<int:id>', views.edit_appointment, name='edit_appointment'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('all_patient/', views.all_patient, name='all_patient'),
    path('about_patient/', views.about_patient, name='about_patient'),
    path('edit_patient/', views.edit_patient, name='edit_patient'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('all_doctor/', views.all_doctor, name='all_doctor'),
    path('about_doctor/', views.about_doctor, name='about_doctor'),
    path('edit_doctor/', views.edit_doctor, name='edit_doctor'),
    path('add_payment/<int:id>', views.add_payment, name='add_payment'),
    path('all_payment/', views.all_payment, name='all_payment'),
    path('about_payment/<int:id>', views.about_payment, name='about_payment'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('profile/', views.profile, name='profile'),
    path('delete_appointment/<int:id>',views.delete_appointment ,name='delete_appointment'),
    path('get-service-cost/', views.get_service_cost, name='get_service_cost'),
    path('payment_history/', views.payment_history, name='payment_history'),
    path('search',views.search,name='search'),
    
]

# Only add this when we are in debug mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)