from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserToken
        fields='__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields='__all__'


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
         model=Investor
         fields='__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'


class InflowTransactionSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=InflowTransaction
        fields='__all__'

class OutflowTransactionSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=OutflowTransaction
        fields='__all__'



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'


class ApprovedInflowTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApprovedInflowTransaction
        fields='__all__'

class RejectedInflowTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=RejectedInflowTransaction
        fields='__all__'


class ApprovedOutflowTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= ApprovedOutflowTransaction
        fields='__all__'


class RejectedOutflowTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=RejectedOutflowTransaction
        fields='__all__'