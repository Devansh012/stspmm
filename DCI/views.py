import openpyxl
import logging
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from django.contrib import messages
from .models import DCI, DCIGroup, DCIItem
from .forms import (
    DCIForm,
    DCIGroupForm,
    DCIItemForm,
    ExcelUploadForm
)


def dciList(request):
    dci = DCI.objects.select_related('project').all()
    context = {"dci": dci}
    return render(request, "dci/dciList.html", context)


def dciCreateView(request):
    context = {}

    form = DCIForm(request.POST or None, request.FILES or None)
    context["form"] = form
    if form.is_valid():
        form.save()
        return redirect("/dci/dciList")
    # else id==True:
    #     form.save()
    #     return redirect("/dci/dciOfDciGroup")
    
    return render(request, "dci/dciCreateView.html", context)

def dciUpdateView(request, id):
    context1 = {}
    obj = get_object_or_404(DCI, id=id)
    form = DCIForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/dci/dciList")

    context1["form"] = form

    return render(request, "dci/dciUpdateView.html", context1)

def dciDeleteView(request, id):

    # context2 = {}

    obj = get_object_or_404(DCI, id=id)

    if request.method == "POST":

        obj.delete()

        return HttpResponseRedirect("/dci/dciList")
    return render(request, "dci/dciList.html")


def dciOfDciGroup(request, id):
    dcigroup = DCIGroup.objects.filter(dci=id)
    dci = get_object_or_404(DCI, id=id)

    context = {"dciGroup": dcigroup, "id": id, "dci": dci}
    return render(request, "dci/dciOfDciGroup.html", context)


def dciGroupCreateView(request, id):
    context = {}
    
    # Fetch the DCI object
    dci = get_object_or_404(DCI, id=id)
    
    if request.method == "POST":
        form = DCIGroupForm(request.POST, request.FILES)
        if form.is_valid():
            dci_group = form.save()
            dci_group.dci_id = id  # Set the DCI ID
            dci_group.save()
            return redirect("dciOfDciGroup", id=id)
    else:
        form = DCIGroupForm()
    
    context["form"] = form
    context["id"] = id  # Pass the DCI ID to the template
    context["dci_name"] = dci.name  # Pass the DCI name to the template
    
    return render(request, "dci/dciGroupCreateView.html", context)


def dciGroupUpdateView(request, id):
    obj = get_object_or_404(DCIGroup, id=id)
    dci = obj.dci
    context1 = {"dci": dci}
    
    form = DCIGroupForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("dciOfDciGroup", id=dci.id)

    context1["form"] = form
    return render(request, "dci/dciGroupUpdateView.html", context1)


def dciGroupDeleteView(request, id):
    obj = get_object_or_404(DCIGroup, id=id)
    dci_id = obj.dci.id  # Store the DCI ID before deleting

    if request.method == "POST":
        obj.delete()
        return redirect("dciOfDciGroup", id=dci_id)  # Redirect to the DCI Group list for the specific DCI

    context = {"object": obj}
    return render(request, "dci/dciGroupDeleteView.html", context)



def dciItemList(request, id):
    dciGroup = get_object_or_404(DCIGroup, id=id)
    dciItems = DCIItem.objects.filter(dciGroup=dciGroup)
    
    if request.method == "POST":
        upload_form = ExcelUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            excel_file = request.FILES['excel_file']
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                DCIItem.objects.create(
                    sNo=row[0],
                    itemCode=row[1],
                    name=row[2],
                    documentNo=row[3],
                    description=row[4],
                    likelySubmissionDate=row[5],
                    weightage=row[6],
                    associatedCost=row[7],
                    dciGroup=dciGroup
                )
            dciItems = DCIItem.objects.filter(dciGroup=dciGroup)

    else:
        upload_form = ExcelUploadForm()

    context = {
        "dciGroup": dciGroup,  # Pass the parent DCIGroup to the template
        "dciItems": dciItems,
        "upload_form": upload_form,
    }
    return render(request, "dci/dciItemList.html", context)




def dciItemCreateView(request, id):
    dci_group = get_object_or_404(DCIGroup, id=id)
    context = {'dciGroup': dci_group}
    
    if request.method == "POST":
        form = DCIItemForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.dciGroup = dci_group  # Set the DCIGroup
            new_item.save()
            return redirect("dciItemList", id=id)
    else:
        form = DCIItemForm()
    
    context["form"] = form
    
    return render(request, "dci/dciItemCreateView.html", context)




def dciItemUpdateView(request, id):
    obj = get_object_or_404(DCIItem, id=id)
    dci_group = obj.dciGroup  # Get the associated DCIGroup instance

    form = DCIItemForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        form.save()
        # Redirect to the dciItemList with the correct group id
        return redirect(f"/dci/dciItemList{dci_group.id}/")

    context = {
        "form": form,
        "parent_name": dci_group.name  # Pass the DCIGroup name to the template
    }

    return render(request, "dci/dciItemUpdateView.html", context)


    
def dciItemDeleteView(request, id):
    obj = get_object_or_404(DCIItem, id=id)
    dci_group = obj.dciGroup

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(f"/dci/dciItemList{dci_group.id}/")
    
    context = {
        "dciItem": obj,
        "parent_name": dci_group.name  # Pass the DCIGroup name to the template
    }
    return render(request, "dci/dciItemDeleteView.html", context)





