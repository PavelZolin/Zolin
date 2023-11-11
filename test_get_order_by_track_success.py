import sender_stand_request



def test_positive_assert():
    get_track = sender_stand_request.get_track_orders(sender_stand_request.get_track())
    assert get_track.status_code == 200









