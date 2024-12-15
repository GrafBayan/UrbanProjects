from django.shortcuts import render

def main(request):
    title = 'Онлайн магазин настолок'
    text1 = ('Мы любим вас и ненавидим, как друзей, покупайте же у нас настолки для себя и своих друзей (с нами '
             'поиграть тоже можно)')
    context = {
        'title': title,
        'text1': text1,
    }
    return render(request, 'fourth_task/main_page.html', context)

def shop(request):
    games = ["Bullet", "Feet The Kraken", "The East Indian Campaign"]

    if request.method == "POST":
        game_name = request.POST.get('game_name')

        if 'cart' not in request.session:
            request.session['cart'] = {}

        if game_name in request.session['cart']:
            request.session['cart'][game_name] += 1
        else:
            request.session['cart'][game_name] = 1

        request.session.modified = True

    context = {
        'games': games,
        'cart_items': request.session.get('cart', {}),
    }
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    cart_items = request.session.get('cart', {})
    return render(request, 'fourth_task/cart.html', {'cart_items': cart_items})