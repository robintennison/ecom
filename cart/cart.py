from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')  # 'cart' is stored in the session
        if not cart:
            cart = self.session['cart'] = {}  # Initialize an empty cart
        self.cart = cart


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += product_qty  # Add to existing quantity
        else:
            self.cart[product_id] = {'quantity': product_qty}  # New entry

        self.session.modified = True

    
    def __len__(self):
        total_qty = 0
        for item in self.cart.values():
            if isinstance(item, dict):
                total_qty += item.get('quantity', 0)
            else:
                total_qty += int(item)  # fallback for old int-only data
        return total_qty