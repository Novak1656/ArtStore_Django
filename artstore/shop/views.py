from django.shortcuts import render


def main(request):
    return render(request, 'shop/base_shop.html')
