from django.db import models
from Project.models import Project, Staff, ContactPerson
from DCI.models import DCIItem
from Docs.models import Document

# Create your models here.
class Submissions(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    name =  models.CharField(max_length=20,verbose_name='Name')
    revisionNo = models.IntegerField(blank=True, null=True)
    whyRevision = models.TextField(blank=True, null=True)
    checkedBy = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True)
    checkingDate = models.DateField(blank=True, null=True)
    printedBy = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True, related_name='printingStaff')
    printingDate = models.DateField(blank=True, null=True)
    submittedTo = models.ForeignKey('DocumentSubmissionAgency', on_delete=models.CASCADE, blank=True, null=True)
    submissionDate = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dciItems = models.ForeignKey(DCIItem, on_delete=models.CASCADE, blank=True, null=True)
    documents = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True)
    earlierSubmissionReference = models.CharField(max_length=30, blank=True, null=True)
    commentIfAny = models.TextField(blank=True, null=True)
    commentDocument = models.FileField(blank=True, null=True)
    commentReply = models.TextField(blank=True, null=True)
    replyDocument = models.FileField(blank=True, null=True)
    approved = models.BooleanField(default=False, blank=True, null=True)
    approvalDate = models.DateField(blank=True, null=True)
    # finalApprovedDocuments = models.OneToOneField(Document, related_name='final_documents', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        project_name = self.project if self.project else "No Project"
        revision = f"Revision {self.revisionNo}" if self.revisionNo is not None else "No Revision"
        submission_date = self.submissionDate if self.submissionDate else "No Submission Date"
        return f"{project_name} - {revision} submitted on {submission_date}"


    

class DocumentSubmissionAgency(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    agencytype = models.ForeignKey('DocumentSubmissionAgencyType', on_delete=models.CASCADE, blank=True, null=True)
    contactPersons = models.ForeignKey(ContactPerson, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        agency_name = self.name if self.name else "Unnamed Agency"
        agency_type = self.agencytype.DSATName if self.agencytype else "No Type"
        return f"{agency_name} ({agency_type})"


class DocumentSubmissionAgencyType(models.Model):
    DSATName = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.DSATName if self.DSATName else "No Agency Type"

