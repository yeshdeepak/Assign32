import django_filters

from .models import *

class propertyfilter(django_filters.FilterSet):
    class Meta:
        model=Properties
        fields = ('County','Property_Guest_Capacity')
        labels= {'County': 'AnyWhere',
                 'Property_Guest_Capacity':'Adult',
                 'Property_Guest_Capacity': 'Children'

                 }

