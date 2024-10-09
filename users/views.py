from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView

from users.services import create_stripe_product, create_stripe_price, create_stripe_session


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    """Опция создания нового юзера"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    """Настройка для разрешения создавать нового юзера всем"""
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        stripe_product_id = create_stripe_product(payment)
        price_id = create_stripe_price(payment, stripe_product_id)
        session_id, payment_link = create_stripe_session(price_id)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()

