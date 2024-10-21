from django.shortcuts import render, redirect
from .models import BugReport, Project
from .forms import BugReportForm

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'reports/bug_list.html', {'bugs': bugs})

def bug_detail(request, pk):
    bug = BugReport.objects.get(pk=pk)
    return render(request, 'reports/bug_detail.html', {'bug': bug})

def new_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.created_by = request.user
            bug.save()
            return redirect('bug_list')
    else:
        form = BugReportForm()
    return render(request, 'reports/new_bug.html', {'form': form})
