from django.shortcuts import render,redirect
from django.contrib import messages 
import requests 
from django.contrib.auth.decorators import login_required
from crudapi.models import *
from django.http import HttpResponseForbidden
from crudapi.models import User,Company,Investor

# def add_user(request):
#     return render(request,'add_user.html')

# def update_user(request):
#     return render(request,'update_user.html')

permission_url='http://127.0.0.1:8000/get_permissions'   
add_login_url='http://127.0.0.1:8000/login'

get_company_url='http://127.0.0.1:8000/get_company'
company_url='http://127.0.0.1:8000/get_company_list'
country_url='http://127.0.0.1:8000/get_country_list'


role_url='http://127.0.0.1:8000/get_role_list'
user_url='http://127.0.0.1:8000/get_user'
users_url='http://127.0.0.1:8000/get_user_list' 
menu_list_url='http://127.0.0.1:8000/menu_list'
add_permission_url='http://127.0.0.1:8000/add_permission'
invester_url='http://127.0.0.1:8000/get_investor_list'

inflow_transaction_url='http://127.0.0.1:8000/get_cash_inflow_list'
outflow_transaction_url='http://127.0.0.1:8000/get_cash_outflow_list'
log_out_url='http://127.0.0.1:8000/log_out'



def login(request):
    data=request.POST.copy()
    if request.method=='POST':
      
      login_request= requests.post(add_login_url,data=data)
      login_response = login_request.json()
      print('response',login_response)
      if login_response['n']==1:
            request.session['access_token']=login_response['accesstoken']
            request.session['role']=login_response['data']['role']
            print("role",login_response['data']['role'])
            request.session['name']=login_response['data']['name']
            print("username",login_response['data']['name'])
            permission_list_request=requests.post(permission_url,data={'role':login_response['data']['role']})
             
            menu_list_response= permission_list_request.json()
            
            request.session['menu_list'] = menu_list_response['permissions']['menu_details']
            messages.success(request, login_response['msg'])
            return redirect('crudapp:dashboard')
      else:
            messages.error(request,login_response['msg'])
            return redirect('http://127.0.0.1:8000')
     
      
     
    return render(request,'login.html')
        
user_url='http://127.0.0.1:8000/get_user'
def base(request):
    
    return render(request,'base.html' )


def logout(request):
    data={}
    data['access_token'] = request.session.get('access_token')
    log_out_request=requests.post(log_out_url,data=data)
    log_out_response=log_out_request.json()   
    print('rspons...',log_out_response)
    if log_out_response['n']==1:
        messages.success(request,log_out_response['msg'])
        request.session.flush()
        return redirect('http://127.0.0.1:8000')

    return redirect('http://127.0.0.1:8000') 

def permission(request):
    if 'role' not in request.session:
        return redirect("http://127.0.0.1:8000")
    menu = request.session.get('menu_list', '')
    print('mmmmm',menu)
    menu_paths = [menu_item['menuPath'] for menu_item in menu]
    print(' menu_paths', menu_paths)
    if '/crudapp/permission'not in menu_paths:
        return redirect('crudapp:not_found')
    menu_list_request=requests.post(menu_list_url)
    menu_list_response=menu_list_request.json()
    role_list_request=requests.post(role_url)
    role_list_response= role_list_request.json()
    name = request.session.get('name', '')
     
   

    # permission_list_request=requests.post(permission_url)
    # permission_list_response= permission_list_request.json()

    if request.method=='POST':
         
        role = request.POST.get('role')
        menus = request.POST.getlist('checklist')
        data = {'role': role, 'menu': menus}
        add_permission_request=requests.post(add_permission_url,data=data)
        add_permission_response=add_permission_request.json()
        if add_permission_response['n']==1:
           messages.success(request,add_permission_response['msg'])
        else:
           messages.error(request,add_permission_response['msg'])

        return redirect('crudapp:permission')
       
    return render(request,'permissions.html',{'menu_list': menu_list_response,'rolelist':role_list_response,'name':name})

# def create_role(request):
#     return render(request,'create_role.html')

# def update_role(request):
#     return render(request,'update_role.html')

# def add_investor(request):
#     return render(request,'add_investor.html')

# def update_investor(request):
#     return render(request,'update_investor.html')

# def add_company(request):
#     return render(request,'add_company.html')


# def update_company(request):
#     return render(request,'update_company.html')

# def add_cash_flow(request):
#     return render(request,'add_cash_flow.html')

approved_inflow_url='http://127.0.0.1:8000/ApprovedInflowTransactionList'
approved_outflow_url='http://127.0.0.1:8000/ApprovedOuflowTransactionList'
def dashboard(request): 
    if 'role' not in request.session:
        return redirect("http://127.0.0.1:8000")
    company_request=requests.post(company_url)
    company_response=company_request.json()
    
    invester_request=requests.post(invester_url)
    investor_response=invester_request.json()

    total_users = User.objects.count()
    total_company=Company.objects.count()
    total_investor=Investor.objects.count()

    print('total_users',total_users)
    name = request.session.get('name', '')
    approved_inflow_request=requests.post(approved_inflow_url)
    approved_inflow_response=approved_inflow_request.json()

   
    approved_outflow_request=requests.post(approved_outflow_url)
    approved_outflow_response=approved_outflow_request.json()
    print('approved_inflow_response',approved_inflow_response)
    return render(request,'dashboard.html',{'total_users':total_users,'investors':investor_response,'companies':company_response,'total_company':total_company,'total_investor':total_investor,'name':name,'approved_inflows':approved_inflow_response,'approved_outflows':approved_outflow_response})



def not_found(request):
    return render(request,'not_found.html')

def user_list(request):
    if 'role' not in request.session:
        return redirect("http://127.0.0.1:8000")
    menu = request.session.get('menu_list', '')
    print('mmmmm',menu)
    menu_paths = [menu_item['menuPath'] for menu_item in menu]
    print(' menu_paths', menu_paths)
    if '/crudapp/user_list'not in menu_paths:
        return redirect('crudapp:not_found')
    role_request=requests.post(role_url)
    role_response=role_request.json()

    user_request=requests.post(user_url)
    user_response=user_request.json()

    user_list_request= requests.post(users_url)
    user_list_response= user_list_request.json()
    name = request.session.get('name', '')
    
    return render(request,'user_list.html',{'users':user_list_response,'single_user':user_response,'rolelist':role_response,'name':name})


def company_list(request):
    if 'role' not in request.session:
         
        return redirect("http://127.0.0.1:8000")
    menu = request.session.get('menu_list', '')
    print('mmmmm',menu)
    menu_paths = [menu_item['menuPath'] for menu_item in menu]
    print(' menu_paths', menu_paths)
    if '/crudapp/company_list'not in menu_paths:
          return redirect('crudapp:not_found')
    get_company_request=requests.post(get_company_url)
    get_company_response=get_company_request.json()
    country_request=requests.post(country_url)
    country_response=country_request.json()
    company_request=requests.post(company_url)
    company_response=company_request.json()
    name = request.session.get('name', '')
    
    return render(request,'company_list.html',{'companies':company_response,'countries':country_response,'single_company':get_company_response,'name':name})

def investers_list(request):
    if 'role' not in request.session:
         
        return redirect("http://127.0.0.1:8000")
    menu = request.session.get('menu_list', '')
    print('mmmmm',menu)
    menu_paths = [menu_item['menuPath'] for menu_item in menu]
    print(' menu_paths', menu_paths)
    if '/crudapp/investers_list'not in menu_paths:
          return redirect('crudapp:not_found')
    invester_request=requests.post(invester_url)
    investor_response=invester_request.json()
    name = request.session.get('name', '')
     
    return render(request,'investers_list.html',{'investors':investor_response,'name':name})


def role_list(request):
    if 'role' not in request.session:
         
        return redirect("http://127.0.0.1:8000")
    menu = request.session.get('menu_list', '')
    print('mmmmm',menu)
    menu_paths = [menu_item['menuPath'] for menu_item in menu]
    print(' menu_paths', menu_paths)
    if '/crudapp/role_list'not in menu_paths:
          return redirect('crudapp:not_found')
    role_request=requests.post(role_url)
    role_response=role_request.json()
    name = request.session.get('name', '')
    
    return render(request,'role_list.html',{'roles':role_response,'name':name})


def inflow_transaction_list(request):
    if 'role' not in request.session:
         
        return redirect("http://127.0.0.1:8000")
    menu = request.session.get('menu_list', '')
    print('mmmmm',menu)
    menu_paths = [menu_item['menuPath'] for menu_item in menu]
    print(' menu_paths', menu_paths)
    if '/crudapp/inflow_transaction_list'not in menu_paths:
        return redirect('crudapp:not_found')
    company_request=requests.post(company_url)
    company_response=company_request.json()
    
    invester_request=requests.post(invester_url)
    investor_response=invester_request.json()
    inflow_transaction_list_request=requests.post(inflow_transaction_url)
    inflow_transaction_list_response=inflow_transaction_list_request.json()
    name = request.session.get('name', '')
    
   
            
    return render(request,'inflow_transaction_list.html',{'inflow_transactions':inflow_transaction_list_response,'investors':investor_response,'companies':company_response,'name':name})
 

def outflow_transaction_list(request):
    if 'role' not in request.session:
        return redirect("http://127.0.0.1:8000")
    
    menu = request.session.get('menu_list', '')
    print('mmmmm',menu)
    menu_paths = [menu_item['menuPath'] for menu_item in menu]
    print(' menu_paths', menu_paths)
    if '/crudapp/outflow_transaction_list'not in menu_paths:
        return redirect('crudapp:not_found')
    company_request=requests.post(company_url)
    company_response=company_request.json()
    outflow_transaction_list_request=requests.post(outflow_transaction_url)
    outflow_transaction_list_response=outflow_transaction_list_request.json()
    name = request.session.get('name', '')
    
   
    return render(request,'outflow_transaction_list.html',{'outflow_transactions':outflow_transaction_list_response,'companies':company_response,'name':name})

 
def reports(request):
    if 'role' not in request.session:
         
        return redirect("http://127.0.0.1:8000")
    menu = request.session.get('menu_list', '')
    print('mmmmm',menu)
    menu_paths = [menu_item['menuPath'] for menu_item in menu]
    print(' menu_paths', menu_paths)
    if '/crudapp/reports'not in menu_paths:
        return redirect('crudapp:not_found')
    company_request=requests.post(company_url)
    company_response=company_request.json()
    name = request.session.get('name', '')
     
    return render(request,'reports.html',{'companies':company_response,'name':name })

send_mail_url="http://127.0.0.1:8000/send_email"
def forget_password(request):
    data=request.POST
    if request.method=='POST':
        send_mail_request=requests.post(send_mail_url,data=data)
        print('.../',send_mail_request)
        send_mail_response=send_mail_request.json()
        print('///',send_mail_response)
        if send_mail_response['n']==1:
            messages.success(request,send_mail_response['msg'])
            return redirect('http://127.0.0.1:8000')
        else:
            messages.error(request,send_mail_response['msg'])

    return render(request,'forget_password.html')

request_password_url='http://127.0.0.1:8000/reset_password'
def reset_password(request,id):
    data=request.POST.copy()
    print(';;;;',data)
    data['id']=id
    print('d id',data['id'])
    if request.method=='POST':
        reset_password_request=requests.post(request_password_url,data=data)
        print('reset_password_request',reset_password_request)
        reset_password_response=reset_password_request.json()
        print('reset_password_response',reset_password_response)
        if reset_password_response['n']==1:
            messages.success(request,reset_password_response['msg'])
            return redirect('http://127.0.0.1:8000')
        else:
            messages.error(request,reset_password_response['msg'])
           
    return render(request,'reset_password.html')



