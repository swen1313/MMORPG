from django.contrib import admin
from .models import Advert, AdvertCategory, Response, Category

admin.site.register(Category)
admin.site.register(Advert)
admin.site.register(AdvertCategory)
admin.site.register(Response)


# Register your models here.
