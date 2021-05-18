from django.contrib import admin

# Register your models here.
from novel.models import Charpter, Novel

admin.site.register(Charpter)
admin.site.register(Novel)
