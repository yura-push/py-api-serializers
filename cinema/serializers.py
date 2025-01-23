from rest_framework import serializers
from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie,
    MovieSession
)


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]
