import inquirer
import matplotlib as plt
from datetime import datetime
from avantlib import init, connect
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user:welcome123@avant.kp8vmpd.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['avant']
map_data = db['map_data']

init()
connect()
print(db.list_collection_names())