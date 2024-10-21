from django.shortcuts import get_object_or_404, render, redirect,HttpResponse
from django.contrib import messages
from .models import Document, Folder
from .forms import DocumentForm, FolderForm
from django.http import FileResponse

# Create your views here.
def folderList(request):
    folders = Folder.objects.select_related('parentFolder').all().order_by('name')

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

def toggle_protection(request):
    if request.method == "POST":
        folder_id = request.GET.get("folder_id")
        password = request.POST.get("password")

        folder = get_object_or_404(Folder, id=folder_id)
        
        # Toggle protection status and save the password
        if folder.protected:
            # Unlock folder
            folder.protected = False
            folder.password = None  # Clear password on unlock
        else:
            # Lock folder
            folder.protected = True
            folder.password = password  # Set password on lock

        folder.save()
        return redirect('folderList')
    
    return HttpResponse(status=400)

def documentList(request, id):
    folder = get_object_or_404(Folder, id=id)

    # Check if the folder is protected
    if folder.protected:
        # Check if the correct password is already stored in the session
        if not request.session.get(f'unlocked_folder_{folder.id}'):
            if request.method == "POST":
                entered_password = request.POST.get("password")
                if folder.password == entered_password:
                    # Store folder unlocked status in session
                    request.session[f'unlocked_folder_{folder.id}'] = True
                    return redirect('documentList', id=folder.id)
                else:
                    messages.error(request, "Password doesn't match.")
            return render(request, 'docs/folder_password.html', {"folder": folder})

    # If folder is not protected or already unlocked, show the document list
    documents = Document.objects.filter(folder=folder).order_by('name')
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
