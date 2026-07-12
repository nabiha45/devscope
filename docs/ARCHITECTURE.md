# ARCHITECTURE.md

# DevScope System Architecture

---

# 1. Overview

DevScope follows a modular, service-oriented architecture designed around clear separation of responsibilities.

Each major capability of the application is isolated into its own service. This keeps the system maintainable, testable, and easier to extend as new features are introduced.

The application consists of a Next.js frontend, a FastAPI backend, a PostgreSQL database, background workers, AI integrations, and a repository analysis engine.

The guiding architectural principle is:

> Each service should have a single responsibility.

---

# 2. High-Level Architecture

```
                        Browser
                           │
                           ▼
                  Next.js Frontend
                           │
                      REST API
                           │
                           ▼
                    FastAPI Backend
                           │
      ┌────────────┬────────────┬────────────┬────────────┐
      ▼            ▼            ▼            ▼
Authentication  Repository   Analysis       AI
   Service        Service      Service      Service
      │            │            │            │
      └────────────┴────────────┴────────────┘
                           │
                     PostgreSQL
                           │
                   Background Jobs
                           │
                     Tree-sitter
                           │
                      Gemini API
```

---

# 3. Technology Stack

## Frontend

- Next.js
- TypeScript
- Tailwind CSS

## Backend

- FastAPI
- SQLAlchemy
- Alembic

## Database

- PostgreSQL

## Background Processing

- Celery
- Redis

## AI

- Gemini API

## Code Analysis

- Tree-sitter

## Containerization

- Docker

---

# 4. Core Services

## Authentication Service

Responsible for user authentication and authorization.

Responsibilities

- GitHub OAuth
- User login
- Session management
- Authorization
- JWT handling

---

## Repository Service

Responsible for repository lifecycle management.

Responsibilities

- Import repositories
- Clone repositories
- Store repository metadata
- List repositories
- Delete repositories
- Trigger repository analysis

---

## Repository Analysis Service

Responsible for understanding the repository.

Responsibilities

- Parse source code
- Detect frameworks
- Identify technologies
- Count project statistics
- Extract repository metadata
- Generate dependency information
- Store analysis results

---

## AI Service

Responsible for AI-powered features.

Responsibilities

- Repository summaries
- AI chat
- Function explanations
- File explanations
- Generate onboarding path
- Answer repository questions

---

# 5. Data Flow

The following sequence describes what happens when a user imports a repository.

```
User

↓

Authenticate with GitHub

↓

Select Repository

↓

Repository Service

↓

Clone Repository

↓

Queue Analysis Job

↓

Repository Analysis Service

↓

Tree-sitter parses source code

↓

Extract repository metadata

↓

Detect technologies

↓

Generate repository statistics

↓

AI Service generates

• Project summary
• Repository explanation
• Onboarding path

↓

Store analysis results

↓

Display Dashboard
```

---

# 6. Design Principles

DevScope follows the following architectural principles.

## Separation of Concerns

Each service owns one business capability.

---

## Single Responsibility

Services should have one clear purpose.

---

## Modular Design

Features should be independent whenever possible.

---

## Scalability

Long-running operations should execute asynchronously.

---

## Maintainability

Readable code is preferred over clever code.

---

## Extensibility

New analysis features should be added without modifying existing services whenever possible.

---

# 7. Future Architecture

The architecture is intentionally designed to support future capabilities.

Examples include

- Semantic search
- Dependency graphs
- Call graphs
- Database visualization
- AI documentation generation
- Security analysis
- Repository health dashboard

These features should integrate into the existing service architecture without requiring major redesign.

---

# 8. Guiding Principle

Every architectural decision should answer the following question:

> Does this make the repository easier for a developer to understand?

If the answer is no, the feature should be reconsidered.

The primary objective of DevScope is developer onboarding and repository understanding.