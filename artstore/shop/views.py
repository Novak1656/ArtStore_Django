from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView
from galery.models import Art, Genre, Gallery
from authentication.models import User
from .models import Basket


class Shop(LoginRequiredMixin, ListView):
    paginate_by = 6
    template_name = 'shop/shop.html'
    context_object_name = 'arts'
    login_url = 'login'

    def get_queryset(self):
        if self.request.GET.get('author_name') and self.request.GET.get('genre_name'):
            return Art.objects.filter(Q(author__username=self.request.GET.get('author_name')) &
                                      Q(genre__title=self.request.GET.get('genre_name')))\
                .select_related("author", "genre").all()
        elif self.request.GET.get('author_name'):
            return Art.objects.filter(author__username=self.request.GET.get('author_name'))\
                .select_related("author", "genre").all()
        elif self.request.GET.get('genre_name'):
            return Art.objects.filter(genre__title=self.request.GET.get('genre_name'))\
                .select_related("author", "genre").all()
        return Art.objects.select_related("author", "genre").all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('page'):
            context['page'] = f"page={self.request.GET.get('page')}"
        if self.request.GET.get('author_name'):
            context['author_name'] = f"author_name={self.request.GET.get('author_name')}&"
        if self.request.GET.get('genre_name'):
            context['genre_name'] = f"genre_name={self.request.GET.get('genre_name')}&"
        return context


class BasketView(LoginRequiredMixin, ListView):
    queryset = Basket
    template_name = 'shop/basket.html'
    context_object_name = 'arts'
    login_url = 'login'

    def get_queryset(self):
        return self.request.user.basket_user.select_related("art_id", "user_id").all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum_prise'] = sum([elm.art_id.prise for elm in self.get_queryset()])
        return context


class Search(LoginRequiredMixin, ListView):
    template_name = 'shop/search.html'
    context_object_name = 'arts'
    login_url = 'login'
    paginate_by = 6

    def get_queryset(self):
        return Art.objects.filter(title__icontains=self.request.GET.get('search_word'))\
            .select_related("author", "genre").all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.request.GET.get('search_word')
        if self.request.GET.get('page'):
            context['page'] = f"page={self.request.GET.get('page')}"
        context['search_word'] = f"search_word={self.request.GET.get('search_word')}&"
        return context


class GenresPage(LoginRequiredMixin, ListView):
    template_name = 'shop/genre_section.html'
    model = Genre
    context_object_name = 'genres'
    login_url = 'login'


class AuthorsPage(LoginRequiredMixin, ListView):
    template_name = 'shop/author_section.html'
    context_object_name = 'authors'
    login_url = 'login'

    def get_queryset(self):
        if self.request.GET.get('author_name'):
            return User.objects.filter(Q(roles='Автор') &
                                       Q(username__icontains=self.request.GET.get('author_name'))).all()
        return User.objects.filter(roles='Автор').all()


@login_required
def add_in_basket(request, pk):
    art = Art.objects.get(pk=pk)
    Basket.objects.create(art_id=art, user_id=request.user, prise=art.prise)
    args = {}
    view_name = 'main'
    if request.GET.get('search_word'):
        args['search_word'] = request.GET.get('search_word')
        view_name = 'search'
    if request.GET.get('page'):
        args['page'] = request.GET.get('page')
    if request.GET.get('author_name'):
        args['author_name'] = request.GET.get('author_name')
    if request.GET.get('genre_name'):
        args['genre_name'] = request.GET.get('genre_name')
    return redirect('{}?{}'.format(reverse(view_name), urlencode(args)))


@login_required
def delete_basket_art(request, pk):
    art = Basket.objects.get(pk=pk)
    art.delete()
    return redirect('basket')


@login_required
def buy_arts(request):
    arts = Art.objects.filter(basket_art__user_id__id=request.user.id).all()

    for art in arts:
        gallery = Gallery(user=request.user, art_title=art.title,
                          genre=art.genre.title, author=art.author.username)

        with open(art.art.path, 'rb') as f:
            image_file = File(f)
            file_name = art.art.name.split('/')[-1]
            gallery.art.save(file_name, image_file, True)
            gallery.save()

        request.user.basket_user.filter(art_id__id=art.id).delete()
    return redirect('gallery')
