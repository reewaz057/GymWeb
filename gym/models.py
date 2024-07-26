from django.db import models
from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_start_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Session(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    session_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Session on {self.session_date} with {self.trainer}"
