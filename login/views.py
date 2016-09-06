from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if not request.user.is_anonymous():
        return redirect('main')
    context = {'title': 'Login',
               'user': request.user}
    return render(request, 'login.html', context)
