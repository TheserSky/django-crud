from django.forms import ModelForm
from .models import Tasks
class taskForm (ModelForm):
    class Meta: 
        model  = Tasks
        fields = ['title','description','important']