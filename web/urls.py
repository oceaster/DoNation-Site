# Essential
from api.post.pledge import new_pledge
from django.urls import path

# Application Views
from core.views import *

# API Views
from api.views import *

# URL Endpoints
urlpatterns = [

    # Core App
    path('', index),
    path('robots.txt', robots),
    path('manifest.json', manifestJSON),
    path('asset-manifest.json', asset_manifest),

    # API Endpoints
    path('api/fetch/<uid>', fetch_user_pledges),
    path('api/post/<uid>/<pledge>/<co2>', post_user_pledge),

]
