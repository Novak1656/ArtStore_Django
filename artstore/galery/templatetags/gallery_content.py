from django import template

register = template.Library()


@register.inclusion_tag('gallery/gallery_content.html')
def get_author_arts(user):
    arts = user.art.all()
    return {'arts': arts}
