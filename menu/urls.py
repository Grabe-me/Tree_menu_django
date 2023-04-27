from django.urls import path
from menu import views


def parameters(num):
    params = ''.join([f'<param{i}>/' for i in range(1, num+1)])
    return params


urlpatterns = [
    path('', views.index_page, name='index'),
    path(parameters(2), views.redirect_func),
]

main_menu = [
    path('1/', views.index_page, name='1'),
    path('2/', views.index_page, name='2'),
    path('21/', views.index_page, name='21'),
    path('22/', views.index_page, name='22'),
    path('211/', views.index_page, name='211'),
    path('212/', views.index_page, name='212'),
    path('221/', views.index_page, name='221'),
    path('222/', views.index_page, name='222'),
    path('11/', views.index_page, name='11'),
    path('12/', views.index_page, name='12'),
    path('111/', views.index_page, name='111'),
    path('112/', views.index_page, name='112'),
    path('121/', views.index_page, name='121'),
    path('122/', views.index_page, name='122'),
]

another_menu = [
    path('a/', views.index_page, name='a'),
    path('b/', views.index_page, name='b'),
    path('aa/', views.index_page, name='aa'),
    path('ab/', views.index_page, name='ab'),
    path('aaa/', views.index_page, name='aaa'),
    path('aab/', views.index_page, name='aab'),
    path('aba/', views.index_page, name='aba'),
    path('abb/', views.index_page, name='abb'),
    path('ba/', views.index_page, name='ba'),
    path('bb/', views.index_page, name='bb'),
    path('baa/', views.index_page, name='baa'),
    path('bab/', views.index_page, name='bab'),
    path('bba/', views.index_page, name='bba'),
    path('bbb/', views.index_page, name='bbb'),
]

urlpatterns += main_menu
urlpatterns += another_menu
