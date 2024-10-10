import json
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Sector,ScopeGroup,ScopeItem, Client, Staff,ContactPerson,ProjectLead, ProjectProposal, Project
from DCI.models import DCI,DCIGroup,DCIItem
from .forms import SectorForm,ScopeGroupForm, ScopeItemForm, ClientForm, StaffForm, ContactPersonForm, ProjectLeadForm, ProjectProposalForm, ProjectForm
# Create your views here.

def sectorList(request):
    sector = Sector.objects.all()

    context = {"sector": sector}
    return render(request, "project/sectorList.html", context)

def sectorCreateView(request):
    form = SectorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        sector = form.save()
        if request.headers.get('HX-Request'):
            return render(request, 'project/sectorRow.html', {'sc': sector})
        return redirect('/project/sectorList')
    return render(request, "project/sectorCreateView.html", {'form': form})

# Update View
def sectorUpdateView(request, id):
    obj = get_object_or_404(Sector, id=id)
    form = SectorForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        sector = form.save()
        if request.headers.get('HX-Request'):
            return render(request, 'project/sectorRow.html', {'sc': sector})
        return redirect('/project/sectorList')
    return render(request, "project/sectorUpdateView.html", {'form': form, 'sc': obj})

# Delete View
def sectorDeleteView(request, id):
    obj = get_object_or_404(Sector, id=id)
    if request.method == "POST":
        obj.delete()
        if request.headers.get('HX-Request'):
            return HttpResponse('')
        return redirect('/project/sectorList')
    return render(request, "project/sectorDeleteView.html", {'sc': obj})

def scopeGroupList(request):
    scopeGroups = ScopeGroup.objects.all()
    context = {"scopeGroups": scopeGroups}
    return render(request, "project/scopeGroupList.html", context)

def scopeGroupCreateView(request):
    form = ScopeGroupForm(request.POST or None)

    if request.method == "POST":
        print("POST request received")  # Debugging
        if form.is_valid():
            print("Form is valid, saving data")  # Debugging
            form.save()
            return HttpResponse(status=204, headers={"HX-Trigger": "scopeGroupListChanged"})
        else:
            print("Form is not valid", form.errors)  # Debugging
    
    print("GET request or form invalid")  # Debugging
    return render(request, "project/scopeGroupCreateView.html", {"form": form})


def scopeGroupUpdateView(request, id):
    obj = get_object_or_404(ScopeGroup, id=id)
    
    if request.method == "POST":
        form = ScopeGroupForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            # HTMX success response, triggers update of the scope group list on the client
            return HttpResponse(status=204, headers={"HX-Trigger": "scopeGroupListChanged"})
        else:
            return HttpResponseBadRequest("Invalid form data")
    
    # For GET requests (loading the form into the modal)
    else:
        form = ScopeGroupForm(instance=obj)
        return render(request, "project/scopeGroupUpdateView.html", {"form": form, "scopeGroup": obj})



def scopeGroupDeleteView(request, id):
    obj = get_object_or_404(ScopeGroup, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponse(status=204, headers={"HX-Trigger": "scopeGroupListChanged"})
    return render(request, "project/scopeGroupDeleteView.html", {"scopeGroup": obj})

def scopeItemListHTMX(request, id):
    scopeGroup = get_object_or_404(ScopeGroup, id=id)
    scopeItems = ScopeItem.objects.filter(scopeGroup=scopeGroup)
    
    context = {
        "scopeItems": scopeItems,
        "scopeGroup": scopeGroup,
        "id": id
    }
    return render(request, "project/scopeItemList.html", context)



def scopeItemCreateView(request, id):
    scopeGroup = get_object_or_404(ScopeGroup, id=id)
    form = ScopeItemForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        scopeItem = form.save(commit=False)
        scopeItem.scopeGroup = scopeGroup
        scopeItem.save()
        return redirect('scopeItemListHTMX', id=id)  # Redirect after successful creation
    
    context = {
        'form': form,
        'scopeGroup': scopeGroup,
        'id': id,
    }
    return render(request, 'project/scopeItemCreateView.html', context)



def scopeItemUpdateView(request, id):
    obj = get_object_or_404(ScopeItem, id=id)
    scopeGroup = obj.scopeGroup
    
    if request.method == "POST":
        form = ScopeItemForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("scopeItemListHTMX", id=scopeGroup.id)
    else:
        form = ScopeItemForm(instance=obj)

    context = {
        "form": form,
        "scopeGroup": scopeGroup,
        "id":id,
    }
    return render(request, "project/scopeItemUpdateView.html", context)



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
        return redirect('plList')
    context = {'form': form}
    return render(request, 'project/plCreateView.html', context)


def plUpdateView(request, id):
    obj = get_object_or_404(ProjectLead, id=id)
    form = ProjectLeadForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('plList')  # Updated redirect
    context = {"form": form}
    return render(request, "project/plUpdateView.html", context)


def plDeleteView(request, id):
    obj = get_object_or_404(ProjectLead, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('plList')
    return render(request, "project/plDeleteView.html")


def ppList(request, id):
    projectProposals = ProjectProposal.objects.filter(projectLead=id)
    projectLead = get_object_or_404(ProjectLead, id=id)
    any_approved = projectProposals.filter(accepted=True).exists()
    context = {
        "projectProposals": projectProposals,
        "projectLead": projectLead,
        "id": id,
        "any_approved": any_approved
    }
    return render(request, "project/ppList.html", context)


def ppCreateView(request, id):
    projectLead = get_object_or_404(ProjectLead, id=id)

    form = ProjectProposalForm(request.POST or None)

    if form.is_valid():
        projectProposal = form.save(commit=False)
        projectProposal.projectLead = projectLead
        projectProposal.save()
        return redirect('ppList', id=id)

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
        return redirect('ppList', id=projectLead.id)  # Updated redirect

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
        return redirect('ppList', id=projectLead_id)
    context = {"object": obj}
    return render(request, "project/ppDeleteView.html", context)

def dciDetailView(request, id):
    dci = get_object_or_404(DCI, id=id)
    dci_groups = DCIGroup.objects.filter(dci=dci)  # Adjust the filter based on your model relationships
    dci_items = DCIItem.objects.filter(dciGroup__in=dci_groups)
    projectproposal = dci.projectproposal    # Fetch items associated with these groups
    projectLead = projectproposal.projectLead
    return render(request, 'project/dciDetailView.html', {
        'dci': dci,
        'dci_groups': dci_groups,
        'dci_items': dci_items,
        "projectproposal": projectproposal,
        "projectLead":projectLead,
    })


def projectList(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project/projectList.html", context)

def projectCreateView(request):
    form = ProjectForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("projectList")

    context = {"form": form}
    return render(request, "project/projectCreateView.html", context)

def projectUpdateView(request, id):
    obj = get_object_or_404(Project, id=id)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/project/projectList")
    context = {"form": form}
    return render(request, "project/projectUpdateView.html", context)

def projectDeleteView(request, id):
    obj = get_object_or_404(Project, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("projectList")
    context = {
        "project": obj,
        "id": obj.projectProposal.id
    }
    return render(request, "project/projectDeleteView.html", context)


def approve_proposal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        proposal_id = data.get('proposalId')
        approval_date = data.get('approvalDate')
        work_order_no = data.get('workOrderNo')
        work_order_date = data.get('workOrderDate')
        work_amount = data.get('workAmount')

        # Set all other proposals to False
        ProjectProposal.objects.filter(accepted=True).update(accepted=False)

        # Get the proposal being approved
        proposal = get_object_or_404(ProjectProposal, id=proposal_id)

        # Ensure the proposal has a valid projectLead before proceeding
        if proposal.projectLead is None:
            return JsonResponse({'error': 'Project Lead is missing for the selected proposal'}, status=400)

        # Update the proposal details
        proposal.accepted = True
        proposal.acceptedDate = approval_date
        proposal.workOrderNo = work_order_no
        proposal.workOrderDate = work_order_date
        proposal.workOrderCost = work_amount
        proposal.save()

        # Debugging output
        print(f"Creating project for sector: {proposal.projectLead.sector}")

        # Check if a project with the same sector already exists
        existing_project = Project.objects.filter(sector=proposal.projectLead.sector).first()
        if existing_project:
            return JsonResponse({'error': 'A project with the same sector already exists.'}, status=400)

        # Create a new project using details from the proposal and projectLead
        project = Project.objects.create(
            projectProposal=proposal,
            projectName=proposal.projectLead.projectName,
            cost=work_amount,
            agency=proposal.projectLead.agency,
            description=proposal.projectLead.description,
            sector=proposal.projectLead.sector,
            workOrderNo=work_order_no,
            workOrderDate=work_order_date,
        )

        return JsonResponse({'message': 'Project approved and created successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)





















 










