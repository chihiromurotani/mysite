from urllib import request
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic.base import TemplateView
from .forms import RegistForm,UserLoginForm,RegistCategoryForm,RegistItemForm
from django.views.generic.edit import CreateView,FormView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category,Item
from django.views.generic.list import ListView
from .import forms
import datetime
from django.views.generic.detail import DetailView

class TopView(TemplateView):  #トップ画面
    template_name = 'top.html'

    def get_success_url(self):
        return reverse_lazy('projectapp:top', kwargs={'id': self.id})   
    

class RegistUserView(CreateView): #ユーザ登録
    template_name = 'regist.html'
    form_class = RegistForm


class UserLoginView(LoginView):#ユーザログイン
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

    def form_valid(self,form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1209600)
        return super().form_valid(form)
    

class UserLogoutView(LogoutView):#ユーザログアウト
    pass


class CategoryListView(LoginRequiredMixin,ListView): #ホーム一覧表示
    model = Category
    template_name = 'category_list.html' 
    context_object_name = 'category_list'

    def get_queryset(self):
        current_user = self.request.user
        queryset = super().get_queryset().filter(user_id=current_user)
        return queryset
    
    def dispatch(self, *args, **kwargs) :
        return super().dispatch(*args, **kwargs)   
    
    

class RegistCategoryView(CreateView): #カテゴリ新規登録
    model = Category
    template_name = 'category_regist.html'
    form_class = RegistCategoryForm

    def form_valid(self,form):
        form.instance.create_at = datetime.datetime.today()
        form.instance.update_at = datetime.datetime.today()
        form.instance.user = self.request.user        
        return super(RegistCategoryView,self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('projectapp:category_list')
    


class CategoryUpdateView(UpdateView):#カテゴリ編集
    model = Category
    template_name = 'category_update.html'
    form_class = forms.UpdateCategoryForm
    success_url = reverse_lazy('projectapp:category_list') #処理成功後の遷移先

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self,form):
        form.instance.update_at = datetime.datetime.today()
        return super(CategoryUpdateView,self).form_valid(form)
    


class CategoryDeleteView(DeleteView):#カテゴリ削除
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('projectapp:category_list')


#****************************************************************

class ItemGetListView(ListView): #カテゴリごとのアイテム名一覧表示
    model = Item
    template_name = 'item_get_list.html' 
    context_object_name = 'item_get_list'

    def get_queryset(self):
        current_user = self.request.user
        queryset = super().get_queryset().filter(user_id=current_user, category_id=self.kwargs.get('category_id'))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs('category_id')
        context['category_id'] = category_id
        return context


class RegistItemView(CreateView): #アイテム新規登録
    model = Item
    template_name = 'item_regist.html'
    form_class = RegistItemForm
    # success_url = reverse_lazy('projectapp:item_get_list')
    context_object_name = 'category_list'

    def form_valid(self,form):
        form.instance.create_at = datetime.datetime.today()
        form.instance.update_at = datetime.datetime.today()
        form.instance.category = self.request.category        
        form.instance.user = self.request.user         
        return super(RegistItemView,self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('projectapp:item_get_list',kwargs={'pk': self.object.id})
    


class ItemUpdateView(UpdateView):#アイテム編集
    model = Item
    template_name = 'item_update.html'
    form_class = forms.UpdateItemForm
    # success_url = reverse_lazy('projectapp:item_get_list')

    def get_success_url(self):
        return reverse_lazy('projectapp:item_get_list',kwargs={'pk': self.object.id})

    def form_valid(self,form):
        form.instance.update_at = datetime.datetime.today()
        return super(ItemUpdateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

    
class ItemDeleteView(DeleteView):#アイテム削除
    model = Item
    template_name = 'item_delete.html'
    # success_url = reverse_lazy('projectapp:item_get_list')

    def get_success_url(self):
        return reverse_lazy('projectapp:item_get_list',kwargs={'pk': self.object.id})
    

    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
