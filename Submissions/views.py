from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from .models import Submissions,DocumentSubmissionAgency, DocumentSubmissionAgencyType, Project
from .forms import SubmissionsForm, DocumentSubmissionAgencyForm, DocumentSubmissionAgencyTypeForm
# Create your views here. 

def submissionsList(request):
    submissions = Submissions.objects.all()

    context = {"submissions": submissions}
    return render(request, "submissions/submissionsList.html", context)

def projectSubmissionsListView(request, project_id):
    # Filter submissions by project ID
    project = Project.objects.get(id=project_id)
    submissions = Submissions.objects.filter(project=project)

    context = {"project": project, "submissions": submissions}
    return render(request, "submissions/projectSubmissionsList.html", context)

def submissionsCreateView(request):
    context = {}
    form = SubmissionsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/submissions/submissionsList")
    context["form"] = form
    return render(request, "submissions/submissionsCreateView.html", context)


def submissionsUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(Submissions, id=id)
    form = SubmissionsForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/submissions/submissionsList")
    context1["form"] = form
    return render(request, "submissions/submissionsUpdateView.html", context1)


def submissionsDeleteView(request, id):
    context2 = {}
    obj = get_object_or_404(Submissions, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/submissions/submissionsList")
    return render(request, "submissions/submissionsDeleteView.html", context2)


def dsaList(request,id):
    docSubAgency = DocumentSubmissionAgency.objects.all()

    context = {"docSubAgency": docSubAgency, "id":id}
    return render(request, "submissions/dsaList.html", context)

def dsaCreateView(request,id):
    context = {}

    if request.method == "POST":
        form = DocumentSubmissionAgencyForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            dsa = form.save()
            dsa.submissions_id = id
            dsa.save()
            return redirect("dsaList", id=id)
    else:
        form = DocumentSubmissionAgencyForm()
    context["form"] = form
    context["id"] = id
    return render(request, "submissions/dsaCreateView.html", context)

def dsaUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(DocumentSubmissionAgency, id=id)
    form = DocumentSubmissionAgencyForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/dsaList")

    context1["form"] = form

    return render(request, "submissions/dsaUpdateView.html", context1)

def dsaDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(DocumentSubmissionAgency, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/")
    return render(request, "submissions/submissionsDeleteView.html", context2)

def dsatList(request):
    dsat = DocumentSubmissionAgencyType.objects.all()

    context = {"dsat": dsat}
    return render(request, "submissions/dsatList.html", context)

def dsatCreateView(request):
    context = {}

    form = DocumentSubmissionAgencyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/dsatList")
    context["form"] = form
    return render(request, "submissions/dsatCreateView.html", context)

def dsatUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(DocumentSubmissionAgencyType, id=id)
    form = DocumentSubmissionAgencyTypeForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/dsatList")

    context1["form"] = form

    return render(request, "submissions/dsatUpdateView.html", context1)

def dsatDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(DocumentSubmissionAgencyType, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/")
    return render(request, "submissions/dsatDeleteView.html", context2)
