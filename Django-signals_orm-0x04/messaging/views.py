from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def delete_user(request):
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        return redirect('home')
    return redirect('home')