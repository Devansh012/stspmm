from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from .models import Sector,ScopeItem, Client, Staff,ContactPerson,ProjectLead, ProjectProposal, Project
from .forms import SectorForm, ScopeItemForm, ClientForm, StaffForm, ContactPersonForm, ProjectLeadForm, ProjectProposalForm, ProjectForm
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

def scopeItemList(request):
    scopeItems = ScopeItem.objects.all()  # Use plural for consistency

    context = {"scopeItems": scopeItems}
    return render(request, "project/scopeItemList.html", context)


def scopeItemCreateView(request):
    form = ScopeItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("scopeItemList")  # Use named URL pattern
    return render(request, "project/scopeItemCreateView.html", {"form": form})


def scopeItemUpdateView(request, id):
    obj = get_object_or_404(ScopeItem, id=id)
    form = ScopeItemForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("scopeItemList")  # Use named URL pattern

    return render(request, "project/scopeItemUpdateView.html", {"form": form})


def scopeItemDeleteView(request, id):
    obj = get_object_or_404(ScopeItem, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("scopeItemList")  # Use named URL pattern

    return render(request, "project/scopeItemDeleteView.html", {"scopeItem": obj})


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

    form = StaffForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/project/staffList")
    context["form"] = form
    return render(request, "project/staffCreateView.html", context)

def staffUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(Staff, id=id)
    form = StaffForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/project/staffList")

    context1["form"] = form

    return render(request, "project/staffUpdateView.html", context1)

def staffDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(Staff, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/project/staffList")
    return render(request, "project/staffDeleteView.html", context2)

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


def plList(request,id):
    projectLead = ProjectLead.objects.filter(projectproposal = id)

    context = {"projectLead": projectLead, "id":id}
    return render(request, "project/plList.html", context)

def plCreateView(request):
    context = {}

    if request.method == "POST":
        form = ProjectLeadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            pl= form.save()
            pl.projectproposal.id = id
            pl.save()
            return redirect("/project/plList",id=id)
    else:
        form = ProjectLeadForm()
    context["form"] = form
    context["id"] = id
    return render(request, "project/plCreateView.html", context)

def plUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(ProjectLead, id=id)
    form = ProjectLeadForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("project/plList")

    context1["form"] = form

    return render(request, "project/plUpdateView.html", context1)

def plDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(ProjectLead, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/project/plList")
    return render(request, "project/plDeleteView.html", context2)

def ppList(request,id):
    projectProposal = ProjectProposal.objects.filter(project = id)

    context = {"projectProposal": projectProposal,"id":id}
    return render(request, "project/ppList.html", context)

def ppCreateView(request,id):
    context = {}

    if request.method == "POST":
        form = ProjectProposalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            pp= form.save()
            pp.project_id = id
            pp.save()
            return redirect("/project/ppList",id=id)
    else:
        form = ProjectProposalForm()
    context["form"] = form
    context["id"] = id
    return render(request, "project/ppCreateView.html", context)

def ppUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(ProjectProposal, id=id)
    form = ProjectProposalForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("project/ppList")

    context1["form"] = form

    return render(request, "project/ppUpdateView.html", context1)

def ppDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(ProjectProposal, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("project/ppList")
    return render(request, "project/ppDeleteView.html", context2)

def projectList(request):
    project = Project.objects.all()
    context = {"project": project}
    return render(request, "project/projectList.html", context)


def projectCreateView(request):
    context = {}
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("projectList")
    context["form"] = form
    return render(request, "project/projectCreateView.html", context)

def projectUpdateView(request, id):
    obj = get_object_or_404(Project, id=id)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("projectList")
    context = {"form": form, "project": obj}
    return render(request, "project/projectUpdateView.html", context)


def projectDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(Project, id=id)

    if request.method == "POST":

        obj.delete()

        return redirect("/project/projectList")
    return render(request, "project/projectDeleteView.html", context2)
















 










