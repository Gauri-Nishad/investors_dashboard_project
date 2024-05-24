from django.shortcuts import render
from django.http import request,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *  
import re
# import requests
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime
from django.utils import timezone
from django.db.models import Sum


from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
@api_view(['POST'])
 
def add_user(request):
    data=request.data.copy()
    print('dd',data)
    role=data.get('role')
    name=data.get('name')
    email=data.get('email')
    mobile=data.get('mobile')
    data['password']=make_password(data['password'])
    if len(str(mobile)) != 10:
        return Response({'msg':'Mobile number must be 10 digit','n':0})
    
    existing_number = User.objects.filter(mobile=mobile).first()
    if existing_number !=None:
         return Response({'msg': 'Mobile number already exists','n':0})
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Incorrect email id','n':0})
    
    existing_email=User.objects.filter(email=email).first()
    if existing_email !=None:
        return Response({'msg':'Email already exists','n':0})


    serializer=UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':'serializer.data','msg':'User added successfully','n':1})
    else:
         return Response({'data':'serializer.errors','msg':'User not added','n':1})
   



@api_view(['POST'])
def update_user(request):
    data=request.data
     
    id=data.get('id')
    email=data.get('email')
    mobile=data.get('mobile')
    obj=User.objects.get(id=id)
    if len(str(mobile)) != 10:
        return Response({'msg':'Mobile number must be 10 digit','n':0})
    
    existing_number = User.objects.filter(mobile=mobile).exclude(id=data.get('id')).first()
    if existing_number !=None:
         return Response({'msg': 'Mobile number already exists','n':0})
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Incorrect email id','n':0})
    
    existing_email=User.objects.filter(email=email).exclude(id=data.get('id')).first()
    if existing_email !=None:
        return Response({'msg':'Email already exists','n':0})
    
    serializer=UserSerializer(obj,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':'serializer.data','msg':'User updated sucessfully','n':1})
    else:
        return Response({'data':'serializer.errors','msg':'User not updated','n':0})
    

@api_view(['POST'])
def get_user(request):
    
    id=request.data.get('id')
    obj=User.objects.filter(id=id).first()
    serializer=UserSerializer(obj)
    return Response(serializer.data)

@api_view(['POST'])
def get_user_list(request):
    
    obj=User.objects.filter()
    serializer=UserSerializer(obj,many=True)
    for r in serializer.data:
        roleobj=Role.objects.filter(id=r['role']).first()
        r['role']=roleobj.name
    return Response(serializer.data)

@api_view(['POST'])
def delete_user(request):
    id=request.data.get('id')
    obj=User.objects.filter(id=id).first()
    if obj is not None:
      obj.delete()
      return Response({'msg':'User deleted'})
    else:
        return Response({'msg':'User not deleted'})


@api_view(['POST'])
def add_role(request):
    data=request.data
    role_name= data.get('name')
    obj=Role.objects.filter()
   
    

    role_serializer=RoleSerializer(obj,many=True)
    for s in role_serializer.data:
        if s['name'].lower()==role_name.lower():
            return  Response({'msg':'Role is already exist','n':0})
    serializer=RoleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,'msg':'Role added successfully','n':1})
    else:
        return Response({'data':serializer.errors,'msg':'Role not added','n':1})

@api_view(['POST'])
def update_role(request):
    data=request.data
    role_id=request.data.get('id')
    role_name=request.data.get('name')
    roleobj=Role.objects.get(id=role_id)    
    serializer=RoleSerializer(roleobj,data=data)
   

    obj=Role.objects.filter().exclude(id=role_id)
    role_serializer=RoleSerializer(obj,many=True)
    for c in role_serializer.data:
        if c['name'].lower()==role_name.lower():
            return  Response({'msg':'Role is already exist','n':0})
    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,'msg':'Role updated','n':1})
    else:
        return Response({'data':serializer.errors,'msg':'Role not updated','n':1})
    
@api_view(['POST'])
def get_role(request):
    role_id=request.data.get('id')
    roleobj=Role.objects.filter(id=role_id).first()
    serializer=RoleSerializer(roleobj)
    return Response(serializer.data)


@api_view(['POST'])
def get_role_list(request):
    roleobj=Role.objects.all()
    serializer=RoleSerializer(roleobj,many=True)
    
    return Response(serializer.data)


@api_view(['POST'])
def delete_role(request):
    role_id=request.data.get('id')
    roleobj=Role.objects.filter(id=role_id).first()
    if roleobj is not None:
       roleobj.delete()
       return Response({'msg':'Role deleted'})
    else:
        return Response({'msg':'Role not deleted'})
    


@api_view(['POST'])
def add_investor(request):
    data=request.data

    mobile=data.get('mobile')
    email=data.get('email')
    if len(str(mobile)) != 10:
        return Response({'msg':'Mobile number must be 10 digit','n':0})
    
    existing_number =Investor.objects.filter(mobile=mobile).first()
    if existing_number !=None:
         return Response({'msg': 'Mobile number already exists','n':0})
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Incorrect email id','n':0})
    
    existing_email=Investor.objects.filter(email=email).first()
    if existing_email !=None:
        return Response({'msg':'Email already exists','n':0})
    

    serializer=InvestorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,'msg':'Investor added successfully','n':1})
    else:
        return Response({'data':serializer.errors,'msg':'Investor not added','n':1})




@api_view(['POST'])
def update_investor(request):
    data=request.data
    id=data.get('id')
    mobile=data.get('mobile')
    email=data.get('email')
    if len(str(mobile)) != 10:
        return Response({'msg':'Mobile number must be 10 digit','n':0 })
    
    existing_number =Investor.objects.filter(mobile=mobile).exclude(id=data.get('id')).first()
    if existing_number !=None:
         return Response({'msg': 'Mobile number already exists','n':0})
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Incorrect email id','n':0})
    
    existing_email=Investor.objects.filter(email=email).exclude(id=data.get('id')).first()
    if existing_email !=None:
        return Response({'msg':'Email already exists','n':0})
    
    obj=Investor.objects.get(id=id)
    serializer=InvestorSerializer(obj,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,'msg':'Investor updated successfully','n':1})
    else:
        return Response({'data':serializer.errors,'msg':'Investor not updated','n':1})
   

@api_view(['POST'])
def get_investor(request):

    id=request.data.get('id')
    obj=Investor.objects.filter(id=id).first()
    serializer=InvestorSerializer(obj)
    return Response(serializer.data)
 


@api_view(['POST'])

def get_investor_list(request):
   obj=Investor.objects.filter()
   serializer=InvestorSerializer(obj,many=True)
   return Response(serializer.data)

@api_view(['POST'])
def delete_investor(request):
    id=request.data.get('id')
    obj=Investor.objects.filter(id=id).first()
    if obj is not None:
        obj.delete()
        return Response({'msg':'Investor deleted'})
    else:
       return Response({'msg':'Data is not available'})

@api_view(['POST'])
def add_country(request):
    data=request.data
    country_name=data.get('country_name')
    obj=Country.objects.filter()
    country_serializer=CountrySerializer(obj,many=True)
    
    for c in country_serializer.data:
        if c['country_name'].lower()==country_name.lower():
            return  Response({'msg':'Country already exist'})

    
    serializer=CountrySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

    

@api_view(['POST'])
def get_country(request):
    data=request.data
    id = data.get('id')
    obj=Country.objects.filter(id=id).first()
    serializer=CountrySerializer(obj)
    return Response(serializer.data)

@api_view(['POST'])
def get_country_list(request):
    obj=Country.objects.all()
    serializer=CountrySerializer(obj,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def update_country(request):
    data=request.data
    id=data.get('id')
    country_name=data.get('country_name')
    obj=Country.objects.get(id=id)
    serializer=CountrySerializer(obj,data=data) 

    obj=Country.objects.filter().exclude(id=id)
    country_serializer=CountrySerializer(obj,many=True)

    for c in country_serializer.data:
        if c['country_name'].lower()==country_name.lower():
            return  Response({'msg':'Country already exist'})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)




@api_view(['DELETE'])
def delete_country(request):
    data=request.data
    id = data.get('id')
    obj=Country.objects.filter(id=id).first()
    obj.delete()
    return Response({'msg':'Country deleted'})



@api_view(['POST'])
def add_company(request):
    data=request.data
    print('dddqqqq',data)
    mobile=data.get('mobile')
    email=data.get('email')
    gstin=data.get('gstin')
    if len(str(mobile)) != 10:
        return Response({'msg':'Mobile number must be 10 digit','n':0 })
    
    existing_number =Company.objects.filter(mobile=mobile).first()
    if existing_number !=None:
         return Response({'msg': 'Mobile number already exists','n':0})
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Incorrect email id','n':0})
    
    existing_email=Company.objects.filter(email=email).first()
    if existing_email !=None:
        return Response({'msg':'Email already exists','n':0 })

    gstin_regex= r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}\d{1}$'
    if not re.match(gstin_regex, gstin) :
        return Response({'msg': 'Incorrect GSTIN.. GSTIN should be in the format XXAAAAA1234X1Z5','n':0})
    
    exist_gstin=Company.objects.filter(gstin=gstin).first()
    if exist_gstin is not None:
        return Response({'msg':'GSTIN is already exists','n':0})
    serializer=CompanySerializer(data=data)
    print('serializer',serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,'msg':'Company added successfully','n':1})
    else:
        return Response({'data':serializer.errors,'msg':'Company is not added','n':1})
     


@api_view(['POST'])
def update_company(request):
    data=request.data
    id=data.get('id')
    print('dddqqqq',data)
    mobile=data.get('mobile')
    email=data.get('email')
    gstin=data.get('gstin')
    if len(str(mobile)) != 10:
        return Response({'msg':'Mobile number must be 10 digit','n':0})
    
    existing_number =Company.objects.filter(mobile=mobile).exclude(id=data.get('id')).first()
    if existing_number !=None:
         return Response({'msg': 'Mobile number already exists','n':0})
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, email) :
        return Response({'msg': 'Incorrect email id','n':0})
    
    existing_email=Company.objects.filter(email=email).exclude(id=data.get('id')).first()
    if existing_email !=None:
        return Response({'msg':'Email already exists','n':0})

    gstin_regex= r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}\d{1}$'
    if not re.match(gstin_regex, gstin) :
        return Response({'msg': 'Incorrect GSTIN.. GSTIN should be in the format XXAAAAA1234X1Z5','n':0})
    
    exist_gstin=Company.objects.filter(gstin=gstin).exclude(id=data.get('id')).first()
    if exist_gstin is not None:
        return Response({'msg':'GSTIN is already exists','n':0})
    
    obj=Company.objects.get(id=id)
    serializer=CompanySerializer(obj,data=data)
    print('serializer',serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,'msg':'Company updated successfully', 'n':1})
    else:
        return Response({'data':serializer.errors,'msg':'Company not updated','n':1})
     

@api_view(['POST'])
def get_company(request):
    data=request.data
    id=data.get('id')
    obj=Company.objects.filter(id=id).first()
    serializer=CompanySerializer(obj)
    return Response(serializer.data)

@api_view(['POST'])
def get_company_list(request):
    obj=Company.objects.filter()
    serializer=CompanySerializer(obj,many=True)
    for c in serializer.data:
        countryobj=Country.objects.filter(id=c['country']).first()
        c['country']=countryobj.country_name
    return Response(serializer.data)

@api_view(['POST'])
def delete_company(request):
   id=request.data.get('id')
   obj=Company.objects.filter(id=id).first()
   if obj is not None:
       obj.delete()
       return Response({'msg':'Company data is deleted'})
   else:
       return Response({'msg':'Data is not available'})



@api_view(['POST'])
def cash_inflow(request):
    data=request.data.copy()
    amount=data.get('amount')
    date=data.get('date')
    date_object = datetime.strptime(date, '%d-%m-%Y')  
    formatted_date = date_object.strftime('%Y-%m-%d')   
    print('formatted_date:', formatted_date)
    print('date:', date)
    data['date'] = formatted_date
    if int(str(amount)) <=0:
        return Response({'msg':'Amount should be in positive number','n':0})

    serializer=InflowTransactionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,'msg':'Amount added successfully','n':1})
    else:
        return Response({'data':serializer.errors,'msg':'Amount not added','n':1})


@api_view(['POST'])
def update_cash_inflow(request):
    data=request.data
    id=data.get('id')
    amount=data.get('amount')
    
    if amount <=0:
        return Response({'msg':'Amount should be in positive'})
    obj=InflowTransaction.objects.get(id=id)
    serializer=InflowTransactionSerializer(obj,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def get_cash_inflow(request):
   id=request.data.get('id')
   obj=InflowTransaction.objects.filter(id=id).first()
   serializer=InflowTransactionSerializer(obj)
   return Response(serializer.data)

@api_view(['POST'])
def get_cash_inflow_list(request):
  obj=InflowTransaction.objects.filter()
  serializer=InflowTransactionSerializer(obj,many=True)
  for n in serializer.data:
     investorobj=Investor.objects.filter(id=n['investor']).first()
     n['investor']=investorobj.first_name
     to_companyobj=Company.objects.filter(id=n['to_company']).first()
      
     n['to_company']= to_companyobj.company_name
  for inflow in serializer.data:
        inflow_id = inflow['id']
        
        
        if ApprovedInflowTransaction.objects.filter(inflowtransaction=inflow_id).exists():
            inflow['status'] = 'Approved'
        
        elif RejectedInflowTransaction.objects.filter(inflowtransaction=inflow_id).exists():
            inflow['status'] = 'Rejected'
  return Response(serializer.data)

@api_view(['POST'])
def delete_cash_inflow(request):
   id=request.data.get('id')
   obj=InflowTransaction.objects.filter(id=id).first()
   if obj is not None:
       obj.delete()
       return Response({'msg':'Data deleted'})
   else:
       return Response({'msg':'Data is not available'})
   




@api_view(['POST'])
def cash_outflow(request):
    data=request.data.copy()
    amount=data.get('amount')
    company_id = data.get('company')
    date=data.get('date')
    date_object = datetime.strptime(date, '%d-%m-%Y')  
    formatted_date = date_object.strftime('%Y-%m-%d')   
    print('formatted_date:', formatted_date)
    print('date:', date)
    data['date'] = formatted_date
    if int(str(amount)) <=0:
       return Response({'msg':'Amount should be in postive number','n':0})
    
    company = Company.objects.filter(id=company_id).first()
    if int(str(amount)) > company.balance:
        return Response({'msg': 'Outlow amount exceeds company balance','n':0})
    serializer=OutflowTransactionSerializer(data=data)
    if serializer.is_valid():
       serializer.save()
       return Response({'data':serializer.data,'msg':'Amount added successfully','n':1})
    else:
       return Response({'data':serializer.errors,'msg':'Form not submitted','n':1})

@api_view(['POST'])
def update_cash_outflow(request):
   data=request.data
   id=data.get('id')
   amount=data.get('amount')
     
   if amount <=0:
    return Response({'msg':'Amount should be in positive'})
   
   obj=OutflowTransaction.objects.get(id=id)
   serializer=OutflowTransactionSerializer(obj,data=data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
   else:
       return Response(serializer.errors)

@api_view(['POST'])
def get_cash_outflow(request):
    id=request.data.get('id')
    obj=OutflowTransaction.objects.filter(id=id).first()
    serializer=OutflowTransactionSerializer(obj)
    return Response(serializer.data)


@api_view(['POST'])
def get_cash_outflow_list(request):
    id=request.data.get('id')
    obj=OutflowTransaction.objects.filter()
    serializer=OutflowTransactionSerializer(obj,many=True)
    for o in serializer.data:
        companyobj=Company.objects.filter(id=o['company']).first()
        o['company']=companyobj.company_name
        tocompanyobj=Company.objects.filter(id=o['to_company']).first()
        o['to_company']=tocompanyobj.company_name
 
         
    for outflow in serializer.data:
        outflow_id = outflow['id']
        
        if ApprovedOutflowTransaction.objects.filter(outflowtransaction=outflow_id).exists():
            outflow['status'] = 'Approved'
        
        elif RejectedOutflowTransaction.objects.filter(outflowtransaction=outflow_id).exists():
            outflow['status'] = 'Rejected'
    return Response(serializer.data)


@api_view(['POST'])
def delete_cash_outflow(request):
    id=request.data.get('id')
    obj=OutflowTransaction.objects.filter(id=id).first()
    if obj is not None:
        obj.delete()
        return Response({'msg':'Data is deleted'})
    
    else:
        return Response({'msg':'Data is not available '})

# @api_view(['POST'])
# def approved_inflow_transactio(request):
#     data = request.data   
#     inflow_transaction_id = data.get('id')

#     inflow_transaction = InflowTransaction.objects.filter(id=inflow_transaction_id).first()
    
#     if inflow_transaction:
         
#         approved_transaction = ApprovedInflowTransaction.objects.create(
#             inflowtransaction=inflow_transaction,
#             investor=inflow_transaction.investor,
#             to_company=inflow_transaction.to_company,
#             date=inflow_transaction.date,
#             amount=inflow_transaction.amount,
#             description=inflow_transaction.description
#         )
       
        
        
       
#         to_company = Company.objects.filter(id=inflow_transaction.to_company).first()
        
#         outflow_transactions=ApprovedOutflowTransaction.objects.filter(to_company=inflow_transaction.to_company)
#         print('outflow transaction',outflow_transactions)
#         total_outflow_amount = sum(outflow.amount for outflow in outflow_transactions)
        
#         if outflow_transactions.exists():
#             if inflow_transaction.amount >= total_outflow_amount:
#                 for outflow_transaction in outflow_transactions: 
#                     approved_companies= Company.objects.filter(id=outflow_transaction.company)
#                     for approved_company in approved_companies:
#                         approved_company.balance += outflow_transaction.amount
#                         approved_company.save()
                    
#                     outflow_transaction.Return = True
#                     outflow_transaction.Return_date = inflow_transaction.date
#                     outflow_transaction.Return_amount = outflow_transaction.amount
#                     outflow_transaction.save()
            
#                 to_company.balance += inflow_transaction.amount
#                 print('to_company.balance', to_company.balance)
#                 to_company.save()
#         else:
#             to_company.balance += inflow_transaction.amount
#             print('to_company.balance', to_company.balance)
#             to_company.save()
         
        
    
#         return Response({'id': approved_transaction.id,  'msg': 'Inflow transaction approved successfully'})
#     else:
#         return Response({'msg': 'Inflow transaction not found'})

@api_view(['POST'])
def rejected_inflow_transaction(request):
    data = request.data   
    inflow_transaction_id = data.get('id')

    inflow_transaction = InflowTransaction.objects.filter(id=inflow_transaction_id).first()
    if inflow_transaction:
        
   
            rejected_transaction = RejectedInflowTransaction.objects.create(
                inflowtransaction=inflow_transaction,
                investor=inflow_transaction.investor,
                to_company=inflow_transaction.to_company,
                date=inflow_transaction.date,
                amount=inflow_transaction.amount,
                description=inflow_transaction.description
            )
            return Response({'id': rejected_transaction.id,   'msg': 'Inflow transaction rejected successfully'})
    else:
        return Response({'msg': 'Inflow transaction not found'})



@api_view(['POST'])
def approved_inflow_transaction(request):
    data = request.data   
    inflow_transaction_id = data.get('id')

    inflow_transaction = InflowTransaction.objects.filter(id=inflow_transaction_id).first()
    
    if inflow_transaction:
         
        approved_transaction = ApprovedInflowTransaction.objects.create(
            inflowtransaction=inflow_transaction,
            investor=inflow_transaction.investor,
            to_company=inflow_transaction.to_company,
            date=inflow_transaction.date,
            amount=inflow_transaction.amount,
            description=inflow_transaction.description
        )
        requestdata={}
        requestdata['inflowtransaction']=inflow_transaction
        requestdata['investor']=inflow_transaction.investor
        requestdata['to_company']=inflow_transaction.to_company
        requestdata['date']=inflow_transaction.date
        requestdata['amount']=inflow_transaction.amount
        requestdata['description']=inflow_transaction.description
       
        approve_trasaction_serilizer=ApprovedInflowTransactionSerializer(data=requestdata)
        if approve_trasaction_serilizer.is_valid():
            approve_trasaction_serilizer.save()
       
        to_company = Company.objects.filter(id=inflow_transaction.to_company).first()
       
         
       
         
        outflow_transactions=ApprovedOutflowTransaction.objects.filter(to_company=inflow_transaction.to_company)
        
        print('outflow transaction',outflow_transactions)
        total_outflow_amount = sum(outflow.amount for outflow in outflow_transactions)
        
        if outflow_transactions.exists():
            if inflow_transaction.amount >= total_outflow_amount:
                for outflow_transaction in outflow_transactions: 
                    if outflow_transaction.Return==False:
                     approved_companies= Company.objects.filter(id=outflow_transaction.company)
                     print('approved_companies',approved_companies)
                     for approved_company in approved_companies:
                      
                    
                      approved_company_data={}
                      print('approved_company_data',approved_company_data)
                      approved_company_balance= approved_company.balance + outflow_transaction.amount
                      print(' approved_company_balance', approved_company_balance)
                      approved_company_data['balance']=approved_company_balance
                      approved_company_serializer=CompanySerializer( approved_company,data=approved_company_data,partial=True)
                      print('approved_company_serializer',approved_company_serializer)
                      if approved_company_serializer.is_valid():
                        approved_company_serializer.save()
                      else:
                         print('approved_company_serializer error',approved_company_serializer.errors)
                         
                    
                    outflow_transaction_data={}
                    print('outflow_transaction_data',outflow_transaction_data)
                    outflow_transaction_data['Return']=True
                    outflow_transaction_data['Return_date']=inflow_transaction.date
                    outflow_transaction_data['Return_amount']=outflow_transaction.amount
                    outflow_transactions_serialzer=ApprovedOutflowTransactionSerializer(outflow_transaction,data=outflow_transaction_data,partial=True)
                    print('outflow_transactions_serialzer',outflow_transactions_serialzer)
                    if outflow_transactions_serialzer.is_valid():
                      outflow_transactions_serialzer.save()
                    else:
                        print('outflow_transactions_serialzer error',outflow_transactions_serialzer.errors)
                to_company_data={}
                print('to_company_data',to_company_data)
                company_balance= to_company.balance + inflow_transaction.amount
                print('company_balance',company_balance)
                print('inflow_transaction.amount',inflow_transaction.amount)
                to_company_data['balance'] = company_balance
                to_company_serializer=CompanySerializer(to_company,data=to_company_data,partial=True)
           
                print('to_company_serializer',to_company_serializer)
                if to_company_serializer.is_valid():
                 to_company_serializer.save()
                 print('ddd',to_company_serializer.data)
                else:
                  print('Validation errors:', to_company_serializer.errors)
        else:

            to_company_data={}
            print('to_company_data',to_company_data)
            company_balance= to_company.balance + inflow_transaction.amount
            print('company_balance',company_balance)
            print('inflow_transaction.amount',inflow_transaction.amount)
            to_company_data['balance'] = company_balance
            to_company_serializer=CompanySerializer(to_company,data=to_company_data ,partial=True)
           
            print('to_company_serializer', to_company_serializer)
            if to_company_serializer.is_valid():
             to_company_serializer.save()
             print('ddd',to_company_serializer.data)
            else:
              print('Validation errors:', to_company_serializer.errors)
         
        
    
        return Response({'id': approved_transaction.id,  'msg': 'Inflow transaction approved successfully'})
    else:
        return Response({'msg': 'Inflow transaction not found'})




@api_view(['POST'])
def approved_outflow_transaction(request):
    data=request.data  
    outflow_transaction_id = data.get('id') 
    
    outflow_transaction =OutflowTransaction.objects.filter(id=outflow_transaction_id).first()
    if outflow_transaction:
        
        approved_transaction = ApprovedOutflowTransaction.objects.create(
        outflowtransaction=outflow_transaction,
        company=outflow_transaction.company,
        to_company=outflow_transaction.to_company,
        date=outflow_transaction.date,
        amount=outflow_transaction.amount,
        description=outflow_transaction.description
       
        )
        company = Company.objects.filter(id=outflow_transaction.company).first()
        to_company = Company.objects.filter(id=outflow_transaction.to_company).first()

         
        transaction_exists = ApprovedOutflowTransaction.objects.filter(to_company=outflow_transaction.company, company=outflow_transaction.to_company ,Return=False)
        
        print('111', transaction_exists)
        

         
        if company and to_company:
            if company.id == to_company.id:
             company.balance -= outflow_transaction.amount
             company.save()

            else:
             
              if transaction_exists.exists():
                    for transaction in transaction_exists:
                        company.balance -= outflow_transaction.amount
                        company.save()
                        to_company.balance += outflow_transaction.amount
                        to_company.save()
                        transaction.Return = True
                        transaction.save()
                        transaction.Return_date = outflow_transaction.date
                        transaction.save()
                        transaction.Return_amount = outflow_transaction.amount
                        transaction.save()
                 

              elif to_company.balance <= 0:
               company.balance -= outflow_transaction.amount
               company.save()
               to_company.balance -= outflow_transaction.amount

               to_company.save()
              else:
               company.balance -= outflow_transaction.amount
               company.save()
               to_company.balance += outflow_transaction.amount
               to_company.save()

          
      


            return Response({'id': approved_transaction.id,  'msg': 'Outflow transaction approved successfully'})
        else:
            return Response({'msg': 'Company not found'} )
    else:
        
        return Response({'msg': 'Outflow transaction not found'})
     
    


@api_view(['POST'])
def rejected_outflow_transaction(request):
    data=request.data   
    outflow_transaction_id = data.get('id')
 
    outflow_transaction =OutflowTransaction.objects.filter(id=outflow_transaction_id).first()
    if outflow_transaction:
        
        rejected_transaction = RejectedOutflowTransaction.objects.create(
        outflowtransaction=outflow_transaction,
        company=outflow_transaction.investor,
        to_company=outflow_transaction.to_company,
        date=outflow_transaction.date,
        amount=outflow_transaction.amount,
        description=outflow_transaction.description
       
        )
        return Response({'id': rejected_transaction.id,  'msg': 'Outflow transaction rejected successfully'})
    else:
        
        return Response({'msg': 'Outflow transaction not found'})
    
@api_view(['POST'])
def ApprovedInflowTransactionList(request):

    approved_transactions = ApprovedInflowTransaction.objects.filter()
    serializer = ApprovedInflowTransactionSerializer(approved_transactions, many=True)
    for o in serializer.data:
        
        companyobj=Company.objects.filter(id=o['to_company']).first()
        o['to_company']=companyobj.company_name 
    return Response(serializer.data)



@api_view(['POST'])
def ApprovedOuflowTransactionList(request):

    approved_transactions = ApprovedOutflowTransaction.objects.filter()
    serializer = ApprovedOutflowTransactionSerializer(approved_transactions, many=True) 
    for o in serializer.data:
        companyobj1=Company.objects.filter(id=o['company']).first()
        o['company']=companyobj1.company_name 
        companyobj=Company.objects.filter(id=o['to_company']).first()
        o['to_company']=companyobj.company_name
    return Response(serializer.data)







@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = User.objects.filter(email=email).first()    
    if user is not None:
        serializer = UserSerializer(user)
        valid_pass = check_password(password,user.password)
        print('passwors..',valid_pass)
        
        if valid_pass:
            refresh_token=RefreshToken.for_user(user)
            access_token=refresh_token.access_token
            user_token=UserToken(user=user,access_token=access_token)
            user_token.save()
            return Response({'msg': 'You  have logged in successfully','accesstoken':str(access_token),'data':serializer.data, 'n':1})
        else:
 
            return Response({'msg': 'Enter valid password','n':0})
    else: 
        return Response({'msg': 'Please enter a valid email or password','n':0})

@api_view(['POST'])
def log_out(request):
    if request.method=='POST':
     token= request.data.get('access_token')
     user_token =UserToken.objects.filter(access_token=token, is_active=True).first()
     if not user_token:
        return Response({'msg':'something went wrong','n':0})
     user_token.is_active = False
     user_token.save()
    return Response({'msg':'You have logged out successfully','n':1})



@api_view(['POST'])
def menu_list(request):
    obj=Menu.objects.all()
    serializer=MenuSerializer(obj,many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def add_permission(request):
    data=request.data
    role_id=request.data.get('role')
    role_obj=Permission.objects.filter(role=role_id).first()
    if role_obj is not None:
        serializer=PermissionSerializer(role_obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'serializer.data','msg':'permission is added','n':1})
    
    else:
        serializer=PermissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'serializer.errors','msg':'permission is not added','n':0})
    
     
@api_view(['POST'])   
def get_permissions(request):
 
    data=request.POST.copy()
    role_id = request.data.get('role')
    obj=Permission.objects.filter(role=role_id).first()
    serializer=PermissionSerializer(obj)
    details=[]
    maindetails=[]
    for s in [serializer.data]:
        print("s",s)
        for m in s['menu']:

            menuobj = Menu.objects.filter(id=m).first()
            print("menuobj",menuobj)
            menu_ser = MenuSerializer(menuobj)
            print("menu",menu_ser.data)
            details.append(menu_ser.data)
        s['menu_details'] = details
        print("sdsd",s['menu_details'])
        maindetails.append(s)
    return Response({'permissions': maindetails[0]})
 






@api_view(["POST"])
def fetch_cash_flow_data(request):
    company_id = request.data.get('company_id')
    date1 = request.data.get('from_date')
    date2 = request.data.get('to_date')

     
    # date1 = datetime.strptime(date1, "%Y-%m-%d") if date1 else None
    # date2 = datetime.strptime(date2, "%Y-%m-%d") if date2 else None

    
    date_object = datetime.strptime(date1, '%d-%m-%Y')  
    formatted_date1 = date_object.strftime('%Y-%m-%d')   
    print('formatted_date:', formatted_date1)
    print('date1:', date1)

    date_object = datetime.strptime(date2, '%d-%m-%Y')  
    formatted_date2 = date_object.strftime('%Y-%m-%d')   
    print('formatted_date2:', formatted_date2)
    print('date1:', date2)
     
    
    if date1 and date2:
        approved_inflows = ApprovedInflowTransaction.objects.filter(
            to_company=company_id,
            date__range=[formatted_date1, formatted_date2]   
        )
        approved_outflows = ApprovedOutflowTransaction.objects.filter(
            company=company_id, 
            date__range=[formatted_date1, formatted_date2]  
        )

         
        if approved_inflows.exists() or approved_outflows.exists():
            company = Company.objects.filter(id=company_id).first()
            company_serializer=CompanySerializer(company)
 
            inflow_serializer = ApprovedInflowTransactionSerializer(approved_inflows, many=True)
            outflow_serializer = ApprovedOutflowTransactionSerializer(approved_outflows, many=True)
            totalinflow=0
            totaloutflow=0
            companylist=[]
            for c in [company_serializer.data]:
               
                
                
                print('ccccc',c)
                for inflow in approved_inflows:
                    totalinflow+=inflow.amount
                    print('totalinflow',totalinflow)
                for outflow in approved_outflows:
                    totaloutflow+=outflow.amount
                    print('totaloutflow',totaloutflow)
                c['totalinflow']=totalinflow
                c['totaloutflow']=totaloutflow
                companylist.append(c)
                
               

                
                
                
            if inflow_serializer:
                for o in inflow_serializer.data:
                    investorobj = Investor.objects.filter(id=o['investor']).first()
                    o['investor'] = investorobj.first_name
                    companyobj = Company.objects.filter(id=o['to_company']).first()
                    o['to_company'] = companyobj.company_name

            if outflow_serializer:
                for o in outflow_serializer.data:
                    companyobj1 = Company.objects.filter(id=o['company']).first()
                    o['company'] = companyobj1.company_name 
                    companyobj = Company.objects.filter(id=o['to_company']).first()
                    o['to_company'] = companyobj.company_name

            return Response({
                'company':companylist,
                'inflow_in_range': inflow_serializer.data,
                'outflow_in_range': outflow_serializer.data
            })
        else:
            return Response({"msg": "No data found within the specified date range."})
    else:
        return Response({"msg": "Please provide both 'start date' and 'end date'."})





@api_view(["POST"])
def fetch_all_data(request):
     
    date1 = request.data.get('from_date')
    date2 = request.data.get('to_date')

     
    date_object = datetime.strptime(date1, '%d-%m-%Y')  
    formatted_date1 = date_object.strftime('%Y-%m-%d')   
    print('formatted_date:', formatted_date1)
     

    date_object = datetime.strptime(date2, '%d-%m-%Y')  
    formatted_date2 = date_object.strftime('%Y-%m-%d')   
    print('formatted_date2:', formatted_date2)
    
    
     
    
    if date1 and date2:
        company = Company.objects.all()
        print('kkkpccc',company)
        company_serializer=CompanySerializer(company,many=True)
        print('company_serializer',company_serializer.data)
        for c in company_serializer.data:
         
            approved_inflow_objs = ApprovedInflowTransaction.objects.filter(to_company=c['id'],
            date__range=[formatted_date1,
            formatted_date2])
            print('c',c)
            print('approved_inflows',approved_inflow_objs)
            total_inflow=0
            for a_inflow in approved_inflow_objs:
                print('a_inflow ',a_inflow )
             
                total_inflow+=a_inflow.amount
                c['totalinflow']= total_inflow
                print(' total_inflow', total_inflow)
            approved_inflow_serializer=ApprovedInflowTransactionSerializer(approved_inflow_objs,many=True)
            c['inflowtransaction']=approved_inflow_serializer.data
            for o in approved_inflow_serializer.data:
                investorobj = Investor.objects.filter(id=o['investor']).first()
                o['investor'] = investorobj.first_name
                companyobj = Company.objects.filter(id=o['to_company']).first()
                o['to_company'] = companyobj.company_name

            approved_outflow_objs= ApprovedOutflowTransaction.objects.filter(
            company=c['id'],
            date__range=[formatted_date1, formatted_date2]  
             )
            total_outflow=0
            for a_outflow in approved_outflow_objs:
            
                total_outflow+=a_outflow.amount
                c['totaloutflow']= total_outflow
    
                print('ggggg',total_outflow)

             
            approved_outflow_serializer=ApprovedOutflowTransactionSerializer(approved_outflow_objs,many=True)
            c['outflowtransaction']= approved_outflow_serializer.data
          
            for o in approved_outflow_serializer.data:
                companyobj1 = Company.objects.filter(id=o['company']).first()
                o['company'] = companyobj1.company_name 
                companyobj = Company.objects.filter(id=o['to_company']).first()
                o['to_company'] = companyobj.company_name
        
            print('approved_outflows',approved_outflow_objs)

         
        
        return Response({
            'company': company_serializer.data,
            #  'inflow_in_range':approved_inflow_serializer.data,
            #  'outflow_in_range':approved_outflow_serializer.data
                
        })
        
    return Response({"msg": "No data found within the specified date range."})
 


@api_view(['POST'])
def send_email(request):
    data=request.data
    email=data.get('email')
    print('email',email)

    user=User.objects.filter(email=email).first()
    userid={'id':user.id,'name':user.name}
    if user:
        html_content = render_to_string("content.html",userid)
        # text_content = strip_tags(html_content)
        mail= EmailMultiAlternatives(
        subject="Testing Email Message",
        body=html_content,   
        from_email="gaurinishad18@gmail.com",
        to=[email],  
        )
        mail.attach_alternative(html_content, "text/html")
        mail.send(fail_silently=False)

        return Response({'msg':"Email has been sent", "n":1})
    else:
        return Response({'msg':"Email not sent please send Email again", "n":0})
    

@api_view(['POST'])
def reset_password(request):
    data=request.data.copy()
    id=request.data.get('id')
    print('idd',id)
    new_password=request.data.get('new_password')
    print('new_password', new_password)
    confirm_password=request.data.get('confirm_password')
    print('confirm_password',confirm_password)
    user=User.objects.filter(id=id).first()
    
    if new_password!=confirm_password:
        return Response({'msg':'Your both Password should be same','n':0})
        
    else:
        usertoken={}
        user_token=UserToken.objects.filter(user_id=id, is_active=True).first()
        if not user_token:
            return Response({'msg':'something went wrong','n':0})
        usertoken['is_active']=False
        user_token_serializer=UserTokenSerializer(user_token,data=usertoken,partial=True)
        if user_token_serializer:
            user_token_serializer.is_valid()
            user_token_serializer.save()   
            print('user_token',user_token)
            print('user_token_serializer', user_token_serializer.data)
            user_password={}
            print('passsssqqqwword',user_password)
            user_password['password']=make_password(new_password)
            print('///////',user_password['password'])
        
        user_serializer=UserSerializer(user,data=user_password,partial=True)
        if user_serializer:
            user_serializer.is_valid()
            user_serializer.save()
        print('user_serializer',user_serializer.data)
        return Response({'msg':'Your Password changed successfully','n':1})
        
    
