from django.contrib import admin
from account import models

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (                                               #the order in which the fileds should appear in admin page
        (None, {'fields': ('email', 'name', 'password')}),
        ("Permission", {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        ("Important Dates", {
            'fields': (
                'last_login',
            )
        }),
    )
    readonly_fields = ['last_login']        #we can only read it we can't modify it 

    def save_model(self, request, obj, form, change):

        '''creating the user in admin page so that it can store the password by hashing'''
        password = form.cleaned_data.get('password')
        obj.set_password(password)
        if password and password != obj.password:
            obj.set_password(password)

        
        super().save_model(request, obj, form, change)
        
admin.site.register(models.User, CustomUserAdmin)