from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "role",
            "phone",
        )

    def create(self, validated_data):
        from patients.models import Patient
        from doctors.models import Doctor

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        user.role = validated_data.get(
            "role",
            "patient"
        )

        user.phone = validated_data.get(
            "phone",
            ""
        )

        user.save()

        if user.role == "patient":

            Patient.objects.create(
                user=user
            )

        elif user.role == "doctor":

            Doctor.objects.create(
                user=user
            )

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "role",
            "phone",
        )