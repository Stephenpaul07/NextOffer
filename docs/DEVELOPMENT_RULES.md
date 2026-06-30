# NextOffer Development Rules

Version: 1.0

---

# Core Principles

- Readability over cleverness.
- Simplicity over unnecessary abstraction.
- Consistency over personal preference.
- Production-ready code from day one.

---

# Architecture

NextOffer follows the Django Service + Selector pattern.

Request Flow:

Client
↓
View
↓
Serializer
↓
Service
↓
Selector
↓
Model Manager
↓
Database

Views must never contain business logic.

---

# Responsibilities

## Views

Responsible for:
- HTTP request handling
- Authentication
- Authorization
- Calling services
- Returning responses

Never:
- Write business logic
- Query models directly

---

## Serializers

Responsible for:
- Input validation
- Output formatting
- Data transformation

---

## Services

Responsible for:
- Business logic
- State changes
- Transactions
- Calling AI services
- Calling selectors

Examples:
- Register user
- Update profile
- Create resume
- Generate ATS report

---

## Selectors

Responsible for:
- Read-only database queries

Selectors must never:
- Create objects
- Update objects
- Delete objects

---

## Models

Models should contain:
- Fields
- Relationships
- Constraints
- Small helper methods

Avoid putting workflows inside models.

---

## Custom Managers

Use custom managers for reusable model-level queries.

Example:

User.objects.active()

Resume.objects.latest()

---

# Code Style

- Follow PEP 8.
- Use descriptive names.
- Keep functions focused.
- Use type hints where practical.
- Prefer composition over inheritance.
- Write meaningful docstrings for public APIs.

---

# Database

- PostgreSQL only.
- Never use SQLite.
- Always use migrations.
- Never modify migration history.

---

# Security

- Never hardcode secrets.
- Use environment variables.
- Validate all user input.
- Apply least privilege.

---

# AI Integration

All LLM interactions must go through dedicated AI service classes.

Views and services must never call providers directly.

---

# Testing

Business logic should be testable independently from Django views.

Keep views thin.

---

# Git Workflow

Commit messages should follow Conventional Commits.

Examples:

feat:
fix:
refactor:
docs:
test:
chore:

Commit frequently with small, meaningful changes.