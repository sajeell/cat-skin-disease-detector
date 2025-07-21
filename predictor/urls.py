from django.urls import path
from .views import *

name = "predictor"

urlpatterns = [
    path("predict", PredictSkinDisease.as_view(), name="predict_skin_disease"),
]
