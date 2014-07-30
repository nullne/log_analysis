from django import forms
from view.models import  LogAnalysis, Document
from django.contrib.admin import widgets

class LogAnalysisForm(forms.ModelForm):
    docfile = forms.FileField(
            label="Select the log file",
            help_text="Log file"
            )
    name = forms.CharField(max_length=255, help_text="Analysis Name")
    project = forms.CharField(max_length=128, help_text="Project name")
    start_date = forms.DateField(help_text="Start Date")
    end_date = forms.DateField(help_text="End Date")
    class Meta:
        model = LogAnalysis
        fields = ('name', 'project', 'start_date', 'end_date')
    def __init__(self, *args, **kwargs):
        super(LogAnalysisForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widgets = widgets.AdminDateWidget()

