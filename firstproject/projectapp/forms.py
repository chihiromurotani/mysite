from django import forms
from .models import Users,Category,Item
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime

class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput())

    class Meta:
      model = Users
      fields = ['username', 'email', 'password']

    def save(self,commit=False):
      user = super().save(commit=False)
      validate_password(self.cleaned_data['password'],user)
      user.set_password(self.cleaned_data['password'])
      user.save()
      return user
    
# class UserLoginForm(forms.Form):
#   email = forms.EmailField(label='メールアドレス')
#   password = forms.CharField(label='パスワード',widget=forms.PasswordInput())

class UserLoginForm(AuthenticationForm):
  username = forms.EmailField(label='メールアドレス')
  password = forms.CharField(label='パスワード',widget=forms.PasswordInput())
  remember = forms.BooleanField(label='ログイン状態を保持する',required=False)

class RegistCategoryForm(forms.ModelForm): #カテゴリ新規登録
    category_name = forms.CharField(label='カテゴリ名')

    class Meta:
      model = Category
      fields = ['category_name']

    def save(self,*args,**kwargs):
        obj = super(RegistCategoryForm, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()
        return obj
    

class UpdateCategoryForm(forms.ModelForm): #カテゴリ編集
    category_name = forms.CharField(label='カテゴリ名')

    class Meta:
        model = Category
        fields = ['category_name']

    def save(self,*args,**kwargs):
        obj = super(UpdateCategoryForm, self).save(commit=False)
        obj.update_at = datetime.now()
        obj.save()
        return obj

class RegistItemForm(forms.ModelForm): #item新規登録
    item_name = forms.CharField(label='アイテム名')
    item_picture =forms.FileField(label='画像')
    item_brand = forms.CharField(label='ブランド') 
    item_price = forms.IntegerField(label='価格')    
    item_color = forms.CharField(label='カラー',required=False) 
    item_size = forms.ChoiceField(choices=(
      Item.SIZE_CHOICES
    ),label='サイズ',required=False,widget=forms.CheckboxSelectMultiple)
    item_season = forms.ChoiceField(choices=(
      Item.SEASON_CHOICES
    ),label='季節',required=False,widget=forms.CheckboxSelectMultiple)
    item_purchase_date = forms.DateField(label='購入日',required=False)
    item_expiration_date =forms.DateField(label='消費期限',required=False)
    memo = forms.CharField(widget=forms.Textarea,label='メモ',required=False)

    class Meta:
      model = Item
      fields = ['item_name','item_picture','item_color','item_brand','item_size',
                'item_price','item_season','item_purchase_date','memo']

    def save(self, *args, **kwargs):
      obj = super(RegistItemForm, self).save(commit=False)
      obj.create_at = datetime.now()
      obj.update_at = datetime.now()
      obj.save()
      return obj

class UpdateItemForm(forms.ModelForm): #アイテム編集
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
    item_name = forms.CharField(label='アイテム名')
    item_picture =forms.FileField(label='画像')
    item_brand = forms.CharField(label='ブランド') 
    item_price = forms.IntegerField(label='価格')    
    item_color = forms.CharField(label='カラー',required=False) 
    item_size = forms.MultipleChoiceField(choices=SIZE_CHOICES,label='サイズ',required=False,widget=forms.CheckboxSelectMultiple)
    item_season = forms.MultipleChoiceField(choices=SEASON_CHOICES,label='季節',required=False,widget=forms.CheckboxSelectMultiple)
    item_purchase_date = forms.DateField(label='購入日',required=False)
    item_expiration_date =forms.DateField(label='消費期限',required=False)
    memo = forms.CharField(widget=forms.Textarea,label='メモ',required=False)

    class Meta:
      model = Item
      fields = ['item_name','item_picture','item_color','item_brand','item_size',
                'item_price','item_season','item_purchase_date','memo']


    def save(self,*args,**kwargs):
        obj = super(UpdateItemForm, self).save(commit=False)
        obj.update_at = datetime.now()
        obj.save()
        return obj
