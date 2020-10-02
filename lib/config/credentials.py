from lib.config.server_conf import *

credentials = {
    'app_name': {
        'IDO': '',
        'OFIR': 'OfirLevy-test-PRD-6c8eaa0db-1ff29598'
    },
    'credentials': {
        'IDO': '',
        'OFIR': 'AgAAAA**AQAAAA**aAAAAA**H5hKXw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6AHl4GkAJGFpwudj6x9nY+seQ**hmYGAA**AAMAAA**I6cGW3QDc5h45yOaJ95jG9ZN7zn+WbV6xztgTcSFhB2YZQjvRB61DorP75uS1AviaZ7Doe7Dqc9CtRFsiWaTwazV06HZYXnE8jKYBGa5ROyU18nuyv0BYKPbHftqgmMEcUK2eSqzDXodjTo6ZbCl74mMgkVg/MoxDUV/51wb8sCz2p1vMq7Y6zbdpo12DBZW+0qyNRCsuLEKznLGBJd3zADs3zbmFdgG7HGLKMrUb0v9kAeKKMaKfBodrHrw/MxR0HR71T9jWiFqqdPcciQ61tZ9R1ob53A2Jf++o/i5Xa//5mIY7ClTDt7sjeNIi3LVNfOsHOMdJSepzu62Q+8xBLB4y4nrvDtfXcXLVr5nOxx/uo+0xJck2P5nyYHPbZVCZaGoOOa8CqT6nWn7hB59gDykQhv/0mQPnWa2pg8FK1KVcaDMFn9wBcSLEAi6RnFLkQaXHVcDIA3M2J87333EgcupEKYteJlLFlPN6lEHfI1Aj/3dA/UEvk0wDCRiAeJ3l4kcEqP50mueqevBodXVDonf9kztAJJAUCzgVzDOdyWW8fl6Q0HPDaomD2zhf5iFgxNKCZMTZbhIYHdCkT38Kalz4XHSoa1pbVu9YlbORy1jkwGq7EBhIzxqTudLP5OJDjsNizV1funyKw9OqXvAurAvuT76Olro9aHrdxzXcvfWQTEDcezeBZKISrnuU7hWbcmL8x/Envd6eCgWMY93UW6kHV/Mi5/gcJmlMVtjt0aWHCRNMWpnyK/mlR3OdqDw'
    }

}


def get_app_name():
    return credentials['app_name'][user]


def get_credentials():
    return credentials['credentials'][user]
