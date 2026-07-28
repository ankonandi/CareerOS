# ADR-001: Architectural Pattern - Modular Monolith

## Status
Approved

## Context
We are starting the development of CareerOS, an AI-powered Career Copilot SaaS. The platform will eventually include distinct and complex capabilities such as Authentication, Resume Parsing, Job Description Analysis, AI Voice/Text Mock Interviews, and Progress Tracking.

When designing the system topology, we have two primary options:
1.  **Microservices Architecture:** Splitting the domain capabilities into separate services, each with its own repository, database, and execution environment.
2.  **Monolithic Architecture:** Bundling all features into a single repository and execution unit.

While a microservices architecture offers excellent scaling properties and independent deployability, it introduces significant complexity:
*   **Infrastructure Overhead:** Multiple repositories, CI/CD pipelines, container configurations, and service-to-service communication mechanisms (e.g., REST, gRPC, Message Brokers).
*   **Operational Friction:** High complexity in local setup, cross-service debugging, telemetry correlation, and distributed transaction management.
*   **Organization Overhead:** Requires significant cognitive and development efforts to manage shared libraries, interfaces, and schema synchronization, which is difficult for a small startup team targeting rapid iteration.

On the other hand, a standard monolithic architecture can quickly turn into a "big ball of mud" if boundary discipline is not strictly enforced, leading to circular imports, tight coupling between database tables, and high risk of regression when modifying shared code.

## Decision
We will adopt a **Modular Monolith** architecture. The codebase will reside in a single repository and deploy as a single service, but the internal code structure will strictly enforce module boundaries.

Key implementation rules:
*   **Feature-First Packages:** The codebase will be divided into self-contained modules under `backend/app/` (e.g., `users`, `resume`, `jobs`, `interviews`) introduced incrementally when work on those features begins.
*   **Strict Boundaries:** A module may not directly query another module's internal database tables or imports. Communication between modules must happen through defined module APIs, service interfaces, or internal events.
*   **No Shared Entities:** Each module will manage its own database models and schemas. Shared objects (e.g., a `UserID` or standard metadata structures) will be passed between modules using primitive types or shared Pydantic schemas defined in a root `common` directory.
*   **Independent Schemas:** Database tables managed by different modules will be physically isolated or reference each other via soft foreign keys (logical references rather than database-level hard foreign keys) to allow for simple extraction to independent databases if necessary.

## Alternatives Considered

### 1. Microservices Architecture
*   **Why rejected:** The overhead of managing multiple network-separated service boundaries, eventual consistency, and complex local developer setup outweighs the benefits at this stage of the project. Our priority is speed of iteration, rapid prototyping, and minimizing infrastructure maintenance costs.

### 2. Traditional Monolith (Flat Structure)
*   **Why rejected:** Flat monolithic systems with cross-cutting logic degrade rapidly. Code coupling makes refactoring, testing, and scaling individual components highly error-prone. The modular monolith provides a compromise that enforces modular architecture without microservice orchestration friction.

## Consequences

*   **Positive (Benefits):**
    *   **Low Operational Friction:** A single repository, simple local Docker setup, single CI/CD pipeline, and unified backend deployment.
    *   **Refactoring Velocity:** Easy to refactor module boundaries because the code is in the same repository.
    *   **Paving a Path for Microservices:** By keeping database schemas and internal services separated, extracting any module into a standalone microservice in the future will require minimal code restructuring.
*   **Negative (Risks/Cost):**
    *   **Requires Strict Discipline:** Since all files reside in the same repository, developers can technically bypass module boundaries. We must enforce boundary integrity during code reviews and potentially add static analysis tools (e.g., import-linter) in the future.
    *   **Unified Deployments:** Any deployment will roll out the entire codebase, requiring robust automated testing to avoid regressions in stable modules.
