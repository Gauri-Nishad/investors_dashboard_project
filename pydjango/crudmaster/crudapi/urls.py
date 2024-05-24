from django.urls import path
from crudapi.views import *


urlpatterns = [
    path('add_user',add_user),
    path('update_user',update_user),
    path('get_user',get_user),
    path('get_user_list',get_user_list),
    path('delete_user',delete_user),

    # API for role

    path('add_role',add_role),
    path('update_role',update_role),
    path('get_role',get_role),
    path('get_role_list',get_role_list),
    path('delete_role',delete_role),


    # API for investor

    path('add_investor',add_investor),
    path('update_investor',update_investor),
    path('get_investor',get_investor),
    path('get_investor_list',get_investor_list),
    path('delete_investor',delete_investor),

    #API for country
    path('add_country',add_country),
    path('update_country',update_country),
    path('get_country',get_country),
    path('get_country_list',get_country_list),
    path('delete_country',delete_country),

    #API for company

    path('add_company',add_company),
    path('update_company',update_company),
    path('get_company',get_company),
    path('get_company_list',get_company_list),
    path('delete_company',delete_company),
   

   #API for Cash in flow

   path('cash_inflow',cash_inflow),
   path('update_cash_inflow',update_cash_inflow),
   path('get_cash_inflow',get_cash_inflow),
   path('get_cash_inflow_list',get_cash_inflow_list),
   path('delete_cash_inflow',delete_cash_inflow),
   

   #API for cash out flow
   path('cash_outflow',cash_outflow),
   path('update_cash_outflow',update_cash_outflow),
   path('get_cash_outflow',get_cash_outflow),
   path('get_cash_outflow_list',get_cash_outflow_list),
   path('delete_cash_outflow',delete_cash_outflow),
   #API for login 
   path('login',login),
   path('log_out',log_out),  
   path('menu_list',menu_list),
   path('add_permission',add_permission),
   path('get_permissions',get_permissions),
   #API for appproved and rejected
   path('approved_inflow_transaction', approved_inflow_transaction),
   path('rejected_inflow_transaction', rejected_inflow_transaction),

   path('approved_outflow_transaction', approved_outflow_transaction),
   path('rejected_outflow_transaction', rejected_outflow_transaction),

   path('ApprovedInflowTransactionList',ApprovedInflowTransactionList),
   path('ApprovedOuflowTransactionList',ApprovedOuflowTransactionList),


   #fetch

   path('fetch_cash_flow_data',fetch_cash_flow_data),

   path('fetch_all_data',fetch_all_data),
  


    # mail

    path('send_email',send_email),
    path('reset_password',reset_password)
]