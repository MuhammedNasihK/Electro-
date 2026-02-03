from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAdapter(DefaultSocialAccountAdapter):
    def populate_user(self,request,sociallogin,data):

        user = super().populate_user(request,sociallogin,data)

        first_name = data.get('first_name') or data.get('name')

        if first_name:
            user.username = first_name

        return user