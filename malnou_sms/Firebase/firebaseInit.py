#!/usr/bin/env python

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def firebaseInit(Url, fbJson):
    cred = credentials.Certificate(fbJson)
    firebase_admin.initialize_app(cred, {
        'databaseURL': Url
    })

    dbReference = db.reference('/')

    return dbReference