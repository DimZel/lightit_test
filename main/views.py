# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from forms import CommentTreeForm
from datetime import datetime
from models import CommentTree
from mptt.templatetags.mptt_tags import cache_tree_children
from collections import defaultdict


# Create your views here.
def main(request):
    comment_form = CommentTreeForm
    tree = CommentTree.objects.all()

    # перевод списка в dict: parent -> список детей
    parent_map = defaultdict(list)
    for node in tree:
        parent_map[getattr(node, 'parent')].append(node)

    # сортировка сообщений в обратном порядке
    parent_map[None].sort(key=lambda x: x.date, reverse=True)

    # рекурсивный вывод детей одного parent'а
    def tree_level(parent):
        for item in parent_map[parent]:
            yield item
            sub_items = list(tree_level(item))
            for sub_item in sub_items:
                yield sub_item

    nodes = list(tree_level(None))

    context = {'title': 'Стена сообщений',
               'form': comment_form,
               'nodes': nodes}
    return render(request, 'main.html', context)


def add_comment(request):
    if request.POST:
        form = CommentTreeForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date = datetime.now()
            comment.user = request.user
            form.save()
    return redirect('main')


def edit_comment(request):
    if request.POST:
        comment_id = request.POST.get("id")
        comment = CommentTree.objects.get(id=comment_id)
        if comment.user.id == request.user.id:
            form = CommentTreeForm(request.POST)
            if form.is_valid():
                form = CommentTreeForm(request.POST, instance=comment)
                form.save()
    return redirect('main')


def rm_comment(request):
    comment_id = request.GET.get("id")
    comment = CommentTree.objects.get(id=comment_id)
    if comment.user.id == request.user.id:
        comment.delete()
    return redirect('main')
