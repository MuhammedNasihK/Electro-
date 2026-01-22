from django.shortcuts import redirect



def admin_login_required(view_function):
    def wrapper(request,*args,**kwargs):
        if 'admin_id' not in request.session:
            return redirect('login')
        return view_function(request,*args,**kwargs)
    return wrapper