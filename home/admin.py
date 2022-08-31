from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)

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