from django.shortcuts import get_object_or_404, render, redirect
from .models import Document, Folder
from .forms import DocumentForm, FolderForm
from django.http import FileResponse

# Create your views here.
def folderList(request):
    folders = Folder.objects.select_related('parentFolder').all()

    context = {"folders": folders}
    return render(request, "docs/folderList.html", context)

def folderCreateView(request, parent_id=None):
    parent_folder = None
    if parent_id:
        parent_folder = get_object_or_404(Folder, id=parent_id)
    
    form = FolderForm(request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        return redirect("/docs/folderList")
    
    context = {"form": form, "parent_folder": parent_folder}
    return render(request, "docs/folderCreateView.html", context)

def folderUpdateView(request, id):
    obj = get_object_or_404(Folder, id=id)
    form = FolderForm(request.POST or None, instance=obj, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('folderList')
    
    context = {"form": form, "parent_folder": obj.parentFolder}
    return render(request, "docs/folderUpdateView.html", context)

def folderDeleteView(request, id):
    context2 = {} 
    obj = get_object_or_404(Folder, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/docs/folderList")
    return render(request, "docs/folderDeleteView.html", context2)

def documentList(request, id):
    folder = get_object_or_404(Folder, id=id)
    documents = Document.objects.filter(folder=folder)

    context = {"documents": documents, "folder": folder}
    return render(request, "docs/documentList.html", context)

def documentsDownloadsView(request, id):
    document = get_object_or_404(Document, id=id)
    response = FileResponse(document.file.open(), as_attachment=True, filename=document.file.name)
    return response

def documentCreateView(request, id):
    folder = get_object_or_404(Folder, id=id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            document = form.save(commit=False)
            document.folder = folder
            document.save()
            return redirect('documentList', id=id)
    else:
        form = DocumentForm()
    
    context = {"form": form, "folder": folder}
    return render(request, 'docs/documentCreateView.html', context)

def documentUpdateView(request, id):
    document = get_object_or_404(Document, id=id)
    folder = document.folder
    form = DocumentForm(request.POST or None, request.FILES or None, instance=document, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('documentList', id=folder.id)
    
    context = {"form": form, "folder": folder}
    return render(request, "docs/documentUpdateView.html", context)

def documentDeleteView(request, id):
    document = get_object_or_404(Document, id=id)
    if request.method == "POST":
        document.delete()
        return redirect('documentList', id=document.folder.id)
    return redirect('documentList', id=document.folder.id)
