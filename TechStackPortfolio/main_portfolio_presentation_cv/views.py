from django.shortcuts import render, get_object_or_404
from .models import MainUser

def main_user_view(request):
    main_user = get_object_or_404(MainUser, id=1)
    return render(request, 'main_portfolio_presentation_cv/main_user_detail.html', {'main_user': main_user})
