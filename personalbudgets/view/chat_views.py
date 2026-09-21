# views.py
import json
import requests
from django.http import JsonResponse
from django.conf import settings
from ..model import Category, PersonalBudget, Transaction, Goal
import traceback
import logging

logger = logging.getLogger(__name__)

def AiChat(request):
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        message = data.get("message", "")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({'erro': 'JSON inválido'}, status=400)

    if ( len(message) > 200 ):
        return JsonResponse({'erro': 'Limite de caracteres atingido'}, status=400)

    # Serializa os dados do usuário em texto legível p/ o LLM
    user = request.user
    budgets = PersonalBudget.objects.filter(user=user).values()
    transactions = Transaction.objects.filter(budget__user=user).values()
    goals = Goal.objects.filter(user=user).values()
    categories = Category.objects.filter(user=user).values()

    contexto = json.dumps({
        "budgets": list(budgets),
        "transactions": list(transactions),
        "goals": list(goals),
        "categories": list(categories),
    }, ensure_ascii=False, default=str)

    try:
        resposta = requests.post(
            'https://ollama.com/api/chat',
            json={
                "model": "nemotron-3-super",
                "messages":
                [{
                    "role": "user",
                    "content": f"Using the data {contexto}, Answer the question {message}. Don't talk about the data if not asked about it. Never talk with others topics else financers, economy and education."
                }],
                "stream": False
            },
            headers={
                'Authorization': f"Bearer {settings.API_TOKEN}",  # chave segura no settings
                'Content-Type': 'application/json',
            },
            timeout=30,
        )
        response_data = resposta.json()

        return JsonResponse({
            'message': response_data.get('message', {}),
            'model': response_data.get('model', ''),
            'done': response_data.get('done', False)
        })

    except requests.exceptions.Timeout:
        return JsonResponse({'erro': 'Timeout na API externa'}, status=504)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'erro': f'Erro de conexão: {str(e)}'}, status=502)
    except Exception as e:
        return JsonResponse({'erro': f'Erro interno: {str(e)}'}, status=500)