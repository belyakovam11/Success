from django.http import JsonResponse
from django.db import connection
from django.core.cache import cache
from datetime import datetime
from app_quiz.models import CustomUser
from app_quiz.serializers import UserSerializer


def get_db_status(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({'status': 'ok', 'message': 'Database is up and running.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def get_data(request):
    start_time = datetime.now()
    data = cache.get('my_cache_key')

    if not data:
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        data = serializer.data
        cache.set('my_cache_key', data, timeout=60*15)

    end_time = datetime.now()
    response_time = (end_time - start_time).total_seconds()
    return JsonResponse({'data': data, 'response_time': response_time})
