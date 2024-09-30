from django.contrib import admin
from .models import Profile, Course, Trainer, TimeSlot, Booking

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(TimeSlot)
admin.site.register(Booking)

