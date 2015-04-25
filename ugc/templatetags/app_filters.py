from django import template

register = template.Library()

'''Defines a custom register to return only those messages
	that are of that particular source'''
@register.filter
def from_source(messages, source):
	return messages.filter(source_id=source)


