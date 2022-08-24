from rest_framework.serializers import ModelSerializer
from .models import Employment, User, Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ["name", "country", "region"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmploymentSerializer(ModelSerializer):
    class Meta:
        model = Employment
        fields = ["company", "position", "reward", "content", "techstack"]
        
        
class DetailEmploymentSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Employment
        fields = ["id", "company","position", "reward", "techstack"]