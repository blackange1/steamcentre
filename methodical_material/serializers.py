from rest_framework import serializers


class OneEduMaterialSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

    color_id = serializers.IntegerField()
    img = serializers.ImageField()
    date_create = serializers.DateTimeField(read_only=True)
    description = serializers.CharField()
    detailed_description = serializers.CharField()
    link_download = serializers.CharField(max_length=255)
    source = serializers.CharField(max_length=255)
    like = serializers.IntegerField()


class ColorSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=50)
    color = serializers.CharField(max_length=6)
