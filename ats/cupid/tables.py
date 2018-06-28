import django_tables2 as tables
from django_tables2.utils import A
from .models import jobd

class jdTable(tables.Table):
    jd_id=tables.LinkColumn('results', args =[A('pk')])
    class Meta:
        model = jobd
        template_name = 'django_tables2/bootstrap.html'