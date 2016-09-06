# -*- coding: utf-8 -*-
from django import template
from collections import defaultdict

register = template.Library()


@register.filter
def astree(items, attribute):

    # перевод списка в dict: parent -> список детей
    parent_map = defaultdict(list)
    for item in items:
        parent_map[getattr(item, attribute)].append(item)

    # сортировка сообщений в обратном порядке
    parent_map[None] = parent_map[None][::-1]

    # рекурсивный вывод детей одного parent'а
    def tree_level(parent):
        for item in parent_map[parent]:
            yield item
            sub_items = list(tree_level(item))
            if sub_items:
                yield sub_items

    return list(tree_level(None))