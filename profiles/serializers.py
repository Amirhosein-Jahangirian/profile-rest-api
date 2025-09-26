from rest_framework import serializers

from . import models


class ProfileSerializer(serializers.ModelSerializer):
    """serializes a user object"""

    class Meta:
        model = models.UserProfile
        fields = ('email', 'first_name', 'last_name', 'password',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """creates and returns a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('owner', 'created_on', 'last_edited', 'feed_title', 'feed_description')
        extra_kwargs = {'owner': {'read_only': True},
                        'created_on': {'read_only': True},
                        }
