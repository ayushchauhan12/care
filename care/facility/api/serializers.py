from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField

from config.serializers import ChoiceField
from care.facility.models import Facility
from care.facility.models import FACILITY_TYPES

User = get_user_model()


class FacilitySerializer(serializers.ModelSerializer):
    """Serializer for facility.models.Facility."""

    district = ChoiceField(choices=User.DISTRICT_CHOICES)
    facility_type = ChoiceField(choices=FACILITY_TYPES)
    # A valid location => {
    #     "latitude": 49.8782482189424,
    #     "longitude": 24.452545489
    # }
    location = PointField(required=False)

    class Meta:
        model = Facility
        fields = [
            "id",
            "name",
            "district",
            "facility_type",
            "address",
            "location",
            "oxygen_capacity",
            "phone_number",
        ]
