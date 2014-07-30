from django.conf.urls import patterns, url
from django.contrib import admin
from view.models import LogAnalysis, Entry
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
import pygal
from view.forms import LogAnalysisForm
import os
from django.conf import settings

def compareURL(modeladmin, request, queryset):
    pass
compareURL.short_description = 'Compared by URL, show in SVG '

def comparePage(modeladmin, request, queryset):
    pass
comparePage.short_description = 'Compared by page, show in SVG'

def showSVG(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/admin/view/loganalysis/svg/?ids=%s" % (",".join(selected)))
showSVG.short_description = 'compare results graphically'
def showNiceSVG(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/admin/view/entry/svg/?ids=%s" % (",".join(selected)))
showNiceSVG.short_description = 'compare results in bar'
def showPie(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/admin/view/entry/pie/?ids=%s" % (",".join(selected)))
showPie.short_description = 'compare results in Pie'

class LogAnalysisAdmin(admin.ModelAdmin):
    list_display = ('project','details_link', 'start_time', 'end_time', 'manipulate_time')
    search_fields = ['name', 'project']
    list_filter = ['project']
    actions = [showSVG]

    def details_link(self, obj):
        return u'<a href="/admin/view/entry?logAnalysis__id=%s">%s<a/>' % (obj.id, obj)
    details_link.allow_tags = True
    details_link.short_description = 'name'

    def upload(self, request):
        context = RequestContext(request)
        project_instance = LogAnalysis.objects.values('project').distinct()
        project = [c['project'] for c in project_instance]


        if request.method == 'POST':

            name = request.POST['name']
            project = request.POST['project']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']

            form = LogAnalysisForm(request.POST, request.FILES)
            file = request.FILES['docfile']
            filename = file.name
            upload_path = os.path.join(settings.MEDIA_ROOT, 'log/')
            #while  os.path.exists(os.path.join(upload_path, filename)):
            filename = 'good.log'
            dest = open(os.path.join(upload_path, filename), 'wb')
            for chunk in file.chunks():
                dest.write(chunk)
            dest.close()

            try:

                pass
            finally:
                pass

            return HttpResponseRedirect('/admin/view/loganalysis/upload')

        else:
            form = LogAnalysisForm()

        return render_to_response('admin/view/upload.html', {'form': form, 'project': project}, context)
    def show(self,request):
        showids = request.GET['ids'].split(',')
        images = []
        record = {}
        for showid in showids:
            p = Entry.objects.filter(logAnalysis=showid, entry_type='url')
            q = LogAnalysis.objects.get(pk=showid)
            record[q.name] = {'name':[], 'times':[], 'micros':[], 'average':[]} 
            for a in p:
                record[q.name]['times'].append(a.times)
                record[q.name]['average'].append(a.average)
                record[q.name]['micros'].append(a.micros)
                record[q.name]['name'].append(a.name)
        bar_times = pygal.Bar()
        bar_times.title = 'url times'
        bar_times.x_labels = map(str, record[q.name]['name'])
        bar_micros = pygal.Bar()
        bar_micros.title = 'url micros'
        bar_micros.x_labels = map(str, record[q.name]['name'])
        bar_average = pygal.Bar()
        bar_average.title = 'url average'
        bar_average.x_labels = map(str, record[q.name]['name'])
        for r in record:
            bar_times.add(r, record[r]['times'])
            bar_micros.add(r, record[r]['micros'])
            bar_average.add(r, record[r]['average'])
        bar_times.render_to_file('./static/url_times.svg')
        bar_micros.render_to_file('./static/url_micros.svg')
        bar_average.render_to_file('./static/url_average.svg')
        for showid in showids:
            p = Entry.objects.filter(logAnalysis=showid, entry_type='page')
            q = LogAnalysis.objects.get(pk=showid)
            record[q.name] = {'name':[], 'times':[], 'micros':[], 'average':[]} 
            for a in p:
                record[q.name]['times'].append(a.times)
                record[q.name]['average'].append(a.average)
                record[q.name]['micros'].append(a.micros)
                record[q.name]['name'].append(a.name)
        bar_times = pygal.Bar()
        bar_times.title = 'page times'
        bar_times.x_labels = map(str, record[q.name]['name'])
        bar_micros = pygal.Bar()
        bar_micros.title = 'page micros'
        bar_micros.x_labels = map(str, record[q.name]['name'])
        bar_average = pygal.Bar()
        bar_average.title = 'page average'
        bar_average.x_labels = map(str, record[q.name]['name'])
        for r in record:
            bar_times.add(r, record[r]['times'])
            bar_micros.add(r, record[r]['micros'])
            bar_average.add(r, record[r]['average'])
        bar_times.render_to_file('./static/page_times.svg')
        bar_micros.render_to_file('./static/page_micros.svg')
        bar_average.render_to_file('./static/page_average.svg')

        context = RequestContext(request)
        context_dict = {}
        return render_to_response('admin/view/svg.html', context_dict, context)
    def get_urls(self):
        urls = super(LogAnalysisAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^svg/$', self.show),
            (r'^upload/$', self.upload),
        )
        return my_urls + urls
    def __init__(self, *args, **kwargs):
        super(LogAnalysisAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )




class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'entry_type', 'average', 'micros', 'times', )
    search_fields = ['name']
    list_filter = ['entry_type', 'logAnalysis__name']
    actions = [showNiceSVG, showPie]

    def show(self,request):
        showids = request.GET['ids'].split(',')
        images = []
        record = {}
        name = []
        times = []
        micros =[]
        average = []
        for showid in showids:
            p = Entry.objects.get(pk=showid)
            r = p.logAnalysis.name
            name.append(p.name)
            times.append(p.times)
            average.append(p.average)
            micros.append(p.micros)
        bar_times = pygal.Bar()
        bar_times.title = 'times'
        bar_times.x_labels = map(str, name)
        bar_times.add(r, times)
        bar_times.render_to_file('./static/times.svg')

        bar_micros = pygal.Bar()
        bar_micros.title = 'micros'
        bar_micros.x_labels = map(str, name)
        bar_micros.add(r, micros)
        bar_micros.render_to_file('./static/micros.svg')

        bar_average = pygal.Bar()
        bar_average.title = 'average'
        bar_average.x_labels = map(str, name)
        bar_average.add(r, average)
        bar_average.render_to_file('./static/average.svg')

        context = RequestContext(request)
        context_dict = {}
        return render_to_response('admin/view/svg2.html', context_dict, context)
    def showPie(self, request):
        showids = request.GET['ids'].split(',')
        times = []
        average = []
        micros = []
        for showid in showids:
            p = Entry.objects.get(pk=showid)
            times.append([p.name,p.times])
            average.append([p.name,p.average])
            micros.append([p.name,p.micros])

        pie_average = pygal.Pie()
        pie_average.title = 'average'
        for t in average:
            pie_average.add(t[0], t[1])
        pie_average.render_to_file('./static/average.svg')

        pie_times = pygal.Pie()
        pie_times.title = 'times'
        for t in times:
            pie_times.add(t[0], t[1])
        pie_times.render_to_file('./static/times.svg')

        pie_micros = pygal.Pie()
        pie_micros.title = 'micros'
        for t in micros:
            pie_micros.add(t[0], t[1])
        pie_micros.render_to_file('./static/micros.svg')
        context = RequestContext(request)
        context_dict = {}
        return render_to_response('admin/view/svg3.html', context_dict, context)
    def get_urls(self):
        urls = super(EntryAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^svg/$', self.show),
            (r'^pie/$', self.showPie),
        )
        return my_urls + urls
    def __init__(self,*args,**kwargs):
        super(EntryAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )


admin.site.register(LogAnalysis, LogAnalysisAdmin)
admin.site.register(Entry, EntryAdmin)
#admin.site.disable_action('delete_selected')
