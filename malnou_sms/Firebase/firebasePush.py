#!/usr/bin/env python

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# from Firebase.firebaseInit import firebaseInit

def firebasePush(data, dbReference):
    dbReference.push(data)