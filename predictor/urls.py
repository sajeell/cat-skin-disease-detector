from django.urls import path
from .views import *

name = "predictor"

urlpatterns = [
    path("cat/predict", PredictSkinDisease.as_view(), name="predict_skin_disease"),
]
