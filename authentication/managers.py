from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError("Введите адрес пользователя")
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Введите пароль пользователя')
        
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user