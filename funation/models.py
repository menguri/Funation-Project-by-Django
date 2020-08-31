from django.db import models
 

#이번주/ 피드백, serializer, DRF 목표로 잡기 
#지금은 그냥 내꺼에서 테스트가 잘되면 된다. 

class Post(models.Model):
    title = models.CharField(max_length=100,blank=False)
    cor_id = models.IntegerField(blank=False)                #link with Corpor
    up_date = models.DateField(auto_now_add=True, blank=False)
    fin_date = models.DateField(blank=False)                 #final Day
    goal = models.IntegerField(blank=False)                                 
    lead_img = models.ImageField(upload_to="image")              

class Contents(models.Model):                                #Contents of Post/ 1:1 connection / Contents'id = Post'id
    cont_img = models.ImageField(upload_to="image")               
    cont_write = models.TextField()

class Corporation(models.Model):
    cepre_human = models.CharField(max_length=100,blank=False)
    cor_email = models.EmailField()
    cor_name = models.CharField(max_length=100,blank=False)
    cor_number = models.IntegerField(blank=False)

class Admin(models.Model):                                          
    ad_id = models.CharField(max_length=100,blank=False)
    ad_password = models.CharField(max_length=100,blank=False)

class User(models.Model):                                              
    u_id = models.CharField(max_length=100,blank=False)
    u_password = models.CharField(max_length=100,blank=False)
    profile_img = models.ImageField(upload_to="image")
    email = models.EmailField()
    user_grade = models.IntegerField(blank=False)
    user_number = models.IntegerField(blank=False)
    user_address = models.CharField(max_length=100,blank=False)
    user_money = models.IntegerField(blank=False)

# Mapping for n:m connection
# There are two mapping connection (like, enjoy) 

class Mapping_Enjoy(models.Model):
    user_id = models.IntegerField(blank=False)
    post_id = models.IntegerField(blank=False)

class Mapping_Like(models.Model):
    user_id = models.IntegerField(blank=False)
    post_id = models.IntegerField(blank=False)