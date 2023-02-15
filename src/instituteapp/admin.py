from django.contrib import admin
from .models import ServicesData

class AdminServicesData(admin.ModelAdmin):
    list_display=['Course_Num','Course_Name','Starting_time','Starting_Date','Duration','Fee','Trainer_Name']


admin.site.register(ServicesData,AdminServicesData)
