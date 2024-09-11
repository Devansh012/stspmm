from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from .models import Tasks, TaskActivities, Hinderances, HinderanceFollowUp, Project
from .forms import (
    TasksForm,
    TaskActivitiesForm,
    HinderancesForm,
    HinderanceFollowUpForm,
)

from django.http import FileResponse


def tasksList(request,id):
    tasks = Tasks.objects.filter(project = id)
    project = get_object_or_404(Project, id=id)
    context = {"tasks":tasks,"project":project,"id":id}
    return render(request,"tasks/tasksList.html", context)


def tasksCreateView(request, id):
    project = get_object_or_404(Project, id=id)
    form = TasksForm(request.POST or None, project=project)
    
    if form.is_valid():
        tasks = form.save(commit=False)
        tasks.project = project  # Ensure project is set
        tasks.save()
        return redirect("tasksList", id=id)
    
    context = {
        "form": form,
        "id": id,
        "project": project,
    }

    return render(request, "tasks/tasksCreateView.html", context)


def tasksUpdateView(request, id):
    obj = get_object_or_404(Tasks, id=id)
    project = obj.project
    form = TasksForm(request.POST or None, request.FILES or None, instance=obj, project=project)
    
    if form.is_valid():
        form.save()
        return redirect("tasksList", id=project.id)
    
    context = {
        "form": form,
        "project": project,
    }
    return render(request, "tasks/tasksUpdateView.html", context)


def tasksDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(Tasks, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/tasks/tasksList")
    return render(request, "tasks/tasksDeleteView.html", context2)


def taskActivitiesList(request, id):
    task = get_object_or_404(Tasks, id=id)
    taskActivities = TaskActivities.objects.filter(task_id=id)
    project = task.project  # Retrieve the project from the task
    context = {
        "taskactivities": taskActivities,
        "task": task,
        "project": project,  # Add the project to the context
        "id": id,
    }
    return render(request, 'tasks/taskActivitiesList.html', context)


def taskActivitiesCreateView(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == "POST":
        form = TaskActivitiesForm(request.POST or None, request.FILES or None, user=request.user)
        if form.is_valid():
            task_activities = form.save(commit=False)
            task_activities.task = task
            task_activities.save()
            return redirect("taskActivitiesList", id=id)
    else:
        form = TaskActivitiesForm(user=request.user)
    context = {"form": form, "task": task}
    return render(request, "tasks/taskActivitiesCreateView.html", context)

def taskActivitiesUpdateView(request, id):
    task_activity = get_object_or_404(TaskActivities, id=id)
    task = task_activity.task
    if request.method == "POST":
        form = TaskActivitiesForm(request.POST or None, request.FILES or None, instance=task_activity, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("taskActivitiesList", id=task.id)
    else:
        form = TaskActivitiesForm(instance=task_activity, user=request.user)
    context = {"form": form, "task": task}
    return render(request, "tasks/taskActivitiesUpdateView.html", context)

def taskActivitiesDeleteView(request, id):
    task_activity = get_object_or_404(TaskActivities, id=id)
    task = task_activity.task
    if request.method == "POST":
        task_activity.delete()
        return redirect("taskActivitiesList", id=task.id)
    context = {"task_activity": task_activity, "task": task}
    return render(request, "tasks/taskActivitiesDeleteView.html", context)

def hinderancesList(request):
    hinderances = Hinderances.objects.all()
    return render(request, 'tasks/hinderancesList.html', {'hinderances': hinderances})

def hinderancesCreateView(request):
    form = HinderancesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("hinderancesList")
    context = {"form": form}
    return render(request, "tasks/hinderancesCreateView.html", context)

def hinderancesUpdateView(request, id):
    obj = get_object_or_404(Hinderances, id=id)
    form = HinderancesForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("hinderancesList")
    context = {"form": form}
    return render(request, "tasks/hinderancesUpdateView.html", context)

def hinderancesDeleteView(request, id):
    obj = get_object_or_404(Hinderances, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("hinderancesList")
    context = {"hinderance": obj}
    return render(request, "tasks/hinderancesDeleteView.html", context)


def hinderanceFollowUpList(request, id):
    hinderance = get_object_or_404(Hinderances, id=id)
    hinderanceFollowUps = HinderanceFollowUp.objects.filter(hinderance=hinderance)
    context = {
        "hinderanceFollowUp": hinderanceFollowUps,
        "hinderance": hinderance,
        "id": id
    }
    return render(request, 'tasks/hinderanceFollowUpList.html', context)

def documentDownloadView(request, id):
    document = get_object_or_404(HinderanceFollowUp, id=id)
    response = FileResponse(document.document.open(), as_attachment=True, filename=document.document.name)
    return response

def hinderanceFollowUpCreateView(request, id):
    hinderance = get_object_or_404(Hinderances, id=id)
    if request.method == "POST":
        form = HinderanceFollowUpForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            hinderanceFollowUp = form.save(commit=False)
            hinderanceFollowUp.hinderance = hinderance
            hinderanceFollowUp.save()
            return redirect("hinderanceFollowUpList", id=id)
    else:
        form = HinderanceFollowUpForm()
    return render(request, "tasks/hinderanceFollowUpCreateView.html", {
        "form": form,
        "hinderance": hinderance,
        "id": id
    })

def hinderanceFollowUpUpdateView(request, id):
    obj = get_object_or_404(HinderanceFollowUp, id=id)
    hinderance_id = obj.hinderance.id
    hinderance = obj.hinderance
    form = HinderanceFollowUpForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("hinderanceFollowUpList", id=hinderance_id)
    return render(request, "tasks/hinderanceFollowUpUpdateView.html", {
        "form": form,
        "hinderance": hinderance,
        "id": hinderance_id
    })

def hinderanceFollowUpDeleteView(request, id):
    obj = get_object_or_404(HinderanceFollowUp, id=id)
    hinderance_id = obj.hinderance.id
    hinderance = obj.hinderance
    if request.method == "POST":
        obj.delete()
        return redirect("hinderanceFollowUpList", id=hinderance_id)
    return render(request, "tasks/hinderanceFollowUpDeleteView.html", {
        "hinderanceFollowUp": obj,
        "hinderance": hinderance
    })




