from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,username,email,password):

        user = self.model(
            username = username,
            email = email,
            is_active = True,
            is_staff = False,
            is_superuser = False,
        )

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self,username,email,password):
        user = self.model(
            username = username,
            email = email,
            is_active = True,
            is_staff = True,
            is_superuser = True
        )

        user.set_password(password)
        user.save()

        return user