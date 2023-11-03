import configuration
import requests
import data

def post_CREATE_Courier(Courier_body):
    return requests.post(configuration.URL + configuration.CREATE_Courier,
                         json=Courier_body,
                         headers=data.headers)
response = post_CREATE_Courier(data.Courier_body)
print(response.status_code)
print(response.json())


def editTrackId(t):
    current_body = data.OrdersTrack.copy()
    current_body["t"] = t
    return current_body

def post_CREATE_Orders(body):
    return requests.post(configuration.URL + configuration.CREATE_Orders,
                         json=body,
                         headers=data.headers)
response = post_CREATE_Orders(data.product_body)



def get_track():
    response = post_CREATE_Orders(data.product_body)
    Track = response.json()
    trackId = Track["track"]
    return editTrackId(trackId)



def get_track_Orders():
    param = get_track()
    return requests.get(configuration.URL + configuration.track_Orders,
                        params=param,
                        headers=data.headers)

response = get_track_Orders()

print("track")
print(response.status_code)
print(response.json())



