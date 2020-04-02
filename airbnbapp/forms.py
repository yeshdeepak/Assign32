from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Properties,Property_Availability,Property_Status



class PropertiesForm(forms.ModelForm):

    class Meta:
        model=Properties
        fields = ('Property_Name','Property_Description','Property_Guest_Capacity','Property_Street','Property_City','Property_State','Price','No_of_Rooms',
                  'No_of_Bathrooms','Total_Area','Garage_Capacity','No_of_Floors','Available_Areas','Property_Host','Property_Image','County','Adults','Children')
        labels= {'Property_Name': 'Property Name',
                 'Property_Description':'Description',
                 'Property_Guest_Capacity': 'Guests',
                'Property_Street': 'Street',
                'Property_City':'City',
                'Property_State': 'State',
                'Price':'Price',
                 'No_of_Rooms':'Rooms',
                 'No_of_Bathrooms':'Bathrooms',
                 'Total_Area': 'Total Area',
                 'Garage_Capacity': 'Garage',
                 'No_of_Floors': 'Floors',
                 'Available_Areas': 'Avilable Area',
                 'Property_Host': 'Host',
                 'Property_Image': 'Photo',
                  'County': 'County',
                    'Aduts':'Adults',
                'Children':'Children'
        }

    def __init__(self, *args, **kwargs):
        super(PropertiesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(

            'Property_Image',
            HTML(
                """{% if form.Property_Image.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.Property_Image.value }}">{% endif %}""", ),
            'flag_featured',
        )

class AddMaintenanceForm(forms.ModelForm):
  class Meta:

    model = Property_Status
    fields = ('Property_Name',  'Property_Status_Description', 'Expenses',
              'Maintenance_ID')
    labels = {'Property_Name': 'Property Name',
              'Property_Status_Description': 'Description',
              'Expenses': 'Maintenance Charges',
              'Maintenance_ID': 'Maintenance Staff',

              }




