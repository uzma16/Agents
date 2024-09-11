from django.views.decorators.csrf import csrf_exempt
from .main import main
from django.http import JsonResponse
import datetime 
from django.views.decorators.http import require_http_methods
import json

@csrf_exempt
@require_http_methods(["POST"])  
def create_post(request):
    data = json.loads(request.body.decode('utf-8')) 

    user_id = data.get('user_id')
    platform = data.get('platform')
    description = data.get('description')  
    min_word_length = data.get('min_word_length')
    max_word_length = data.get('max_word_length')

    try:
        result = main(platform, description, min_word_length, max_word_length)      
        # Create the current timestamp
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format as string
        
        return JsonResponse({
        'status': 'success',
        'data': {
            'user_id': user_id,
            'platform': platform,
            'description': description,
            'genearted_output':result,
            'created_at': created_at
        }
    })

    except Exception as e:
        print("Error during script execution:", e)
        return JsonResponse({'status': 'error', 'error': str(e)})


