from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BudgetForm, UserRegistrationForm
from .models import Plan
from .modules.loan_calc import loan_calculator

# Create your views here.

@login_required
def main_page(request):
    plans = Plan.objects.all().order_by('class_name')
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.cleaned_data['budget']
            plan_obj = plans.get(id = 1) # gets Class A. Could possibly let the user choose a class with a dropdown menu.
            loan_number = loan_calculator(budget, plan_obj)
            return render(request, 'calculator/main.html', {'plans': plans, 'form': form, 'loans': loan_number})
    else:
        form = BudgetForm()
    return render(request, 'calculator/main.html', {'plans': plans, 'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_superuser = user_form.cleaned_data['super_user_check']
            new_user.is_staff = user_form.cleaned_data['super_user_check']
            # Save the User object
            new_user.save()
            return render(request,
                        'calculator/register_done.html',
                        {'new_user': new_user})
        return render(request,
                    'calculator/register.html',
                    {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
        return render(request,
                    'calculator/register.html',
                    {'user_form': user_form})

