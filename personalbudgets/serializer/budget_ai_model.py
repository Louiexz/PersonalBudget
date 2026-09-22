from .models_ai import *
from ..model import *

class PersonalBudgetAiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalBudget
        fields = ['budget', 'total_amount', 'total_spent', 'remaining_amount', 'created_at', 'updated_at', 'validity', 'status', 'notes']