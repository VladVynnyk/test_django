from .models import Product


def searchProducts(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    products = Product.objects.all()

    return products, search_query
