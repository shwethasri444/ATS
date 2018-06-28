import django_tables2 as tables
from django_tables2.utils import A
from .models import jobd
from cupid import views
class jdTable(tables.Table):
		jd_id = tables.LinkColumn('results',text='Search')
			# text="static text", args=[A('pk')])
    class Meta:
    	# fields= ['ID','JD_ID','COMPANY','FIELD','DESIGNATION','SKILLS','EDUCATION','EXPERIENCE','SEARCH']
        model = jobd
        # attrs = {"class":"paleblue"}
        template_name = 'django_tables2/bootstrap.html'