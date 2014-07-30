from django.shortcuts import render, render_to_response
from django.template import RequestContext
from view.forms import LogAnalysisForm
# Create your views here.

def showSVG(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('admin/views/svg.html', context_dict, context)
def upload(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = LogAnalysisForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = LogAnalysisForm()

    return render_to_response('view/upload.html', {'form': form}, context)

