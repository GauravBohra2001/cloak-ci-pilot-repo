# FALSE POSITIVE TEST: Docker-internal container URLs
# Should NOT fire — single-word hostname + port = container service URL pattern
GOTENBERG_URL = "http://gotenberg:3000"
REDIS_CACHE_URL = "http://redis:6379"
CELERY_BROKER_URL = "http://rabbitmq:5672"

# TRUE POSITIVE: real external HTTP endpoint (not a container name)
EXTERNAL_PARTNER_API = "http://api.partner-service.com/v2"
