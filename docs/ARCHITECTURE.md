# NextOffer Architecture

Version: 1.0

---

# Architecture Style

NextOffer follows a **Modular Monolith Architecture** built using Django.

The application is organized into independent business modules while remaining a single deployable application.

Each module owns its own models, services, selectors, serializers, and APIs.

The architecture prioritizes:

- High Cohesion
- Low Coupling
- Scalability
- Testability
- Maintainability
- Readability

---

# High-Level Request Flow

Client
    │
    ▼
Django REST API
    │
    ▼
Views
    │
    ▼
Serializers
    │
    ▼
Services
    │
    ▼
Selectors
    │
    ▼
Custom Model Managers
    │
    ▼
Models (Django ORM)
    │
    ▼
PostgreSQL

---

# External Integrations

The application communicates with external systems only through dedicated clients.

Examples:

- Ollama
- Azure Blob Storage
- Redis
- Celery
- Email Service

External providers must never be accessed directly from views or business logic.

---

# Project Structure

```
NextOffr/

    apps/

        accounts/
        common/
        resumes/
        ats/
        jobs/
        interviews/
        analytics/
        notifications/

    config/

    docs/

    tests/

    media/

    static/

    logs/

    manage.py
```

---

# Module Responsibilities

Each application should remain independent and encapsulate its own business logic.

Example:

```
accounts/

    admin.py
    apps.py
    models.py
    urls.py
    views.py
    serializers.py
    services.py
    selectors.py
    managers.py
    permissions.py
    validators.py
    tests/
    migrations/
```

---

# Responsibilities

## Views

Views are responsible for:

- Receiving HTTP requests
- Authentication
- Authorization
- Calling services
- Returning HTTP responses

Views must never contain business logic.

Views should remain small and easy to understand.

---

## Serializers

Serializers are responsible for:

- Request validation
- Data transformation
- API representation

Serializers should not implement business workflows.

---

## Services

Services contain all business logic.

Examples:

- Register user
- Update profile
- Generate ATS score
- Create interview session
- Analyze resume
- Bookmark job

Services may call:

- Selectors
- AI services
- External services

Services should never directly perform HTTP operations.

---

## Selectors

Selectors are responsible for read-only database access.

Examples:

- Get user profile
- Find recommended jobs
- Search resumes
- Fetch interview history
- Dashboard statistics

Selectors must never:

- Create records
- Update records
- Delete records

Selectors should use custom model managers whenever appropriate.

---

## Custom Model Managers

Custom model managers encapsulate reusable model-specific database queries.

Examples:

```
User.objects.active()

Resume.objects.latest_versions()

Job.objects.open_positions()
```

Model managers should contain reusable query logic specific to a model.

Selectors should leverage model managers instead of duplicating query logic.

---

## Models

Models represent data only.

Models should contain:

- Fields
- Relationships
- Constraints
- Simple helper methods

Avoid placing business workflows inside models.

---

# AI Layer

AI providers must remain isolated.

Create dedicated AI clients.

Example:

```
apps/common/ai/

    ollama.py
    openai.py
    gemini.py
```

Business logic should never communicate directly with AI providers.

Instead:

Service

↓

AI Client

↓

Provider

This allows AI providers to be replaced without changing business logic.

---

# Background Processing

Long-running operations should execute asynchronously using Celery.

Examples:

- Resume parsing
- ATS generation
- Interview evaluation
- Email sending
- Notification delivery
- AI analysis

---

# Caching

Redis should be used for:

- Frequently accessed data
- AI response caching
- Sessions
- Rate limiting
- Temporary results

---

# Security

Authentication

- JWT

Authorization

- Roles
- Permissions

Secrets

- Environment variables only

Never hardcode:

- Passwords
- API keys
- Database credentials

---

# Database

Database Engine

- PostgreSQL

Rules

- Always use migrations
- Never edit migration history
- Prefer indexes on frequently queried fields
- Use transactions for critical operations

---

# API Standards

The API must follow REST principles.

Requirements:

- Consistent response structure
- Proper HTTP status codes
- Validation before persistence
- Clear error messages
- Versionable endpoints

---

# Testing Strategy

Business logic should be independently testable.

Testing priority:

1. Services
2. Selectors
3. API endpoints

Views should remain thin enough that minimal testing is required.

---

# Design Principles

Prefer:

- Composition
- Reusable services
- Reusable selectors
- Reusable model managers
- Small focused functions
- Clear naming
- Explicit dependencies

Avoid:

- Fat views
- Massive models
- Duplicate business logic
- Circular imports
- Tight coupling

---

# Long-Term Goals

The architecture should allow:

- New modules
- Multiple AI providers
- Horizontal scaling
- Cloud deployment
- API versioning
- Event-driven processing
- Future microservice extraction

without major refactoring.

---

# Architecture Decision Records

## ADR-001

### Decision

Adopt the Django Service + Selector architecture with Custom Model Managers.

### Reason

This architecture aligns with Django best practices while maintaining a clear separation of responsibilities.

Business logic remains centralized inside services.

Read operations remain centralized inside selectors.

Reusable query logic belongs in custom model managers.

A separate Repository layer is intentionally omitted because Django's ORM already provides an effective abstraction over the database.

This approach minimizes unnecessary boilerplate while preserving scalability, maintainability, and testability.