Overview
This project involves building a simple gym management system using Django. It includes features for managing members, trainers, and sessions, and provides functionality to edit and delete members.
Project Structure
1. Models: Define the data structure for Members, Trainers, and Sessions.
2. Forms: Create forms for editing and adding data.
3. Views: Handle the logic for displaying and modifying data.
4. Templates: Provide the HTML templates for the user interface.
5. URLs: Map URL paths to views.

1. Models
Define the models in models.py to represent the data.
from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    membership_start_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Session(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    session_date = models.DateField()

    def __str__(self):
        return f"Session with {self.trainer} on {self.session_date}"


2. Forms
Create forms for handling member data.
from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'membership_start_date']
        widgets = {
            'membership_start_date': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'membership_start_date': 'Membership Start Date'
        }
3. Views
Define the views to handle data processing and rendering.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Trainer, Session
from .forms import MemberForm

def index(request):
    return render(request, 'index.html')

def members_list(request):
    members = Member.objects.all()
    return render(request, 'members_list.html', {'members': members})

def trainers_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers_list.html', {'trainers': trainers})

def sessions_list(request):
    sessions = Session.objects.all()
    return render(request, 'sessions_list.html', {'sessions': sessions})

def edit_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit_member.html', {'form': form, 'member': member})

def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('members_list')
    return render(request, 'confirm_delete.html', {'member': member})

4. Templates
Create HTML templates for rendering the pages.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Members List</title>
    <style>
       body {
            background-image: url('static/gym/background.jpg');
            background-size: cover;
            font-family: Arial, sans-serif;
            color: white;
            margin: 0;
            padding: 0;
        }
        header, main {
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.5); 
        }
        h1 {
            font-size: 2em;
            text-align: center;
        }
        .actions {
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Members List</h1>
    </header>
    <main>
        <section>
            <ul>
                {% for member in members %}
                <li>
                    {{ member.first_name }} {{ member.last_name }} - {{ member.email }}
                    <div class="actions">
                        <a href="{% url 'edit_member' member.id %}">Edit</a>
                        <a href="{% url 'delete_member' member.id %}">Delete</a>
                    </div>
                </li>
                {% empty %}
                <li>No members found.</li>
                {% endfor %}
            </ul>
        </section>
    </main>
</body>
</html>

edit_member.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Member</title>
    <style>
        /* Add your CSS styling here */
    </style>
</head>
<body>
    <header>
        <h1>Edit Member</h1>
    </header>
    <main>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Save changes</button>
        </form>
    </main>
</body>
</html>

confirm_delete.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirm Delete</title>
    <style>
        /* Add your CSS styling here */
    </style>
</head>
<body>
    <header>
        <h1>Confirm Delete</h1>
    </header>
    <main>
        <p>Are you sure you want to delete {{ member.first_name }} {{ member.last_name }}?</p>
        <form method="post">
            {% csrf_token %}
            <button type="submit">Confirm Delete</button>
            <a href="{% url 'members_list' %}">Cancel</a>
        </form>
    </main>
</body>
</html>

5. URLs
Define URL patterns to route requests to the appropriate views.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members_list, name='members_list'),
    path('members/edit/<int:member_id>/', views.edit_member, name='edit_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
    
]


Modules in Django help structure your application by organizing related code into reusable components. Each app serves as a modular unit of functionality, while the project settings and URLs tie these components together. By following the outlined steps, you can effectively manage and scale your Django applications.




