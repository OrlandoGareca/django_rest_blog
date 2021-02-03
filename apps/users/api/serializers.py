from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.Serializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        # data = super().to_representation(instance)
        return {
            'id': instance['id'],
            'username': instance['username'],
            'name': instance['name'],
            'email': instance['email'],
            'password': instance['password']
        }


# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     email = serializers.EmailField()
#
#     def validate_name(self,value):
#         #custom validation
#         if 'developer' in value:
#             raise serializers.ValidationError('Error, no puede existir un usuario')
#         return value
#
#     def validate_email(self,value):
#         #custom validation
#         if value == '':
#             raise serializers.ValidationError('Tiene que insertar un correo')
#         # if self.validate_name(self.context['name']) in value:
#         #     raise serializers.ValidationError('El email no puede contener el nombre')
#
#         return value
#     def validate(self,data):
#         return data
#
#     def create(self, validated_data):
#         # print(validated_data)
#         # return User(**validated_data)
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.email = validated_data.get('email',instance.email)
#         instance.save()
#         return instance
#
#     # def save(self):
#     #     print(self)
# User Serializer
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

        # return user
