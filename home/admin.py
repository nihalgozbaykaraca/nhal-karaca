from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactMessage, UserProfile, FAQ

admin.site.register(Setting)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']

admin.site.register(ContactMessage,ContactMessageAdmin)




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']

admin.site.register(UserProfile,UserProfileAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question','status']
    list_filter = ['status']

admin.site.register(FAQ,FAQAdmin)