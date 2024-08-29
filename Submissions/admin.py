from django.contrib import admin
from .models import Submissions, DocumentSubmissionAgencyType, DocumentSubmissionAgency

# Register your models here.
admin.site.register(Submissions)
admin.site.register(DocumentSubmissionAgencyType)
admin.site.register(DocumentSubmissionAgency)
