@patch('app.hotel.RoomsManager')
def test_rent_room__when_no_free_rooms__should_raise(self, mock):
    RoomsManagerMock = mock.return_value
    RoomsManagerMock.has_free_rooms.return_value = False

    hotel = Hotel('At Joe\'s', 3, 2, 1)

    with self.assertRaises(NoFreeRoomError) as context:
        hotel.rent_room([], RoomTypes.APARTMENT)
    self.assertIsNotNone(context.exception)
