from rest_framework import serializers
from api.models import RouterDetails


class ResourceDetailsSerializers(serializers.ModelSerializer):

    class Meta:
        model = RouterDetails
        fields = '__all__'
