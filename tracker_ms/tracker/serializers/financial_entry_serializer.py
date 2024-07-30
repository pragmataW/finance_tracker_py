from rest_framework import serializers
from tracker.models import Category, FinancialEntry
from .category_serializer import CategorySerializer

class FinancialEntrySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = FinancialEntry
        fields = ['id', 'user_name', 'category', 'category_id', 'amount', 'target_amount', 'title']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Miktar pozitif bir sayı olmalıdır.")
        return value

    def validate_target_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Hedef miktar pozitif bir sayı olmalıdır.")
        return value

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Başlık en az 2 karakter olmalıdır.")
        return value
