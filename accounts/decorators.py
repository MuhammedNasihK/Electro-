from django.shortcuts import render,redirect

def logout_required(veiw_function):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return veiw_function(request,*args,**kwargs)
    return wrapper
