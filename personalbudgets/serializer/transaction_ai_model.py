from .models_ai import *
from ..model import *

class TransactionAiSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = ['item', 'price', 'created_at', 'updated_at', 'validity', 'remaining_installment', 'status', 'notes', 'budget', 'category'] 