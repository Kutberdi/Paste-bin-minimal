from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Paste
from .forms import PasteForm

def create_paste(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save()
            return redirect('view_paste', paste_id=paste.id)
    else:
        form = PasteForm()
    return render(request, 'paste/create_paste.html', {'form': form})

def view_paste(request, paste_id):
    paste = Paste.objects.get(id=paste_id)
    return render(request, 'paste/view_paste.html', {'paste': paste})


from django.shortcuts import get_object_or_404, redirect
from .models import Paste

def delete_paste(request, paste_id):
    paste = get_object_or_404(Paste, id=paste_id)
    paste.delete()
    return redirect('create_paste')
