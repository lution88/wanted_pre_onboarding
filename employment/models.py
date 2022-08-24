from django.db import models

# 회사, 사용자, 채용공고

class Company(models.Model):
    name = models.CharField("회사명", max_length=50)
    country = models.CharField("국가", max_length=20)
    region = models.CharField("지역", max_length=20)
    
    def __str__(self):
        return self.name

class User(models.Model):
    fullname = models.CharField("이름", max_length=10)
    
    def __str__(self):
        return self.fullname

class Employment(models.Model):
    company = models.ForeignKey(to=Company, verbose_name="회사", on_delete=models.CASCADE ,related_name="employments")
    position = models.CharField("채용포지션", max_length=50)
    reward = models.IntegerField("채용보상금")
    content = models.TextField("채용내용")
    techstack = models.CharField("사용기술", max_length=50)
    
    def __str__(self):
        return f'{self.company} / {self.position}'