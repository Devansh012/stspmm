from django.db import models
from DCI.models import DCI
from django.contrib.auth.models import User

class Sector(models.Model):
    sectorName = models.CharField(max_length=20)
    def __str__(self):
        return (self.sectorName)

class ScopeGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name    

class ScopeItem(models.Model):
    name = models.CharField(max_length=20)
    scopeGroup = models.ForeignKey(ScopeGroup,blank=True,null=True, related_name='scope_items', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Client(models.Model):
    name =  models.CharField(max_length=30,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    mobile = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    # name = models.CharField(max_length=30)
    fathersName = models.CharField(max_length=30, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    addressPresent = models.TextField(blank=True, null=True)
    addressHome = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    mobile1 = models.CharField(max_length=10, blank=True, null=True)
    mobile2 = models.CharField(max_length=10, blank=True, null=True)
    # documentSubmissionAgency = models.ForeignKey('Submissions.DocumentSubmissionAgency',on_delete=models.CASCADE,null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile', null=True, blank=True)

    def __str__(self):
        return str (self.user)

class ContactPerson(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile1 = models.CharField(max_length=10, blank=True, null=True)
    mobile2 = models.CharField(max_length=10, blank=True, null=True)
    landline = models.CharField(max_length=15, blank=True, null=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,blank=True,null=True)
    # dsa = models.ForeignKey(DocumentSubmissionAgency,on_delete=models.CASCADE,null=True,blank=True)
    address = models.TextField(blank=True, null=True)  # New field for address
    image = models.ImageField(upload_to='contact_images/', blank=True, null=True)  # New field for image


    def __str__(self):
        return self.name

class ProjectLead(models.Model):
    projectName = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    agency = models.CharField(max_length=30, blank=True, null=True)
    approved = models.BooleanField(default=False,null=True,blank=True)
    description = models.TextField(blank=True, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, blank=True, null=True)
    scopeItem = models.ForeignKey(ScopeItem, on_delete=models.CASCADE, blank=True, null=True)
    source = models.CharField(max_length=30)
    sourceDescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.projectName
 
class ProjectProposal(models.Model):
    projectLead = models.OneToOneField(ProjectLead, on_delete=models.CASCADE, blank=True, null=True)
    submittedTo = models.ForeignKey(Client, on_delete=models.CASCADE)
    submissionDate = models.DateField(blank=True, null=True)
    proposalCost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    docControlIndex = models.OneToOneField(DCI, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False, blank=True, null=True)
    acceptedDate = models.DateField(blank=True, null=True)
    workOrderNo = models.CharField(max_length=15, blank=True, null=True)
    workOrderDate = models.DateField(blank=True, null=True)
    workOrderCost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Proposal to {self.submittedTo} by {self.projectLead} on {self.submissionDate} | Cost: {self.proposalCost}"


class Project(models.Model):
    projectProposal = models.ForeignKey(ProjectProposal, on_delete=models.CASCADE, blank=True, null=True)
    projectName = models.CharField(max_length=30, blank=True, null=True)
    cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    agency = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sector = models.OneToOneField(Sector, on_delete=models.CASCADE)
    # scopeItems = models.ForeignKey(ScopeItem, on_delete=models.CASCADE, blank=True, null=True)
    incharge = models.ForeignKey(Staff, related_name='incharge_projects', on_delete=models.CASCADE, blank=True, null=True)
    # team = models.ForeignKey(Staff, related_name='team_projects', on_delete=models.CASCADE, blank=True, null=True) many to many
    dateOfCommencement = models.DateField(blank=True, null=True)
    lastDateOfDelivery = models.DateField(blank=True, null=True)
    workOrderNo =  models.CharField(max_length=25,blank=True,null=True,verbose_name='Work Order Number')
    workOrderDate = models.DateField(blank=True,null=True,verbose_name='Work Order Date')
    file = models.FileField(blank=True,null=True,verbose_name='File')
    finalDCI = models.ForeignKey(DCI, on_delete=models.CASCADE, blank=True, null=True)
    # documents = models.ForeignKey('docs.Document', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.projectName if self.projectName else "Unnamed Project"

    

