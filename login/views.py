from django.shortcuts import render


# Create your views here.
def login(request):
    context = {'title': 'Login',
               'user': request.user}
    return render(request, 'login.html', context)
