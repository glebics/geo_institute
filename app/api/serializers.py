from rest_framework import serializers


class StationSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(StationSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            for field_name, field_type in fields.items():
                self.fields[field_name] = field_type

# class StationSerializer(serializers.Serializer):
#     staid = serializers.IntegerField()
#     staname = serializers.CharField(max_length=4)
#     longstaname = serializers.CharField(max_length=255)
#     igsnum = serializers.CharField(max_length=50)
#     network = serializers.CharField(max_length=50)
#     agency = serializers.CharField(max_length=50)
#     observer = serializers.CharField(max_length=50)
#     country = serializers.CharField(max_length=50)
#     district = serializers.CharField(max_length=50)
#     reseiver = serializers.CharField(max_length=50)
#     recvers = serializers.CharField(max_length=50)
#     recnum = serializers.CharField(max_length=50)
#     antenna = serializers.CharField(max_length=50)
#     dome = serializers.CharField(max_length=50)
#     antnum = serializers.CharField(max_length=50)
#     deltan = serializers.FloatField()
#     deltae = serializers.FloatField()
#     deltah = serializers.FloatField()
#     worktime = serializers.CharField(max_length=50)
#     startdate = serializers.CharField(max_length=50)
#     enddate = serializers.CharField(max_length=50)
#     monument = serializers.CharField(max_length=50)
#     plate = serializers.CharField(max_length=50)
