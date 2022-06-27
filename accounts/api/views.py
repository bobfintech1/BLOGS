from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token

from accounts.api.serializers import RegistrationSerializer, AccountsPropertiesSerializers
from accounts.models import Account


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "успешно зарегистрировал нового пользователя."
            data['email'] = account.email
            data['phone_number'] = account.phone_number
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_detail_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountsPropertiesSerializers(account)
        return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_account_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountsPropertiesSerializers(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Аккаунт успешно обновлен"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)