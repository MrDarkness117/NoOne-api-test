import ast
import json
import requests
import pytest


@pytest.mark.skip
class TestAPI(object):

    access_token = None
    refresh_token = None
    expires_in = None

    # host = 'http://10.10.9.30:8080'
    host = 'http://crmdevpreprod.noone.ru:8080'
    login = 'm.romantsov@noone.ru'
    password = '123456'

    res = requests.post(
        '{}/app/rest/v2/oauth/token?grant_type=password&username={}&password={}'.format(host, login, password),
        headers={
            'Authorization': f'Basic Y2xpZW50OnNlY3JldA=='
        }).content.decode('utf-8')

    res_dict = ast.literal_eval(res)

    def __init__(self):
        pass

    def store_value(self):
        self.access_token = self.res_dict['access_token']
        self.refresh_token = self.res_dict['refresh_token']
        self.expires_in = self.res_dict['expires_in']

    def token_refresh(self):
        res = requests.post(
            self.host + '/app/rest/v2/oauth/token?grant_type=refresh_token&refresh_token={}'.format(self.refresh_token),
            headers={
                'Authorization': f'Basic Y2xpZW50OnNlY3JldA=='
            }).content.decode('utf-8')
        self.access_token = ast.literal_eval(res)['access_token']
        print(res)

    def get_cart(self, cart_id):
        res = requests.get(
            self.host + '/app/rest/v2/services/nl_ShoppingCartService/cartGet?cartId={}'.format(cart_id),
            headers={
                'Authorization': 'f\'Bearer {}\''.format(self.access_token)
            }
        ).content.decode('utf-8')
        print(res)
        assert True

    def create_cart(self, shopid):
        res = requests.get(
            self.host + '/app/rest/v2/services/nl_ShoppingCartService/cartCreate?shopid={}'.format(shopid),
            headers={
                'Authorization': 'f\'Bearer {}\''.format(self.access_token)
            }
        ).content.decode('utf-8')
        print(res)

    def close_cart(self, cart_id):
        res = requests.get(
            self.host + '/app/rest/v2/services/nl_ShoppingCartService/cartClose?cartId={}'.format(cart_id),
            headers={
                'Authorization': 'f\'Bearer {}\''.format(self.access_token)
            }
        )
        print(res)

    def cart_merge(self, cart_id_from, cart_id_to):
        res = requests.get(
            self.host + '/app/rest/v2/services/nl_ShoppingCartServices/cartMerge?cartIdFrom={}&cartIdTo={}'.format(
                cart_id_from, cart_id_to
            ),
            headers={
                'Authorization': 'f\'Bearer{}\''.format(self.access_token)
            }
        )
        print(res)

    def cart_add_item(self, cart_id, good_id, price_base, price):
        res = requests.get(
            self.host + '/app/rest/v2/services/nl_ShoppingCartServices/cartAddItem?cartID={}&goodId={}&priceBase={}&price={}'.format(
                cart_id, good_id, price_base, price
            ),
            headers={
                'Authorization': 'f\'Bearer {}\''.format(self.access_token)
            }
        )
        print(res)

    def cart_remove_item(self, cart_id, good_id):
        res = requests.get(
            self.host + '/app/rest/v2/services/nl_ShoppingCartServices/cartRemoveItem?cartId={}&goodId={}'.format(
                cart_id, good_id
            ),
            headers={
                'Authorization': 'f\'Bearer {}\''.format(self.access_token)
            }
        )
        print(res)

    def cart_remove_all_items(self, cart_id):
        res = requests.get(
            self.host + '/app/rest/v2/services/nl_ShoppingCartServices/cartRemoveAllItems?cartId={}'.format(
                cart_id
            ),
            headers={
                'Authorization': 'f\'Bearer {}\''.format(self.access_token)
            }
        )
        print(res)

    # POST orderBasket_add, itemId: 1623403
    # POST orderBasket_get
    # POST orderBasket_setPickup, value: false/true (курьер/самовывоз)
    # POST orderBasket_prepayment, value: true/false (предоплата онлайн/при получении)


# TODO: Add assert values for tests!
