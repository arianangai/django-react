from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
  list = ('firstname', 'lastname', 'email', 'phone', 'jobtitle', 'centername', 'businessdesc', 'centerstatus', 'licensecap', 'country', 'comments', 'tnc')

admin.site.register(Form, FormAdmin)
