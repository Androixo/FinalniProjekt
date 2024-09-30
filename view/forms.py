from django import forms
from .models import Auction, Bid

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'description', 'category', 'min_bid', 'buy_now_price', 'location', 'start_date', 'end_date']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_amount']