from django.contrib import admin
from .models import Member, Trainer, Session

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'membership_start_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('membership_start_date',)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'specialty')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('member', 'trainer', 'session_date', 'notes')
    search_fields = ('member__first_name', 'member__last_name', 'trainer__first_name', 'trainer__last_name', 'notes')
    list_filter = ('session_date', 'trainer')
