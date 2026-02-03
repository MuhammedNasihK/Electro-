

class GetLastPageMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        if request.method == 'GET':
            request.session['last_page'] = request.get_full_path()
        return self.get_response(request)
