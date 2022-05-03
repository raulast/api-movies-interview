from datetime import datetime
from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = [
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
            try:
                datetime.strptime(attrs['release_date'],"%Y-%m-%d")
            except:
                raise serializers.ValidationError({"release_date": "It must have the format YYYY-MM-DD"})

            if attrs.get('rate') is not None:
                if (not ("%s"%(attrs['rate'])).isnumeric())or(("%s"%(attrs['rate'])).isnumeric() and not(0 <= int(("%s"%(attrs['rate']))) <=5)) :
                    raise serializers.ValidationError({"rate": "It must have be float number between 0 and 5"})                
                           
            if attrs.get('duration') is not None:
                if  (not ("%s"%(attrs['duration'])).isnumeric()) :
                    raise serializers.ValidationError({"duration": "It must have be minutes in numeric value"})                
            if attrs.get('favorito') is not None:
                if not isinstance(attrs['favorito'], bool):
                    raise serializers.ValidationError({"favorito": "It must have be boolean."})
            if attrs.get('public') is not None:
                if not isinstance(attrs['public'], bool):
                    raise serializers.ValidationError({"public": "It must have be boolean."})

            return attrs
        
        def create(self, validated_data):
            movie = Movie.objects.create(
                title=validated_data['title'],
                release_date=validated_data['release_date'],
                cover=validated_data['cover'],
                trailer=validated_data['trailer'],
                recap=validated_data['recap'],
                # duration=validated_data['duration'] if validated_data.get('duration') is not None else 0,
                # cover1=validated_data['cover1'] if validated_data.get('cover1') is not None else "",
                # cover2=validated_data['cover2'] if validated_data.get('cover2') is not None else "",
                # fav=validated_data['favorito'] if validated_data.get('favorito') is not None else False,
                # rate=validated_data['rate'] if validated_data.get('rate') is not None else 0,
                # public=validated_data['public'] if validated_data.get('public') is not None else False,
                # created_by=validated_data['owner']
            )
            
            movie.save()

            return movie