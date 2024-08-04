import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-3e5be-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "42069":
        {
            "name": "Joe Biden",
            "major": "presiozentas",
            "starting_year": 2001,
            "total_attendance": 6,
            "standing": "old",
            "year": 4,
            "last_attendance_time": "2024-7-29 13:32:45"
        },
    "123456":
        {
            "name": "Barack Obama",
            "major": "prezedemts",
            "starting_year": 2015,
            "total_attendance": 6,
            "standing": "idk",
            "year": 4,
            "last_attendance_time": "2024-7-29 13:32:45"
        },
    "69420":
        {
            "name": "Donald Trump",
            "major": "scamming",
            "starting_year": 2011,
            "total_attendance": 6,
            "standing": "criminal",
            "year": 4,
            "last_attendance_time": "2024-7-29 13:32:45"
        },
    "100002":
        {
            "name": "Elon Musk",
            "major": "engineering",
            "starting_year": 2022,
            "total_attendance": 69,
            "standing": "good",
            "year": 6,
            "last_attendance_time": "2024-7-29 13:32:45"
        },
    "100001":
        {
            "name": "Emily Blunt",
            "major": "fashion",
            "starting_year": 2015,
            "total_attendance": 42,
            "standing": "good",
            "year": 3,
            "last_attendance_time": "2024-7-29 13:32:45"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
