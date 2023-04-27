from django.shortcuts import render, redirect
from django.conf import settings
import os


def check_address(address):
    template_dir = os.path.join(settings.BASE_DIR, 'templates')
    template_names = []
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith('.html'):
                template_names.append(os.path.join(root, file)[len(template_dir)+1:])
                template_names.append(
                    os.path.splitext(
                        os.path.join(root, file)[len(template_dir) + 1:]
                    )[0]
                )
    if address not in template_names:
        address = 'page'    # --------------- universal "page.html" file
    return f'{address}.html'    # ----------- named by address ".html" file  (1.html)


def index_page(request, address=None):
    address_path = request.path
    address_list = [i for i in address_path.split('/') if i != '']
    if address_list:
        address = address_list[-1]
    page = check_address(address)
    return render(request, page, {'address': address})


def redirect_func(request, **kwargs):
    address = [a for a in kwargs.values()][-1]
    return redirect(address)
