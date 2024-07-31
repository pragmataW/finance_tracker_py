from rest_framework import serializers
from tracker.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

    def validate_type(self, value):
        if value not in ['i', 'e']:
            raise serializers.ValidationError("type should be 'i' or 'e'")
        return value

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("category name must be at least 2 character")
        return value