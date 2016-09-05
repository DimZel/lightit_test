from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if not request.user.is_anonymous():
        print request.user.get_full_name()
        return redirect('main')
    context = {'title': 'Login',
               'user': request.user}
    return render(request, 'login.html', context)
