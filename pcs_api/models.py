from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# Create your models here.

class Client(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Klientas'
        verbose_name_plural = 'Klientai'

    def __str__(self) -> str:
        return f'{self.f_name} {self.l_name}'


class Employee(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Darbuotojas'
        verbose_name_plural = 'Darbuotojai'

    def __str__(self) -> str:
        return f'{self.f_name} {self.l_name}'
    


class Task(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Darbas'
        verbose_name_plural = 'Darbai'

    def __str__(self) -> str:
        return f'{self.name}'


class Bill(models.Model):
    date = models.DateField(auto_now_add=True)
    sum = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = 'Sąskaita'
        verbose_name_plural = 'Sąskaitos'

    def __str__(self) -> str:
        return f'{self.sum}eu {self.date}'


class Project(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    boss = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    employees = models.ManyToManyField(Employee)
    tasks = models.ManyToManyField(Task)
    bills = models.ManyToManyField(Bill)

    class Meta:
        verbose_name = 'Projektas'
        verbose_name_plural = 'Projektai'

    def __str__(self) -> str:
        return f'{self.name}'
    
    def display_employees(self):
        return ', '.join(employee.l_name for employee in self.employees.all())
    

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
