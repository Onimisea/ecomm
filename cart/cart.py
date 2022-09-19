

class Cart():
    """
      A base Cart class, providing some default behaviors that can be inheited or overrided, as necessary.

    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, item):
        """ Adding and updating the users basket session data """
        item_id = item.id

        if item_id not in self.cart:
            self.cart[item_id] = {'price': str(item.price)}

        self.session.modified = True
