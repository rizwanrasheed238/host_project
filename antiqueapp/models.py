from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.urls import reverse
from django.db.models import Avg, Count
from textblob import TextBlob


class MyAccountManager(BaseUserManager):
    def create_user(self, fname, lname, email, phone_number, is_staff, is_user, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not lname:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            lname=lname,
            fname=fname,
            phone_number=phone_number,
            is_user=is_user,
            is_staff=is_staff,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fname, email, lname, password, phone_number):
        user = self.create_user(
            email=self.normalize_email(email),
            fname=fname,
            password=password,
            lname=lname,
            phone_number=phone_number,

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_user = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


role_choices = (('customer', 'customer'), ('seller', 'seller'), ('None', 'None'))


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.BigIntegerField(default=0)
    roles = models.CharField(max_length=100, choices=role_choices, default="")

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    approved_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', 'phone_number', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    descripton = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('antiqueapp:products_by_category', args=self.slug)

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    descripton = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    availabe = models.BooleanField(default=True)
    createf = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('antiqueapp:product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.slug




# class product(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     slug = models.SlugField(max_length=250, unique=True)
#     descripton = models.TextField(blank=True)
#     price = models.FloatField(default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     stock = models.IntegerField(default=1)
#     image = models.ImageField()
#     availabe = models.BooleanField(default=True)
#     createf = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'product'
#         verbose_name_plural = 'products'

#     def __str__(self):
#         return self.name


    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

class Rating(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    value = models.IntegerField()



class Address(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    fname=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    street = models.TextField(blank=True)
    city=models.TextField(default=0)
    state=models.CharField(max_length=250)
    zip=models.IntegerField(default=1)
    phone=models.BigIntegerField(default=0)

    def __str__(self):
        return self.fname


# def __str__(self):
#     return '{}'.format(self.name)

class ReviewRating(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Review(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    sentiment_polarity = models.FloatField(default=0.0)


    def __str__(self):
        return self.product

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sentiment_polarity = self.get_sentiment()
        super().save(*args, **kwargs)

    def get_sentiment(self):
        blob = TextBlob(self.review)
        sentiment_polarity = blob.sentiment.polarity
        return sentiment_polarity