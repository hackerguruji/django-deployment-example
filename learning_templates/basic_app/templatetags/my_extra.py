from django import template

register =  template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the String!
    """
    return vlaue.cut(arg,'')

# register.filter('cut',cut)
