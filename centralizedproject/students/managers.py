from django.contrib.auth.base_user import BaseUserManager

# class CustomManager(BaseUserManager):
    
#     def create_user(self, email , password , **extra__fields):
#         if not email:
#             raise ValueError("email is must")
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra__fields)
#         user.set_password(password)
#         user.save()
        
#         return user
    
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)
        
#         return self.create_user(email, password, **extra_fields)