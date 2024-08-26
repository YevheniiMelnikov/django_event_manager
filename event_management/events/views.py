import os

from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework_api_key.permissions import HasAPIKey

from .filters import EventFilter
from .models import Event, EventRegistration
from .serializers import EventRegistrationSerializer, EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | HasAPIKey]
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated | HasAPIKey]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @staticmethod
    def send_registration_email(event_registration):
        event = event_registration.event
        user = event_registration.user

        subject = f"Registration Confirmation for {event.title}"
        message = f"Dear {user.username},\n\nYou have successfully registered for {event.title}.\n\nEvent Details:\nDate: {event.date}\nLocation: {event.location}\n\nThank you for registering!"
        email_from = os.getenv("DEFAULT_FROM_EMAIL")
        recipient_list = [user.email]

        send_mail(subject, message, email_from, recipient_list)
