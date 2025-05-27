from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import TickTable
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
import json
import logging

logger = logging.getLogger(__name__)

def live_price_view(request):
    """View to display the live price page"""
    # Get the latest price or a default value
    latest_price = TickTable.objects.order_by('-timestamp').first()
    context = {
        'latest_price': latest_price.live_price if latest_price else Decimal('0.0000000000')
    }
    return render(request, 'ticktable/live_price.html', context)

def price_history_view(request):
    """View to display all price history in a table"""
    # Get all price records, ordered by timestamp (newest first)
    prices = TickTable.objects.all().order_by('-timestamp')
    
    # Implement pagination
    page_number = request.GET.get('page', 1)
    paginator = Paginator(prices, 100)  # Show 100 prices per page
    page_obj = paginator.get_page(page_number)
    
    # Get latest price for real-time display
    latest_price = prices.first()
    
    context = {
        'page_obj': page_obj,
        'latest_price': latest_price,
        'total_entries': prices.count(),
    }
    return render(request, 'ticktable/price_history.html', context)

def get_price_history(request):
    """API endpoint to get paginated price history"""
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except ValueError:
        page = 1
        
    # Get all prices ordered by timestamp (newest first)
    prices = TickTable.objects.all().order_by('-timestamp')
    
    # Set up pagination
    paginator = Paginator(prices, 50)  # 50 items per page
    
    try:
        page_obj = paginator.page(page)
    except:
        page_obj = paginator.page(1)
    
    # Format the data for JSON response
    price_list = []
    for price in page_obj:
        price_list.append({
            'id': price.id,
            'live_price': str(price.live_price),
            'timestamp': price.timestamp.isoformat()
        })
    
    # Return JSON data
    return JsonResponse({
        'prices': price_list,
        'current_page': page,
        'total_pages': paginator.num_pages,
        'total_entries': prices.count(),
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous()
    })

@csrf_exempt
def update_price(request):
    """API endpoint to update the live price - store ALL updates"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_price = Decimal(str(data.get('price', '0')))
            
            # Always store the price, no filtering
            price_entry = TickTable.objects.create(live_price=new_price)
            logger.info(f"Stored new price: {new_price}")
            return JsonResponse({
                'status': 'success', 
                'price': str(price_entry.live_price),
                'id': price_entry.id,
                'timestamp': price_entry.timestamp.isoformat()
            })
        except ValueError as e:
            logger.error(f"Invalid price format: {str(e)}")
            return JsonResponse({'status': 'error', 'message': f'Invalid price format: {str(e)}'}, status=400)
        except Exception as e:
            logger.error(f"Error storing price: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)

def get_latest_price(request):
    """API endpoint to get the latest price"""
    latest_price = TickTable.objects.order_by('-timestamp').first()
    if latest_price:
        return JsonResponse({'price': str(latest_price.live_price)})
    return JsonResponse({'price': '0.0000000000'})
