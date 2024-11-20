from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from .models import Tasks, TaskActivities, Hinderances, HinderanceFollowUp, Project, DCIItem, DCIGroup
from .forms import (
    TasksForm,
    TaskActivitiesForm,
    HinderancesForm,
    HinderanceFollowUpForm,
)

from django.http import FileResponse, HttpResponse
from django.template.loader import render_to_string


def tasksList(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project=project).order_by('taskName')

    context = {
        'tasks': tasks,
        'project': project,
        'id': id
    }
    return render(request, "tasks/tasksList.html", context)



def tasksCreateView(request, id):
    project = get_object_or_404(Project, id=id)
    
    # Assuming project.finalDCI is a DCI instance
    dci_groups = DCIGroup.objects.filter(dci=project.finalDCI)  # Get all DCI Groups related to the DCI
    dci_items = DCIItem.objects.filter(dciGroup__in=dci_groups)  # Corrected: use dciGroup

    form = TasksForm(request.POST or None, project=project)
    
    if form.is_valid():
        tasks = form.save(commit=False)
        tasks.project = project  # Ensure project is set
        tasks.save()

        # Now save the selected DCI items
        form.save_m2m()  # This line saves the many-to-many relationship
        
        return redirect("tasksList", id=id)
    
    context = {
        "form": form,
        "id": id,
        "project": project,
        "dci_items": dci_items,  # Pass the filtered DCI Items to the template if needed
    }

    return render(request, "tasks/tasksCreateView.html", context)


def tasksUpdateView(request, id):
    obj = get_object_or_404(Tasks, id=id)  # Fetch the task based on id
    project = obj.project  # Get the project from the task
    task = get_object_or_404(Tasks, id=id)

    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # Redirect to your tasks list page or wherever needed
            return redirect("tasksList", id=project.id) 
    else:
        form = TasksForm(instance=task)

    # Assuming you want to get the DCIItems associated with the task
    dci_groups = DCIGroup.objects.filter(dci=task.project.finalDCI)
    dci_items = DCIItem.objects.filter(dciGroup__in=dci_groups)

    context = {
        'form': form,
        'task': task,
        'dci_items': dci_items,  # Pass DCI items to the template if needed
        'project': project
    }
    return render(request, "tasks/tasksUpdateView.html", context)


def tasksDeleteView(request, id):

    context2 = {}

    obj = get_object_or_404(Tasks, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/tasks/tasksList")
    return render(request, "tasks/tasksDeleteView.html", context2)

def task_detail_view(request, pk):
    # Fetch the task by ID
    task = get_object_or_404(Tasks, id=pk)

    # Fetch related DCI Items and Task Activities
    dci_items = task.dciItem.all()
    task_activities = TaskActivities.objects.filter(task=task)

    context = {
        'task': task,
        'dci_items': dci_items,
        'task_activities': task_activities,
    }
    return render(request, 'tasks/task_detail.html', context)


def load_task_activities(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task_activities = TaskActivities.objects.filter(task=task)
    return render(request, 'tasks/task_activities_partial.html', {'task_activities': task_activities, 'task': task})

def task_dci_item_view(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    dci_items = task.dciItem.all()  # Assuming dciItem is a ManyToManyField or ForeignKey
    
    context = {
        'task': task,
        'dci_items': dci_items,
    }
    return render(request, 'tasks/task_dci_items.html', context)
def taskActivitiesList(request, id):
    task = get_object_or_404(Tasks, id=id)
    taskActivities = TaskActivities.objects.filter(task_id=id).order_by('dateOfEntry')
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
        form = TaskActivitiesForm(request.POST, request.FILES, user=request.user, task_instance=task)
        if form.is_valid():
            task_activity = form.save(commit=False)
            task_activity.task = task  # Set the task explicitly
            task_activity.save()
            return redirect("tasksList", id=id)

    else:
        form = TaskActivitiesForm(user=request.user, task_instance=task)

    return render(request, "tasks/taskActivitiesCreateView.html", {"form": form, "task": task})


def taskActivitiesUpdateView(request, id):
    task_activity = get_object_or_404(TaskActivities, id=id)
    task = task_activity.task  # Get the associated task for the activity
    
    if request.method == "POST":
        form = TaskActivitiesForm(request.POST, instance=task_activity)
        if form.is_valid():
            form.save()
            return redirect("tasksList", id=task.id)  # Redirect to the task list page

    else:
        form = TaskActivitiesForm(instance=task_activity)

    return render(request, 'tasks/taskActivitiesUpdateView.html', {
        'form': form,
        'task_activity': task_activity,
        'task': task  # Make sure task is passed to the template
    })




def taskActivitiesDeleteView(request, id):
    task_activity = get_object_or_404(TaskActivities, id=id)
    task = task_activity.task
    if request.method == "POST":
        task_activity.delete()
        return redirect("tasksList", id=task.id)
    context = {"task_activity": task_activity, "task": task}
    return render(request, "tasks/taskActivitiesDeleteView.html", context)

def hinderancesList(request):
    hinderances = Hinderances.objects.all().order_by('dciItem')  # Ascending order by 'dciItem'
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
    hinderanceFollowUps = HinderanceFollowUp.objects.filter(hinderance=hinderance).order_by('followUpDate')
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
        form = HinderanceFollowUpForm(request.POST, request.FILES)
        if form.is_valid():
            hinderanceFollowUp = form.save(commit=False)
            hinderanceFollowUp.hinderance = hinderance
            hinderanceFollowUp.save()

            if request.headers.get('HX-Request'):
                # Return only the table row that was updated
                hinderanceFollowUpList = HinderanceFollowUp.objects.filter(hinderance=hinderance)
                return render(request, "tasks/hinderanceFollowUpTablePartial.html", {"hinderanceFollowUp": hinderanceFollowUpList, "hinderance": hinderance})
            return redirect("hinderanceFollowUpList", id=id)
    else:
        form = HinderanceFollowUpForm()

    if request.headers.get('HX-Request'):
        return render(request, "tasks/hinderanceFollowUpFormPartial.html", {"form": form, "hinderance": hinderance})

def hinderanceFollowUpUpdateView(request, id):
    obj = get_object_or_404(HinderanceFollowUp, id=id)
    hinderance = obj.hinderance
    form = HinderanceFollowUpForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()

        if request.headers.get('HX-Request'):
            hinderanceFollowUpList = HinderanceFollowUp.objects.filter(hinderance=hinderance)
            return render(request, "tasks/hinderanceFollowUpTablePartial.html", {"hinderanceFollowUp": hinderanceFollowUpList, "hinderance": hinderance})
        return redirect("hinderanceFollowUpList", id=hinderance.id)

    if request.headers.get('HX-Request'):
        return render(request, "tasks/hinderanceFollowUpFormPartial.html", {"form": form, "hinderance": hinderance})




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




