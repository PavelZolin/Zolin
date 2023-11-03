import sender_stand_request
import data


def test_positive_assert():
    get_track = sender_stand_request.get_track_Orders()
    assert get_track.status_code == 200









