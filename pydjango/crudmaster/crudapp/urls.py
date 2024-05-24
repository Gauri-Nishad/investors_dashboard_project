from django.contrib import admin
from django.urls import path,include
from crudapp.views import *
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('base',base),
    # path('add_user',add_user,name="add_user"),
    # path('update_user',update_user,name="update_user"),
    path('',login),
    # path('create_role',create_role,name="create_role"),
    #  path('update_role',update_role,name="update_role"),
    # path('add_investor',add_investor,name="add_investor"),
    # path('update_investor',update_investor,name="update_investor"),
    # path('add_company',add_company,name="add_company"),
    # path('update_company',update_company,name="update_company"),
    # path('add_cash_flow',add_cash_flow,name="add_cash_flow"),
    path('dashboard',dashboard,name="dashboard"),
    path('user_list',user_list,name="user_list"),
    path('company_list',company_list,name="company_list"),
    path('investers_list',investers_list,name="investers_list"),
    path('role_list',role_list,name="role_list"),
    path('permission',permission,name="permission"),
    path('inflow_transaction_list',inflow_transaction_list,name="inflow_transaction_list"),
    path('outflow_transaction_list',outflow_transaction_list,name="outflow_transaction_list"),
    path('reports',reports,name="reports"),
    
    path("permission",permission,name="permission"),
    path("logout",logout,name="logout"),


    
    # path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('not_found',not_found,name='not_found'),
    
    path('forget_password',forget_password ,name='forget_password'),
    path('reset_password/<int:id>',reset_password,name='reset_password'),
  
    
]