from .models_ai import *
from ..model import *

class GoalAiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['title', 'total_amount', 'pending_amount', 'created_at', 'updated_at', 'due_date', 'notes', 'status']