from rest_framework import serializers
from accounts.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'phone_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли должны совпадать!'})
        account.set_password(password)
        account.save()
        return account


class AccountsPropertiesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['pk', 'email', 'phone_number']