def get_cart_length(request):
    return len(request.session.get('cart', []))
