from django import forms
from .models import Album
import datetime

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {'release_date': forms.DateInput(attrs={
                    'type': 'date', 
                    'value': datetime.date.today().strftime('%Y-%m-%d')
                }),
        }

        