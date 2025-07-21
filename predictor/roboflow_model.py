import os
from roboflow import Roboflow

API_KEY = os.getenv("ROBofLOW_API_KEY")
rf = Roboflow(api_key=API_KEY)

project = rf.workspace("maria-angelica-krgdu").project("skin-disease-of-cat")
model = project.version(1).model
