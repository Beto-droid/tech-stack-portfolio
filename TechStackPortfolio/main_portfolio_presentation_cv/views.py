from django.shortcuts import render, redirect
from .models import CVEntry
from .forms import CVEntryForm

def cv_list(request):
    entries = CVEntry.objects.all()
    return render(request, 'main_portfolio_presentation_cv/cv_list.html', {'entries': entries})

def cv_add(request):
    if request.method == 'POST':
        form = CVEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cv_list')
    else:
        form = CVEntryForm()
    return render(request, 'main_portfolio_presentation_cv/cv_add.html', {'form': form})