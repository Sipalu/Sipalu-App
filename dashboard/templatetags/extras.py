<<<<<<< HEAD
from  django import template


register=template.Library()
@register.filter(name='get_val')
def get_val(dict,key):
=======
from  django import template


register=template.Library()
@register.filter(name='get_val')
def get_val(dict,key):
>>>>>>> 550c397da82c84627a5a585ea40baaaeb7077ad9
    return dict.get(key)