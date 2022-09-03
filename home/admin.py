from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Patient, Doctor, MedicalHistory, SelfMonitoringRecords

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalHistory)
admin.site.register(SelfMonitoringRecords)

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
    # model = CustomUser
    # filter_horizontal = ('groups' ,)
    # add_fieldsets = (
    #     *UserAdmin.add_fieldsets,
    #     (
    #         'Custom fields',
    #         {
    #             'fields': (
    #                 'gender',
    #                 'date_of_birth',
    #                 'groups',
    #             )
    #         }
    #     )
    # )
    
    # fieldsets = (
    #     *UserAdmin.fieldsets,
    #     (
    #         'Custom fields',
    #         {
    #             'fields': (
    #                 'gender',
    #                 'date_of_birth',
    #             )
    #         }
    #     )
    # )