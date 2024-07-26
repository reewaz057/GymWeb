from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Trainer, Session
from .forms import MemberForm  # Ensure you have this form defined

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
