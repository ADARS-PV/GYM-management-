\
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('courses/', views.course_list, name='course_list'),
    path('trainers/<int:course_id>/', views.trainer_list, name='trainer_list'),
    path('timeslots/<int:trainer_id>/', views.timeslot_list, name='timeslot_list'),
    path('payment/<int:timeslot_id>/', views.payment, name='payment'),
    path('payment/callback/', views.payment_callback, name='payment_callback'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)