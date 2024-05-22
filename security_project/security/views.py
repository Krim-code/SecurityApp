from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SecurityObject
from .forms import SecurityObjectForm

def calculate_security_level(category, number_of_people, threat_type):
    if category in ['special', 'biometric']:
        if number_of_people == 'more_100k':
            return '1УЗ' if threat_type == '1' else '2УЗ' if threat_type == '2' else '3УЗ'
        else:
            return '2УЗ' if threat_type == '1' else '3УЗ' if threat_type == '2' else '4УЗ'
    else:
        if number_of_people == 'more_100k':
            return '2УЗ' if threat_type == '1' else '3УЗ'
        else:
            return '3УЗ' if threat_type == '1' else '4УЗ'

@login_required
def index(request):
    objects = SecurityObject.objects.all()
    return render(request, 'security/index.html', {'objects': objects})

@login_required
def create_object(request):
    if request.method == 'POST':
        form = SecurityObjectForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.security_level = calculate_security_level(obj.category, obj.number_of_people, obj.threat_type)
            obj.save()
            return redirect('index')
    else:
        form = SecurityObjectForm()
    return render(request, 'security/create_object.html', {'form': form})

@login_required
def edit_object(request, pk):
    obj = get_object_or_404(SecurityObject, pk=pk)
    if request.method == 'POST':
        form = SecurityObjectForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.security_level = calculate_security_level(obj.category, obj.number_of_people, obj.threat_type)
            obj.save()
            return redirect('index')
    else:
        form = SecurityObjectForm(instance=obj)
    return render(request, 'security/edit_object.html', {'form': form, 'object': obj})

@login_required
def delete_object(request, pk):
    obj = get_object_or_404(SecurityObject, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('index')
    return render(request, 'security/delete_object.html', {'object': obj})
