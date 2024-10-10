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
    dci = DCI.objects.all()
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


def copyDci(request, id):
   
    dci = get_object_or_404(DCI, id=id)
    dci_groups = DCIGroup.objects.filter(dci=dci)
    dci_items = DCIItem.objects.filter(dciGroup__in=dci_groups)

    new_dci = DCI.objects.create(
        name=f"Copy of {dci.name}",  
        # project=dci.project,          
    )

    for group in dci_groups:
        new_group = DCIGroup.objects.create(
            name=group.name,    
            groupCode=group.groupCode,       
            dci=new_dci                      
        )
        
   
        for item in dci_items.filter(dciGroup=group):
            DCIItem.objects.create(
                name=item.name,  
                sNo=item.sNo,                 
                dciGroup=new_group,      
                itemCode=item.itemCode,
                documentNo=item.documentNo,
                description=item.description,
                likelySubmissionDate=item.likelySubmissionDate,
                weightage=item.weightage,
                associatedCost=item.associatedCost,
            )

    return redirect("/dci/dciList")



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
        form = DCIGroupForm(request.POST, request.FILES, parent_dci=dci)
        if form.is_valid():
            dci_group = form.save(commit=False)
            dci_group.dci = dci  # Set the DCI directly
            dci_group.save()
            return redirect("dciOfDciGroup", id=id)
    else:
        form = DCIGroupForm(parent_dci=dci)
    
    context["form"] = form
    context["id"] = id  # Pass the DCI ID to the template
    context["dci_name"] = dci.name  # Pass the DCI name to the template
    
    return render(request, "dci/dciGroupCreateView.html", context)



def dciGroupUpdateView(request, id):
    obj = get_object_or_404(DCIGroup, id=id)
    dci = obj.dci
    context1 = {"dci": dci}
    
    form = DCIGroupForm(request.POST or None, request.FILES or None, instance=obj, parent_dci=dci)

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
                if len(row) >= 4:  # Ensure the row has at least 4 elements
                    DCIItem.objects.create(
                        sNo=row[0],
                        itemCode=row[1],
                        name=row[2],
                        documentNo=row[3],
                        dciGroup=dciGroup
                    )
                else:
                    # Handle rows that don't have enough columns
                    messages.error(request, f"Row {row[0]} does not have enough columns.")

            dciItems = DCIItem.objects.filter(dciGroup=dciGroup)

    else:
        upload_form = ExcelUploadForm()

    context = {
        "dciGroup": dciGroup,
        "dciItems": dciItems,
        "upload_form": upload_form,
    }
    return render(request, "dci/dciItemList.html", context)


def dciItemCreateView(request, id):
    dci_group = get_object_or_404(DCIGroup, id=id)
    
    if request.method == "POST":
        form = DCIItemForm(request.POST or None, request.FILES or None, user=request.user, dci_group=dci_group)
        if form.is_valid():
            form.save()
            return redirect("dciItemList", id=id)
    else:
        form = DCIItemForm(dci_group=dci_group)

    context = {
        "form": form,
        "dciGroup": dci_group,
    }

    return render(request, "dci/dciItemCreateView.html", context)





def dciItemUpdateView(request, id):
    obj = get_object_or_404(DCIItem, id=id)
    dci_group = obj.dciGroup

    form = DCIItemForm(request.POST or None, request.FILES or None, instance=obj, user=request.user, dci_group=dci_group)

    if form.is_valid():
        form.save()
        return redirect("dciItemList", id=dci_group.id)

    context = {
        "form": form,
        "parent_name": dci_group.name,
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


# views.py
def dci_groups_and_items(request, dci_id):
    dci = get_object_or_404(DCI, pk=dci_id)
    
    # Get the groups and items related to the DCI
    dci_groups = DCIGroup.objects.filter(dci=dci)  # Assuming DCIGroup has a ForeignKey to DCI
    dci_items = DCIItem.objects.filter(dciGroup__dci=dci)  # Assuming DCIItem has a ForeignKey to DCIGroup

    # Zip the two querysets together
    groups_and_items = zip(dci_groups, dci_items)
    
    return render(request, 'dci/dci_groups_items.html', {
        'dci': dci,
        'groups_and_items': groups_and_items,  # Pass the zipped data to the template
    })




