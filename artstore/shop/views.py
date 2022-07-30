from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.shortcuts import redirect
from django.views.generic import ListView
from galery.models import Art, Genre, Gallery
from .models import Basket


class Shop(LoginRequiredMixin, ListView):
    model = Art
    paginate_by = 1
    template_name = 'shop/shop.html'
    context_object_name = 'arts'
    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['basket_list'] = [elm.art_id.id for elm in self.request.user.basket_user.all()]
        return context


class BasketView(LoginRequiredMixin, ListView):
    queryset = Basket
    template_name = 'shop/basket.html'
    context_object_name = 'arts'
    login_url = 'login'

    def get_queryset(self):
        return self.request.user.basket_user.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum_prise'] = sum([elm.art_id.prise for elm in self.get_queryset()])
        return context


@login_required
def add_in_basket(request, pk):
    art = Art.objects.get(pk=pk)
    Basket.objects.create(art_id=art, user_id=request.user, prise=art.prise)
    return redirect('main')


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
