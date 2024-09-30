from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Auction, Bid, Watchlist, TransactionRating
from .forms import AuctionForm, BidForm

# Hlavní stránka s výpisem aukcí
def home(request):
    auctions = Auction.objects.all()[:10]
    return render(request, 'auctions/home.html', {'auctions': auctions})

# Zobrazení detailu aukce
def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    return render(request, 'auctions/auction_detail.html', {'auction': auction})

# Zahájení aukce
@login_required
def create_auction(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.user = request.user
            auction.save()
            return redirect('auction_detail', auction_id=auction.id)
    else:
        form = AuctionForm()
    return render(request, 'auctions/create_auction.html', {'form': form})

# Přihazování
@login_required
def place_bid(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.auction = auction
            bid.save()
            return redirect('auction_detail', auction_id=auction.id)
    else:
        form = BidForm()
    return render(request, 'auctions/place_bid.html', {'form': form})
