from django import template
from django.core.cache import cache
from galery.models import Genre
register = template.Library()


@register.inclusion_tag('shop/genre_list.html')
def get_genres(author_name):
    genres = cache.get('genres')
    if not genres:
        genres = Genre.objects.all()
        cache.set('genres', genres, 300)
    data = {'genres': genres}
    if author_name:
        data['author_name'] = author_name
    return data


@register.simple_tag()
def get_basket_info(user):
    return [elm.art_id.id for elm in user.basket_user.all()]
