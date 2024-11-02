from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Portfolio, UserData

def main_user_view(request):
    if request.user.is_authenticated:
        portfolio = get_object_or_404(Portfolio, user=request.user)
    else:
        # Load the public user data if no user is logged in
        public_user = get_object_or_404(User, username="alberto")  # Adjust username as needed
        portfolio = get_object_or_404(Portfolio, user=public_user)

    return render(request, 'main_portfolio_presentation_cv/portfolio_user_data_detail.html', {'user_data': portfolio.user_data})
