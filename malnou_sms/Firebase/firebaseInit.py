#!/usr/bin/env python

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def firebaseInit():
    cred = credentials.Certificate('malnou-526e9db8402c.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://malnou.firebaseio.com/'
    })

    dbReference = db.reference('/')

    return dbReference