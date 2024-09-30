from django.db import models
from django.contrib.auth.models import AbstractUser

# Uživatelský účet
class User(AbstractUser):
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    account_type = models.CharField(max_length=10, choices=[('BĚŽNÝ', 'Běžný'), ('PREMIUM', 'Premium')])
    status = models.CharField(max_length=10, choices=[('AKTIVNÍ', 'Aktivní'), ('NEAKTIVNÍ', 'Neaktivní'), ('BLOKOVANÝ', 'Blokovaný')])
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

# Kategorie aukce
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='category_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

# Detaily aukce
class Auction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    min_bid = models.DecimalField(max_digits=10, decimal_places=2)
    buy_now_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    promoted = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Přihazování
class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_date = models.DateTimeField(auto_now_add=True)

# Nákup
class Purchase(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

# Sledování aukcí
class Watchlist(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Hodnocení transakce
class TransactionRating(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    seller_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    seller_comment = models.TextField()
    buyer_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    buyer_comment = models.TextField()