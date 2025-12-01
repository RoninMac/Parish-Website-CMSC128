"""
========================================
CORE VIEWS - Main Site Pages
========================================
Views for the public-facing website pages.
Each view renders a template using the base.html layout.

ROUTES:
  - '' (root) -> index() or home() [TODO: consolidate these]
  - 'history/' -> history()
  - 'location/' -> location()

TEMPLATES USED: base.html, index.html, history.html, location.html
========================================
"""

from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    """
    Render the home/index page.
    Route: '/' (root URL)
    Template: index.html
    Context: None (static page)
    """
    return render(request, 'index.html')


def history(request):
    """
    Render the parish history page.
    Route: '/history/'
    Template: history.html
    Context: None (static content - timeline and milestones)
    
    TODO: Consider adding context with historical events/data from model
    """
    return render(request, 'history.html')


def location(request):
    """
    Render the location/contact page.
    Route: '/location/'
    Template: location.html
    Context: None (static page)
    
    TODO: Add map integration (Google Maps, Leaflet)
    TODO: Add contact form
    """
    return render(request, 'location.html')


def home(request):
    """
    Render the home page (landing page).
    Route: '' (root URL, name='home')
    Template: home.html
    Context: None (static page)
    
    NOTE: There are two home views (home() and index()).
    TODO: Consolidate to use one home view - recommend using this one
    """
    return render(request, 'home.html')

def go_to_admin(request):
    return redirect('/admin/')