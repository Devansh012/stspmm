from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from .models import Sector,ScopeGroup,ScopeItem, Client, Staff,ContactPerson,ProjectLead, ProjectProposal, Project
from .forms import SectorForm,ScopeGroupForm, ScopeItemForm, ClientForm, StaffForm, ContactPersonForm, ProjectLeadForm, ProjectProposalForm, ProjectForm
# Create your views here.

def sectorList(request):
    sector = Sector.objects.all()

    context = {"sector": sector}
    return render(request, "project/sectorList.html", context)

def sectorCreateView(request):
    context = {}

    form = SectorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/project/sectorList")
    context["form"] = form
    return render(request, "project/sectorCreateView.html", context)

def sectorUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(Sector, id=id)
    form = SectorForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/project/sectorList")

    context1["form"] = form

    return render(request, "project/sectorUpdateView.html", context1)

def sectorDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(Sector, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/project/sectorList")
    return render(request, "project/sectorDeleteView.html", context2)

def scopeGroupList(request):
    scopeGroups = ScopeGroup.objects.all()  # Use plural for consistency

    context = {"scopeGroups": scopeGroups}
    return render(request, "project/scopeGroupList.html", context)


def scopeGroupCreateView(request):
    form = ScopeGroupForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("scopeGroupList")  # Use named URL pattern
    return render(request, "project/scopeGroupCreateView.html", {"form": form})


def scopeGroupUpdateView(request, id):
    obj = get_object_or_404(ScopeGroup, id=id)
    form = ScopeGroupForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("scopeGroupList")  # Use named URL pattern

    return render(request, "project/scopeGroupUpdateView.html", {"form": form})


def scopeGroupDeleteView(request, id):
    obj = get_object_or_404(ScopeGroup, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("scopeGroupList")  # Use named URL pattern

    return render(request, "project/scopeGroupDeleteView.html", {"scopeGroup": obj})

def scopeItemList(request, id):
    scopeGroup = get_object_or_404(ScopeGroup, id=id)
    scopeItems = ScopeItem.objects.filter(scopeGroup=scopeGroup)
    context = {
        "scopeItems": scopeItems,
        "scopeGroup": scopeGroup,  # Include the ScopeGroup object in the context
        "id": id
    }
    return render(request, "project/scopeItemList.html", context)



def scopeItemCreateView(request, id):
    context = {}
    scopeGroup = get_object_or_404(ScopeGroup, id=id)

    if request.method == "POST":
        form = ScopeItemForm(request.POST, request.FILES)
        if form.is_valid():
            scopeItem = form.save(commit=False)
            scopeItem.scopeGroup = scopeGroup
            scopeItem.save()
            return redirect("scopeItemList", id=id)  # Redirect after successful creation
    else:
        form = ScopeItemForm()  # Initialize empty form for GET request

    # Populate the context with the form and other data
    context["form"] = form
    context["id"] = id
    context["scopeGroup_name"] = scopeGroup.name
    
    return render(request, "project/scopeItemCreateView.html", context)


def scopeItemUpdateView(request, id):
    obj = get_object_or_404(ScopeItem, id=id)
    scopeGroup = obj.scopeGroup
    context1 = {"scopeGroup": scopeGroup}
    if request.method == "POST":
        form = ScopeItemForm(request.POST or None, request.FILES or None, instance=obj, parent_scopeGroup=scopeGroup)
        if form.is_valid():
            form.save()
            return redirect("scopeItemList", id=scopeGroup.id)  # Use named URL pattern
    else:
        form = ScopeItemForm(instance=obj, parent_scopeGroup=scopeGroup)

    context1["form"] = form
    return render(request, "project/scopeItemUpdateView.html", context1)



def scopeItemDeleteView(request, id):
    obj = get_object_or_404(ScopeItem, id=id)
    scopeGroup_id = obj.scopeGroup.id

    if request.method == "POST":
        obj.delete()
        return redirect("scopeItemList",id=scopeGroup_id)  # Use named URL pattern

    context = {"object":obj}
    return render(request, "project/scopeItemDeleteView.html", context)


def clientList(request):
    client = Client.objects.all()

    context = {"client": client}
    return render(request, "project/clientList.html", context)

def clientCreateView(request):
    context = {}

    form = ClientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/project/clientList")
    context["form"] = form
    return render(request, "project/clientCreateView.html", context)

def clientUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/project/clientList")

    context1["form"] = form

    return render(request, "project/clientUpdateView.html", context1)

def clientDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(Client, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/project/clientList")
    return render(request, "project/clientDeleteView.html", context2)

def staffList(request):
    staff = Staff.objects.all()
    context = {"staff": staff}
    return render(request, "project/staffList.html", context)

def staffCreateView(request):
    context = {}
    
    # Check if the user already has a staff profile
    if Staff.objects.filter(user=request.user).exists():
        return redirect('staffUpdateView', id=request.user.staff_profile.id)
    
    form = StaffForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        staff_instance = form.save(commit=False)
        staff_instance.user = request.user
        staff_instance.save()
        return HttpResponseRedirect("/project/staffList")
    
    context["form"] = form
    return render(request, "project/staffCreateView.html", context)

def staffUpdateView(request, id):
    obj = get_object_or_404(Staff, id=id)
    
    if obj.user != request.user:
        return redirect('/project/staffList')  # Restrict updates to the owner only

    form = StaffForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        staff_instance = form.save(commit=False)
        staff_instance.user = request.user  # Keep the logged-in user associated
        staff_instance.save()
        return redirect("/project/staffList")

    context1 = {"form": form}
    return render(request, "project/staffUpdateView.html", context1)

def staffDeleteView(request, id):
    obj = get_object_or_404(Staff, id=id)
    
    if obj.user != request.user:
        return redirect('/project/staffList')  # Restrict deletion to the owner only

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/project/staffList")
    
    return render(request, "project/staffDeleteView.html")
def cpList(request):
    contactPersons = ContactPerson.objects.all()  # Use plural for consistency

    context = {"contactPersons": contactPersons}
    return render(request, "project/cpList.html", context)


def cpCreateView(request):
    form = ContactPersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("cpList")  # Use named URL pattern
    return render(request, "project/cpCreateView.html", {"form": form})


def cpUpdateView(request, id):
    obj = get_object_or_404(ContactPerson, id=id)
    form = ContactPersonForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("cpList")  # Use named URL pattern

    return render(request, "project/cpUpdateView.html", {"form": form})


def cpDeleteView(request, id):
    obj = get_object_or_404(ContactPerson, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("cpList")  # Use named URL pattern

    return render(request, "project/cpDeleteView.html", {"contactPerson": obj})


def plList(request):
    projectLeads = ProjectLead.objects.all()
    context = {"projectLeads": projectLeads}
    return render(request, "project/plList.html", context)

def plCreateView(request):
    form = ProjectLeadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('plList')  # Redirect to a list or another page after creation
    context = {'form': form}
    return render(request, 'project/plCreateView.html', context)

def plUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(ProjectLead,id=id)
    form = ProjectLeadForm(request.POST or None, request.FILES or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect("/project/plList")
    context1["form"] = form
    return render(request, "project/plUpdateView.html", context1)

def plDeleteView(request, id):
    obj = get_object_or_404(ProjectLead, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("plList")
    return render(request, "project/plDeleteView.html")


def ppList(request, id):
    projectProposals = ProjectProposal.objects.filter(projectLead = id)
    projectLead = get_object_or_404(ProjectLead, id=id)
    context = {"projectProposals":projectProposals,"projectLead":projectLead,"id":id}
    return render(request,"project/ppList.html", context)

def ppCreateView(request, id):
    projectLead = get_object_or_404(ProjectLead, id=id)
    form = ProjectProposalForm(request.POST or None, parent_projectLead=projectLead)
    
    if form.is_valid():
        projectProposal = form.save(commit=False)
        projectProposal.projectLead = projectLead
        projectProposal.save()
        return redirect("ppList", id=id)
    
    context = {
        "form": form,
        "id": id,
        "projectLead": projectLead,
    }

    return render(request, "project/ppCreateView.html", context)


def ppUpdateView(request, id):
    obj = get_object_or_404(ProjectProposal, id=id)
    projectLead = obj.projectLead
    form = ProjectProposalForm(request.POST or None, request.FILES or None, instance=obj, parent_projectLead=projectLead)
    
    if form.is_valid():
        form.save()
        return redirect("ppList", id=projectLead.id)
    
    context = {
        "form": form,
        "projectLead": projectLead,
    }
    return render(request, "project/ppUpdateView.html", context)




def ppDeleteView(request, id):
    obj = get_object_or_404(ProjectProposal, id=id)
    projectLead_id = obj.projectLead.id
    if request.method == "POST":
        obj.delete()
        return redirect("ppList", id=projectLead_id)
    context ={"object":obj}
    return render(request, "project/ppDeleteView.html",context)



def projectList(request, id):
    projects = Project.objects.filter(projectProposal=id)
    projectProposal = get_object_or_404(ProjectProposal, id=id)
    context = {
        "projects": projects,
        "projectProposal": projectProposal,
        "id": id
    }
    return render(request, "project/projectList.html", context)


def projectCreateView(request, id):
    projectProposal = get_object_or_404(ProjectProposal, id=id)
    form = ProjectForm(request.POST or None, parent_projectProposal=projectProposal)
    
    if form.is_valid():
        project = form.save(commit=False)
        project.projectProposal = projectProposal
        project.save()
        return redirect("projectList", id=id)
    
    context = {
        "form": form,
        "projectProposal": projectProposal,
        "id": id
    }
    return render(request, "project/projectCreateView.html", context)



def projectUpdateView(request, id):
    obj = get_object_or_404(Project, id=id)
    projectProposal = obj.projectProposal
    form = ProjectForm(request.POST or None, request.FILES or None, instance=obj, parent_projectProposal=projectProposal)
    
    if form.is_valid():
        form.save()
        return redirect("projectList", id=projectProposal.id)

    context = {
        "form": form,
        "project": obj,
        "projectProposal": projectProposal,
    }
    return render(request, "project/projectUpdateView.html", context)



def projectDeleteView(request, id):
    obj = get_object_or_404(Project, id=id)
    
    if request.method == "POST":
        obj.delete()
        return redirect("projectList", id=obj.projectProposal.id)
    
    context = {
        "project": obj,
        "id": obj.projectProposal.id
    }
    return render(request, "project/projectDeleteView.html", context)



















 










