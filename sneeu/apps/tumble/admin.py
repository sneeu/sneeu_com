from django.contrib import admin
from django.forms.models import modelform_factory

from models import Service, Log, Media


admin.site.register(Service)
admin.site.register(Log)
admin.site.register(Media)

