from django.contrib import admin
from .models import Sector, ScopeItem, Staff,Client, ContactPerson,ProjectLead,Project,ProjectProposal
# Register your models here.
admin.site.register(Sector)
admin.site.register(ScopeItem)
admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(ContactPerson)
admin.site.register(ProjectLead)
admin.site.register(Project)
admin.site.register(ProjectProposal)

