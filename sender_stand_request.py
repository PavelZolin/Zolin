import configuration
import requests
import data


def edit_track_Id(t):
    current_body = data.orders_track.copy()
    current_body["t"] = t
    return current_body

def post_create_orders(body):
    return requests.post(configuration.URL + configuration.CREATE_ORDERS,
                         json=body,
                         headers=data.headers)


def get_track():
    response = post_create_orders(data.product_body)
    track = response.json()
    track_id = track["track"]
    return edit_track_Id(track_id)



def get_track_orders(tr):
    return requests.get(configuration.URL + configuration.TRACK_ORDERS, params=tr, headers=data.headers)









