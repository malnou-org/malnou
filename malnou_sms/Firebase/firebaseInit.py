#!/usr/bin/env python

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def firebaseInit():
    cred = credentials.Certificate({'Path/Json file'})
    firebase_admin.initialize_app(cred, {
        'databaseURL': {'Database url'}
    })

    dbReference = db.reference('/')

    return dbReference