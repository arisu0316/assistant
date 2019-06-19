from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import *

# Create your views here.

class ExpenseList(LoginRequiredMixin, ListView):
    model = Expense
    ordering = ['-id']  # 反向排序
    paginate_by = 10    # 每頁顯示幾筆

class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = '__all__'                  # 在表單上顯示*所有*欄位
    template_name = 'form.html'         # 指定使用 form.html 這個頁面範本

    def get_success_url(self):
        return reverse('expense_list')  # 新增成功返回支出紀錄列表頁面

class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = '__all__'
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('expense_list')  # 修改成功返回支出紀錄列表頁面

class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('expense_list')