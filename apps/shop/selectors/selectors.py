from ..models import Product

def product_list_fetch(category, search):
    queryset = Product.objects.all()
    if category:
        queryset = queryset.filter(categories__name=category)
    if search:
        queryset = queryset.filter(name__icontains=search) | queryset.filter(description__icontains=search)
    return queryset
