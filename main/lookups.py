from ajax_select import register, LookupChannel
from home.models import RuralDistrict

@register('eldimeken')
class FamilyLookup(LookupChannel):

    model = RuralDistrict

    def get_query(self, pk, request):
        return self.model.objects.filter(id=pk)

    def format_item_display(self, item):
        return u"<select name='eldimeken' id='id_eldimeken'><option value="">---------</option></select>" % item.name
    
    
    


