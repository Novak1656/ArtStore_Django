from django.shortcuts import render


def main(request):
    user = request.user
    return render(request, 'shop/base_shop.html', {'user': user})
