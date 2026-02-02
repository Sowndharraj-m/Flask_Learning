"""Gunicorn configuration for production deployment"""

# Binding address
bind = "0.0.0.0:8000"

# Number of worker processes (2-4x number of CPU cores recommended)
workers = 4

# Worker class
worker_class = "sync"

# Maximum number of requests a worker will process before restarting
max_requests = 1000

# Timeout in seconds
timeout = 60

# Access log
accesslog = "logs/access.log"

# Error log
errorlog = "logs/error.log"

# Log level
loglevel = "info"

# Graceful timeout in seconds
graceful_timeout = 30
