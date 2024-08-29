from django.contrib import admin
from .models import Tasks, TaskActivities, Hinderances,HinderanceFollowUp

# Register your models here.
admin.site.register(Tasks)
admin.site.register(TaskActivities)
admin.site.register(Hinderances)
admin.site.register(HinderanceFollowUp)

