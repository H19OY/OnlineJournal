from django.shortcuts import render, redirect
from .models import JournalEntry
from .forms import JournalEntryForm

def create_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = JournalEntryForm()
    return render(request, 'journal/create_entry.html', {'form': form})

def entry_list(request):
    entries = JournalEntry.objects.all().order_by('-date', '-time')
    return render(request, 'journal/entry_list.html', {'entries': entries})
