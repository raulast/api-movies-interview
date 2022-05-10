from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "release_date",
            "duration",
            "cover",
            "cover1",
            "cover2",
            "trailer",
            "recap",
            "fav",
            "rate",
            "created_at",
            "created_by",
            "public"
        ]
        read_only_fields = ['created_at']


class AddMovieSerializer(serializers.ModelSerializer):

    favorito = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = Movie
        fields = (
            'title',
            'release_date',
            'duration',
            'cover',
            'cover1',
            'cover2',
            'trailer',
            'recap',
            'favorito',
            'rate',
            'public'
        )
        extra_kwargs = {
            'title': {'required': True},
            'release_date': {'required': True},
            'cover': {'required': True},
            'trailer': {'required': True},
            'recap': {'required': True},
            'duration': {'required': False},
            'cover1': {'required': False},
            'cover2': {'required': False},
            'favorito': {'required': False},
            'rate': {'required': False},
            'public': {'required': False}
        }

    def validate(self, attrs):
        if attrs.get('rate') is not None:
            if not(0 <= float(attrs['rate']) <= 5):
                raise serializers.ValidationError(
                    {"rate": "It must have be float number between 0 and 5"})
        return attrs

    def create(self, validated_data):
        movie = Movie.objects.create(
            title=validated_data['title'],
            release_date=validated_data['release_date'],
            cover=validated_data['cover'],
            trailer=validated_data['trailer'],
            recap=validated_data['recap'],
            duration=float(validated_data['duration']) if validated_data.get(
                'duration') is not None else float(0),
            cover1=validated_data['cover1'] if validated_data.get(
                'cover1') is not None else "",
            cover2=validated_data['cover2'] if validated_data.get(
                'cover2') is not None else "",
            fav=validated_data['favorito'] if validated_data.get(
                'favorito') is not None else False,
            rate=float(validated_data['rate']) if validated_data.get(
                'rate') is not None else float(0),
            public=validated_data['public'] if validated_data.get(
                'public') is not None else False,
            created_by=validated_data['owner']
        )

        movie.save()

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.release_date = validated_data.get(
            'release_date', instance.release_date)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.trailer = validated_data.get('trailer', instance.trailer)
        instance.recap = validated_data.get('recap', instance.recap)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.cover1 = validated_data.get('cover1', instance.cover1)
        instance.cover2 = validated_data.get('cover2', instance.cover2)
        instance.fav = validated_data.get('favorito', instance.fav)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.public = validated_data.get('public', instance.public)
        instance.created_by = validated_data.get('owner', instance.created_by)

        instance.save()

        return instance
