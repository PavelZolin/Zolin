import sender_stand_request



def test_get_order_by_track_success():
    get_track = sender_stand_request.get_track_orders(sender_stand_request.get_track())
    assert get_track.status_code == 200









