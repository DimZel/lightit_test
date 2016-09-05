from django.shortcuts import render, redirect
from forms import CommentForm
from datetime import datetime
from models import User, Comment


# Create your views here.
def main(request):
    comment_form = CommentForm
    context = {'title': 'Main',
               'form': comment_form,
               'comments': Comment.objects.order_by('date')[::-1]}
    return render(request, 'main.html', context)


def add_comment(request):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date = datetime.now()
            comment.user = User.objects.all()[0]
            form.save()
    return redirect('main')
