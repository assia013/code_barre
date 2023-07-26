from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User require an email field')
        if not password:
            raise ValueError('User require a password field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(db_index=True, unique=True, max_length=60)
    username = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    def has_module_perms(self, app_label):
        return True

class Marque (models.Model):
    nom= models.CharField(max_length=30)
    def __str__(self):
        return self.nom
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.marque):
            raise StopIteration
        marque = self.marque[self.index]
        self.index += 1
        return marque
    class Meta:
        verbose_name = 'Marque'
        verbose_name_plural = 'Marques'

class Category (models.Model):
    nom= models.CharField(max_length=30)
    def __str__(self):
        return self.nom
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.Category):
            raise StopIteration
        category = self.Category[self.index]
        self.index += 1
        return category
    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'


class Produit (models.Model):
    num= models.CharField(max_length=30, primary_key=True)
    nom= models.CharField(max_length=30)
    marque= models.ForeignKey(Marque, on_delete=models.CASCADE, null=False)
    categorie= models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.num
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.produit):
            raise StopIteration
        produit = self.produit[self.index]
        self.index += 1
        return produit
    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'


class code_serie(models.Model):
    code = models.IntegerField(unique=True)
    produit= models.ForeignKey(Produit, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.code