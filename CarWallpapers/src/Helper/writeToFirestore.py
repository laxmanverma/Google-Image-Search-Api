import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def writeToCloudFirestore(coll, doc, fields, data):
	doc_ref = db.collection(coll).document(doc)
	doc_ref.set({
		fields: data
	})
	return "update successful"
