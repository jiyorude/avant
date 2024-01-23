import inquirer
import matplotlib as plt
from datetime import datetime
from avantlib import init
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

current = datetime.now()
formatted = current.strftime("%A, %d %B %Y - %H:%M")
print(formatted)
init()