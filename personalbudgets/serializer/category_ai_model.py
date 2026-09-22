from .models_ai import *
from ..model import *

class CategoryAiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'notes', 'created_at', 'updated_at']