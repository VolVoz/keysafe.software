# -*- coding: utf-8 -*-

from models import User, Key, UserKeyLink, KeyPlaces


users = [{"firstname": u"ПЕТРО", "lastname": u"ІВАНЕНКО", "rfid_card": "11111", "admin": True},
         {"firstname": u"СИДІР", "lastname": u"БЕРЕЗА", "rfid_card": "22222", "admin": False},
         {"firstname": u"ІВАН", "lastname": u"ІВАНЕНКО", "rfid_card": "33333", "admin": False},
         {"firstname": u"ПЕТРО", "lastname": u"ПЕТРЕНКО", "rfid_card": "44444", "admin": True},
         {"firstname": u"СЕРГІЙ", "lastname": u"КОВАЛЬ", "rfid_card": "55555", "admin": False},
         {"firstname": u"ТАРАС", "lastname": u"ОСТАПЕНКО", "rfid_card": "66666", "admin": False}]
keys = [{"room": "311", "rfid_chip": "111"},
        {"room": "11D", "rfid_chip": "444"},
        {"room": "212", "rfid_chip": "222"},
        {"room": "555", "rfid_chip": "555"},
        {"room": "343", "rfid_chip": "333"}]
keys_places = [{"coordinate_place_x": "11111", "coordinate_place_y": "11111"},
               {"coordinate_place_x": "22222", "coordinate_place_y": "22222"},
               {"coordinate_place_x": "33333", "coordinate_place_y": "33333"},
               {"coordinate_place_x": "44444", "coordinate_place_y": "44444"},
               {"coordinate_place_x": "55555", "coordinate_place_y": "55555"}]


def create_test_data():
    try:
        for place in keys_places:
            KeyPlaces.create(place['coordinate_place_x'], place['coordinate_place_y'])
            print 'Places created!'
    except Exception as e:
        print 'Error - {}'.format(e)
    try:
        for user in users:
            User.create(user['firstname'], user['lastname'], user['rfid_card'], user['admin'])
            print 'Users created!'
    except Exception as e:
        print 'Error - {}'.format(e)
    try:
        for key in keys:
            Key.create(key['room'], key['rfid_chip'])
        print 'Keys added!'
    except Exception as e:
        print 'Error - {}'.format(e)

    try:
        user1 = User.get_by_rfid(users[0]['rfid_card'])['data']
        user2 = User.get_by_rfid(users[1]['rfid_card'])['data']
        user3 = User.get_by_rfid(users[2]['rfid_card'])['data']
        key1 = Key.get_by_rfid(keys[0]['rfid_chip'])['data']
        key2 = Key.get_by_rfid(keys[1]['rfid_chip'])['data']
        key3 = Key.get_by_rfid(keys[2]['rfid_chip'])['data']
        print 'Getting users from db!'
    except Exception as e:
        print 'Error - {}'.format(e)

    try:
        print "Start operations with keys"
        UserKeyLink.getting_key(user1, key1.rfid_chip)['data']
        UserKeyLink.getting_key(user2, key2.rfid_chip)['data']
        UserKeyLink.getting_key(user3, key3.rfid_chip)['data']
        UserKeyLink.returning_key(key2.rfid_chip)['data']
        UserKeyLink.returning_key(key1.rfid_chip)['data']
        print "Done"
    except Exception as e:
        print 'Error - {}'.format(e)
