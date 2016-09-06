from django.shortcuts import render, redirect
from forms import CommentForm
from datetime import datetime
from models import Comment
# from social.apps.django_app.default.models import UserSocialAuth


# Create your views here.
def main(request):
    comment_form = CommentForm
    context = {'title': 'Main',
               'form': comment_form,
               'comments': Comment.objects.order_by('date')}
    return render(request, 'main.html', context)


def add_comment(request):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date = datetime.now()
            # comment.user = UserSocialAuth.objects.get(request.user)
            # comment.user = UserSocialAuth.objects.all()[0]
            form.save()
    return redirect('main')
