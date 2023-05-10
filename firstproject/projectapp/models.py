from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)
from django.urls import reverse_lazy
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,password=None):
        user =self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True       
        user.is_superuser = True   
        user.save(using=self._db)
        return user    

class Users(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('projectapp:top')
    
class Category(models.Model): #カテゴリ(トップス、ボトムスなど)
    category_name = models.CharField(max_length=150)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)  

    user = models.ForeignKey(
        'Users',on_delete=models.CASCADE,
        )

    class Meta:
        db_table = 'Category'

    def get_absolute_url(self):
        return reverse_lazy('projectapp:item_get_list',kwargs={'pk': self.pk})

class Item(models.Model):#各アイテム(白Tシャツ、花柄スカートなど)
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('F', 'F')
    ]    
    SEASON_CHOICES = [
        ('春', '春'),
        ('夏', '夏'),
        ('秋', '秋'),
        ('冬', '冬')
    ]    
    item_name = models.CharField(max_length=150)
    item_picture = models.FileField(upload_to='item_picture/',null=True,blank=True)
    item_color = models.CharField(max_length=150,db_index=True,null=True,blank=True) 
    item_brand = models.CharField(max_length=150,db_index=True,blank=True) 
    item_price = models.IntegerField()
    item_size = models.CharField(max_length=150,null=True,blank=True,choices=SIZE_CHOICES)
    item_season = models.CharField(max_length=150,db_index=True,null=True,blank=True,choices=SEASON_CHOICES)
    item_purchase_date = models.DateField(null=True,blank=True)
    item_expiration_date = models.DateField(null=True,blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)    
    memo = models.TextField(null=True,blank=True)

    user = models.ForeignKey(
        'Users',on_delete=models.CASCADE,
        )
    
    category = models.ForeignKey(
        'Category',on_delete=models.CASCADE
        )

    class Meta:
        db_table = 'Item'

    def get_absolute_url(self):
        return reverse_lazy('projectapp:item_detail',kwargs={'pk': self.pk})


    


