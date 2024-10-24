from django.contrib import admin
from .models import Profile, Course, Trainer, TimeSlot, Booking,DailyClass

from django import forms


class BookingAdminForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'course', 'trainer', 'timeslot', 'payment_status', 'class_assigned']

    class_assigned = forms.ModelChoiceField(
        queryset=DailyClass.objects.all(),
        required=False,
        label="Assign Class"
    )


class BookingAdmin(admin.ModelAdmin):
    form = BookingAdminForm
    list_display = ('user', 'course', 'trainer', 'payment_status', 'class_assigned')
    list_filter = ('payment_status', 'trainer', 'course')
    search_fields = ['user__username']

    def save_model(self, request, obj, form, change):
        # Logic for assigning class
        if form.is_valid():
            if obj.payment_status and form.cleaned_data['class_assigned']:
                obj.class_assigned = form.cleaned_data['class_assigned']
            super().save_model(request, obj, form, change)




admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(TimeSlot)
admin.site.register(Booking, BookingAdmin)
admin.site.register(DailyClass)
