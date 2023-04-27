from django import template
from menu.models import MainMenu, AnotherMenu

register = template.Library()


def get_parents(items, address):
    lst = []
    for i in items:
        if i.name == address:
            lst.append(i.name)
            if i.parent:
                lst += get_parents(items, i.parent.name)
    return lst


@register.inclusion_tag('children_menu.html')
def children_menu(menu, item, address, address_list):
    return {'menu': menu, 'item': item, 'address': address, 'address_list': address_list}


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, address):
    if menu_name == 'main_menu':
        menu = MainMenu.objects.all()
    elif menu_name == 'another_menu':
        menu = AnotherMenu.objects.all()
    address_list = get_parents(menu, address)
    return {'menu': menu, 'address': address, 'address_list': address_list}


@register.inclusion_tag('check_address.html')
def check_address(item, address):
    return {'item': item, 'address': address}
