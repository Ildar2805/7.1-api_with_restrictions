from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at', )

    def create(self, validated_data):

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        advertisements_count = Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN').count()
        if advertisements_count >= 10:
            raise serializers.ValidationError("You have 10 open advertisements. You can't create new one.")

        return data
