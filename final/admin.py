from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from final.models import *


# Register your models here.

class NUserAdmin(BaseUserAdmin):
  list_display=('name', 'email', 'date_joined', 'last_login', 'is_admin', 'is_active')
  search_fields=('name', 'email')
  readonly_fields=('date_joined','last_login')
  filter_horizontal=()
  list_filter=('last_login',)
  fieldsets=()

  add_fieldsets=(
    (None, {
      'classes':('wide'),
      'fields':('name','email','password1','password2'),
    }),
  )

  ordering=('email',)


admin.site.register(NUser, NUserAdmin)
admin.site.register(Comment)
admin.site.register(Progress)