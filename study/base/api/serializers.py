from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Priva