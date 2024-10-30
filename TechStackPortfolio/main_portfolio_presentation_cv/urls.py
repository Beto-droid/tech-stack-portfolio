from django.urls import path
from .views import main_user_view

urlpatterns = [
    path('', main_user_view, name='main_portfolio_presentation_cv_home'),
]