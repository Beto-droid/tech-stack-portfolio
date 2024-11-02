from TechStackPortfolio.form import LoginForm

def login_form(request):
    return {'login_form': LoginForm()}