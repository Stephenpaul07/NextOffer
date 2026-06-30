# NextOffer Engineering Guidelines

## Project Overview
NextOffer is an enterprise-grade AI-powered career platform built with Django.

## Tech Stack

- Python 3.12
- Django 5
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Docker
- Azure
- Ollama (Local AI)

## Architecture

Follow a modular monolith architecture.

Keep business logic separated from views.

Organize code into reusable apps.

Prefer composition over duplication.

## Coding Standards

Follow PEP 8.

Use meaningful variable and function names.

Use type hints where practical.

Keep functions focused and readable.

Add docstrings to public functions and classes.

## Database

Use PostgreSQL only.

Never generate SQLite configuration.

Always use Django migrations.

Use indexes for frequently queried fields.

## API

Use Django REST Framework.

Use proper HTTP status codes.

Validate all inputs.

Return consistent JSON responses.

## Security

Never hardcode secrets.

Read configuration from .env.

Validate user input.

Follow secure authentication practices.

## AI Assistant Behavior

Before generating code:

1. Understand the existing project structure.
2. Reuse existing components where possible.
3. Explain architectural decisions when asked.
4. Avoid introducing unnecessary dependencies.
5. Keep the project production-ready.