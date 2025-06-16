import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import webchat_project.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchat_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            webchat_project.routing.websocket_urlpatterns
        )
    ),
})
