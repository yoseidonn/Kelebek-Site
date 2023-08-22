from django.contrib import admin
from .models import Slide, Feature, Heading

# Register your models here.
admin.site.register(Slide)
admin.site.register(Heading)
admin.site.register(Feature)