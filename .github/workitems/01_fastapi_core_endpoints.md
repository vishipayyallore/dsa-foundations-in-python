# Work Item: Implement FastAPI Core Backend with 6 Endpoints + OpenAPI/Swagger

**Priority:** P0 (Critical)  
**Status:** ✅ Complete  
**Created:** February 12, 2026  
**Completed:** February 12, 2026  
**Assignee:** GitHub Copilot (Coding Agent)  
**Actual Effort:** ~2 hours  
**PR:** [#2 - Merged](https://github.com/Srivari-Hema-SSPL-2026/enterprise-policy-assistant/pull/2)  

---

## 🎯 **S - SPECIFIC ROLE DEFINITION**

**You are a Senior Python Backend Developer specializing in:**

* FastAPI REST API development with async/await patterns
* OpenAPI 3.1 specification and Swagger UI integration
* JWT-based authentication and authorization
* Pydantic v2 models for request/response validation
* Enterprise-grade error handling and logging

**Technology Stack:**

* Python 3.12+
* FastAPI 0.110.0+
* Pydantic 2.6.1+
* python-jose[cryptography] 3.3.0 (JWT)
* passlib[bcrypt] 1.7.4 (password hashing)

---

## 🎯 **M - MISSION-CRITICAL REQUIREMENTS**

**Primary Objective:**  
Implement a production-ready FastAPI backend with **6 core endpoints**, comprehensive OpenAPI 3.1 documentation, and interactive Swagger UI for the Enterprise Policy Assistant RAG application.

**Measurable Outcomes:**

* ✅ All 6 endpoints operational and tested
* ✅ OpenAPI 3.1 specification auto-generated and accessible at `/api/openapi.yaml`
* ✅ Interactive Swagger UI available at `/api/docs`
* ✅ JWT authentication working with token expiration
* ✅ All endpoints return proper HTTP status codes (200, 201, 400, 401, 409)
* ✅ 100% request/response validation via Pydantic
* ✅ Zero linting errors (black, isort, flake8)
* ✅ Test coverage ≥ 80% for all endpoints

---

## 👥 **A - AUDIENCE-AWARE COMMUNICATION**

**Target Audience:** Enterprise development team with:

* Intermediate-to-Advanced Python knowledge
* Familiarity with FastAPI and async programming
* Understanding of RESTful API design principles
* Experience with JWT authentication flows
* Knowledge of OpenAPI specifications

**Architectural Maturity:** N-Tier architecture with clear separation:

* **Presentation Layer:** React 19 frontend (future)
* **Application Layer:** FastAPI REST API (this work item)
* **Service Layer:** RAG services (future work items)
* **Data Layer:** Qdrant + PostgreSQL (infrastructure ready)

---

## 📋 **R - RESPONSE FORMAT CONTROL**

### **Required File Structure:**

```text
src/backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app + endpoint registration
│   ├── config.py               # Configuration management
│   ├── models/
│   │   ├── __init__.py
│   │   ├── auth.py             # Pydantic models for auth
│   │   └── health.py           # Pydantic models for health
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py             # Auth endpoints: /api/auth/*
│   │   └── health.py           # Health endpoint: /health
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth_service.py     # Authentication business logic
│   └── utils/
│       ├── __init__.py
│       ├── jwt_handler.py      # JWT token creation/validation
│       └── password.py         # Password hashing utilities
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_auth.py
│   └── conftest.py             # Pytest fixtures
└── .env.example                # Environment variables template
```

### **Code Quality Standards:**

```python
# All functions must have:
# 1. Type hints (PEP 484)
# 2. Docstrings (Google style)
# 3. Async where applicable
# 4. Proper error handling

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

async def example_endpoint(
    user_id: Annotated[str, Depends(get_current_user)]
) -> dict[str, str]:
    """
    Example endpoint with proper typing.
    
    Args:
        user_id: Authenticated user ID from JWT token
        
    Returns:
        Dictionary containing user information
        
    Raises:
        HTTPException: 401 if authentication fails
    """
    # Implementation here
    pass
```

---

## ⚙️ **T - TASK-ORIENTED CONSTRAINTS**

### **🚨 CRITICAL CONSTRAINTS:**

1. **Framework Versions (DO NOT CHANGE):**
   * Python: 3.12+
   * FastAPI: 0.110.0+
   * Pydantic: 2.6.1+
   * ❌ DO NOT downgrade packages in `pyproject.toml`

2. **Architecture Patterns:**
   * ✅ MUST use FastAPI dependency injection
   * ✅ MUST separate routes, models, and services
   * ✅ MUST use async/await for all endpoints
   * ❌ DO NOT use synchronous blocking calls

3. **Security Requirements:**
   * ✅ MUST hash passwords with bcrypt (12 rounds minimum)
   * ✅ MUST validate JWT tokens on protected endpoints
   * ✅ MUST use environment variables for secrets (JWT_SECRET_KEY)
   * ❌ DO NOT hardcode secrets or API keys

4. **OpenAPI Requirements:**
   * ✅ MUST use FastAPI auto-generated OpenAPI 3.1
   * ✅ MUST include comprehensive endpoint descriptions
   * ✅ MUST define all request/response schemas
   * ✅ MUST add security schemes for bearerAuth

---

## 📝 **DETAILED ENDPOINT SPECIFICATIONS**

### **Endpoint 1: Root Endpoint**

```yaml
GET /
Summary: Root endpoint with API information
Tags: [System]
Responses:
  200:
    description: API information
    content:
      application/json:
        schema:
          type: object
          properties:
            status:
              type: string
              example: "ok"
            message:
              type: string
              example: "Enterprise Policy Assistant API"
            version:
              type: string
              example: "1.0.0"
            endpoints:
              type: object
              properties:
                health:
                  type: string
                  example: "/health"
                openapi:
                  type: string
                  example: "/api/openapi.yaml"
                swagger:
                  type: string
                  example: "/api/docs"
```

**Implementation Notes:**

* Simple informational endpoint
* No authentication required
* Returns API metadata and navigation links

---

### **Endpoint 2: Health Check**

```yaml
GET /health
Summary: Health check endpoint
Tags: [System]
Responses:
  200:
    description: Service is healthy
    content:
      application/json:
        schema:
          type: object
          required: [status, message]
          properties:
            status:
              type: string
              enum: [healthy, degraded, unhealthy]
              example: "healthy"
            message:
              type: string
              example: "All systems operational"
            timestamp:
              type: string
              format: date-time
              example: "2026-02-12T23:30:00Z"
```

**Implementation Notes:**

* Used by monitoring systems and load balancers
* Should check database connectivity (future: add Qdrant + PostgreSQL health checks)
* Always returns 200 for basic version

---

### **Endpoint 3: OpenAPI Specification (YAML)**

```yaml
GET /api/openapi.yaml
Summary: Get OpenAPI 3.1 specification in YAML format
Tags: [Documentation]
Responses:
  200:
    description: OpenAPI YAML specification
    content:
      application/x-yaml:
        schema:
          type: string
```

**Implementation Notes:**

* FastAPI auto-generates OpenAPI spec
* Use `app.openapi()` to get JSON, then convert to YAML
* Requires `PyYAML` package (add to dependencies)

---

### **Endpoint 4: User Registration**

```yaml
POST /api/auth/register
Summary: Register a new user account
Tags: [Authentication]
RequestBody:
  required: true
  content:
    application/json:
      schema:
        type: object
        required: [username, email, password]
        properties:
          username:
            type: string
            minLength: 3
            maxLength: 50
            pattern: "^[a-zA-Z0-9_-]+$"
            example: "john_doe"
          email:
            type: string
            format: email
            example: "john.doe@company.com"
          password:
            type: string
            minLength: 8
            maxLength: 100
            example: "SecurePass123!"
          role:
            type: string
            enum: [USER, ADMIN]
            default: USER
            example: "USER"
Responses:
  201:
    description: User successfully registered
    content:
      application/json:
        schema:
          type: object
          properties:
            user:
              $ref: "#/components/schemas/User"
            access_token:
              type: string
              example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            token_type:
              type: string
              example: "bearer"
  400:
    description: Validation error (invalid input)
    content:
      application/json:
        schema:
          $ref: "#/components/schemas/ErrorResponse"
  409:
    description: User already exists (duplicate username/email)
    content:
      application/json:
        schema:
          $ref: "#/components/schemas/ErrorResponse"
```

**Implementation Notes:**

* Validate email format and password strength
* Hash password with bcrypt before storage
* Check for duplicate username/email (return 409 Conflict)
* Generate JWT token upon successful registration
* Store user in PostgreSQL `users` table

---

### **Endpoint 5: User Login**

```yaml
POST /api/auth/login
Summary: Authenticate user and return JWT token
Tags: [Authentication]
RequestBody:
  required: true
  content:
    application/json:
      schema:
        type: object
        required: [username, password]
        properties:
          username:
            type: string
            example: "john_doe"
          password:
            type: string
            example: "SecurePass123!"
Responses:
  200:
    description: Login successful
    content:
      application/json:
        schema:
          type: object
          properties:
            user:
              $ref: "#/components/schemas/User"
            access_token:
              type: string
              example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            token_type:
              type: string
              example: "bearer"
  400:
    description: Validation error
    content:
      application/json:
        schema:
          $ref: "#/components/schemas/ErrorResponse"
  401:
    description: Invalid credentials (wrong username/password)
    content:
      application/json:
        schema:
          $ref: "#/components/schemas/ErrorResponse"
```

**Implementation Notes:**

* Verify username exists in database
* Compare hashed password with stored hash
* Return 401 if credentials are invalid
* Generate new JWT token on successful login
* Include user role in JWT payload

---

### **Endpoint 6: Get Current User**

```yaml
GET /api/auth/me
Summary: Get authenticated user information
Tags: [Authentication]
Security:
  - bearerAuth: []
Responses:
  200:
    description: Current user information
    content:
      application/json:
        schema:
          type: object
          properties:
            user:
              $ref: "#/components/schemas/User"
  401:
    description: Unauthorized (missing or invalid token)
    content:
      application/json:
        schema:
          $ref: "#/components/schemas/ErrorResponse"
```

**Implementation Notes:**

* Protected endpoint requiring valid JWT token
* Extract user_id from JWT payload
* Fetch user details from PostgreSQL
* Return 401 if token is missing, expired, or invalid

---

## 🔒 **OPENAPI & SWAGGER CONFIGURATION**

### **Required OpenAPI Metadata:**

```python
from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Policy Assistant API",
    description="RAG-based policy query system with OpenAI and Qdrant",
    version="1.0.0",
    contact={
        "name": "Viswanatha Swamy P K",
        "email": "support@enterprise-policy-assistant.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {
            "name": "System",
            "description": "System health and metadata endpoints",
        },
        {
            "name": "Authentication",
            "description": "User registration, login, and profile management",
        },
        {
            "name": "Documentation",
            "description": "API documentation and OpenAPI specification",
        },
    ],
)
```

### **Security Schemes:**

```python
# Add to OpenAPI schema
app.openapi_schema["components"]["securitySchemes"] = {
    "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "Enter JWT token obtained from /api/auth/login or /api/auth/register",
    }
}
```

### **Common Schemas:**

```python
# In app/models/auth.py
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal

class User(BaseModel):
    """User model (excluding password)"""
    id: int
    username: str
    email: EmailStr
    role: Literal["USER", "ADMIN"]
    created_at: datetime

class RegisterRequest(BaseModel):
    """User registration request"""
    username: str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_-]+$")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)
    role: Literal["USER", "ADMIN"] = "USER"

class LoginRequest(BaseModel):
    """User login request"""
    username: str
    password: str

class AuthResponse(BaseModel):
    """Authentication response with JWT token"""
    user: User
    access_token: str
    token_type: str = "bearer"

class ErrorResponse(BaseModel):
    """Standard error response"""
    detail: str
    error_code: str | None = None
```

---

## ✅ **WHAT TO DO (Implementation Checklist)**

### **Phase 1: Project Setup (1 hour)**

- [ ] Create directory structure (`app/`, `routers/`, `models/`, `services/`, `utils/`)
- [ ] Set up `app/main.py` with FastAPI app initialization
- [ ] Configure OpenAPI metadata (title, description, version, contact, license)
- [ ] Add CORS middleware for future frontend integration
- [ ] Create `.env.example` with required environment variables

### **Phase 2: Configuration & Utils (1 hour)**

- [ ] Implement `app/config.py` using `pydantic-settings`
  - [ ] JWT_SECRET_KEY
  - [ ] JWT_ALGORITHM (HS256)
  - [ ] JWT_ACCESS_TOKEN_EXPIRE_MINUTES (30)
  - [ ] DATABASE_URL
- [ ] Implement `app/utils/password.py`
  - [ ] `hash_password(password: str) -> str`
  - [ ] `verify_password(plain: str, hashed: str) -> bool`
- [ ] Implement `app/utils/jwt_handler.py`
  - [ ] `create_access_token(data: dict) -> str`
  - [ ] `verify_access_token(token: str) -> dict`
  - [ ] `get_current_user(token: str) -> int` (dependency)

### **Phase 3: Pydantic Models (1 hour)**

- [ ] Create `app/models/health.py`
  - [ ] HealthResponse
- [ ] Create `app/models/auth.py`
  - [ ] User
  - [ ] RegisterRequest
  - [ ] LoginRequest
  - [ ] AuthResponse
  - [ ] ErrorResponse

### **Phase 4: Routers & Endpoints (3 hours)**

- [ ] Implement `app/routers/health.py`
  - [ ] GET `/health` endpoint
- [ ] Implement `app/routers/auth.py`
  - [ ] POST `/api/auth/register`
  - [ ] POST `/api/auth/login`
  - [ ] GET `/api/auth/me` (with JWT dependency)
- [ ] Implement root endpoint in `app/main.py`
  - [ ] GET `/` endpoint
- [ ] Implement OpenAPI YAML endpoint in `app/main.py`
  - [ ] GET `/api/openapi.yaml`

### **Phase 5: Authentication Service (1.5 hours)**

- [ ] Create `app/services/auth_service.py`
  - [ ] `register_user(username, email, password, role) -> User`
  - [ ] `authenticate_user(username, password) -> User | None`
  - [ ] `get_user_by_id(user_id: int) -> User | None`
- [ ] Integrate with PostgreSQL `users` table
- [ ] Handle duplicate user errors (409 Conflict)

### **Phase 6: Testing (1.5 hours)**

- [ ] Create `tests/conftest.py`
  - [ ] TestClient fixture
  - [ ] Mock database fixture
  - [ ] Test user fixtures
- [ ] Write `tests/test_health.py`
  - [ ] Test GET `/health` returns 200
- [ ] Write `tests/test_auth.py`
  - [ ] Test user registration (201, 400, 409)
  - [ ] Test user login (200, 401)
  - [ ] Test get current user (200, 401)
  - [ ] Test JWT token generation and validation

### **Phase 7: Documentation & Polish (1 hour)**

- [ ] Verify Swagger UI at `/api/docs`
- [ ] Verify ReDoc at `/redoc`
- [ ] Test OpenAPI YAML download at `/api/openapi.yaml`
- [ ] Add endpoint descriptions and examples
- [ ] Add response models to all endpoints
- [ ] Run linters (black, isort, flake8)
- [ ] Ensure 80%+ test coverage

---

## ❌ **WHAT NOT TO DO (Forbidden Actions)**

1. **❌ DO NOT use Flask or any framework other than FastAPI**
   - Reason: This is a FastAPI project, not Flask

2. **❌ DO NOT store passwords in plain text**
   - Reason: Security violation - always use bcrypt hashing

3. **❌ DO NOT hardcode JWT secrets or API keys**
   - Reason: Use environment variables for all secrets

4. **❌ DO NOT modify `pyproject.toml` to downgrade package versions**
   - Reason: Project requires Python 3.12+ and latest packages

5. **❌ DO NOT use synchronous database calls**
   - Reason: Use async SQLAlchemy or async database driver

6. **❌ DO NOT skip input validation**
   - Reason: Always use Pydantic models for request/response validation

7. **❌ DO NOT create custom OpenAPI schema from scratch**
   - Reason: Use FastAPI's auto-generated OpenAPI 3.1

8. **❌ DO NOT expose stack traces or sensitive errors to clients**
   - Reason: Return generic error messages, log details server-side

9. **❌ DO NOT skip testing**
   - Reason: All endpoints must have pytest tests

10. **❌ DO NOT copy code from GenAI/Gemini/Flask projects**
    - Reason: Zero Copy Policy - write original FastAPI code

---

## 🎯 **SUCCESS CRITERIA**

### **Functional Requirements:**

- ✅ All 6 endpoints operational and returning correct responses
- ✅ User registration creates user in PostgreSQL `users` table
- ✅ User login validates credentials and returns JWT token
- ✅ GET `/api/auth/me` requires valid JWT token
- ✅ Health check returns service status
- ✅ OpenAPI YAML downloadable at `/api/openapi.yaml`

### **Quality Requirements:**

- ✅ Zero linting errors (black, isort, flake8 all pass)
- ✅ Test coverage ≥ 80% (`pytest --cov=app --cov-report=term-missing`)
- ✅ All requests/responses validated with Pydantic
- ✅ Type hints on all functions
- ✅ Docstrings on all public functions

### **Documentation Requirements:**

- ✅ Swagger UI accessible at `/api/docs`
- ✅ ReDoc accessible at `/redoc`
- ✅ All endpoints have descriptions and examples
- ✅ Security schemes documented (bearerAuth)
- ✅ All response codes documented (200, 201, 400, 401, 409)

### **Security Requirements:**

- ✅ Passwords hashed with bcrypt (12+ rounds)
- ✅ JWT tokens signed with secret from environment variable
- ✅ Protected endpoints validate JWT tokens
- ✅ No secrets hardcoded in code
- ✅ Generic error messages (no stack traces exposed)

### **Testing Verification:**

```powershell
# Run from src/backend/
pytest tests/ -v --cov=app --cov-report=term-missing --cov-fail-under=80
black --check .
isort --check-only .
flake8 .
```

### **Manual Testing:**

```bash
# 1. Start server
uvicorn app.main:app --reload

# 2. Test health check
curl http://localhost:8000/health

# 3. Test root endpoint
curl http://localhost:8000/

# 4. Register user
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"SecurePass123!","role":"USER"}'

# 5. Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"SecurePass123!"}'

# 6. Get current user (replace TOKEN with actual JWT)
curl http://localhost:8000/api/auth/me \
  -H "Authorization: Bearer TOKEN"

# 7. Access Swagger UI
# Open browser: http://localhost:8000/api/docs

# 8. Download OpenAPI YAML
curl http://localhost:8000/api/openapi.yaml -o openapi.yaml
```

---

## 📦 **DELIVERABLES**

1. **Source Code:**
   - `app/main.py` - FastAPI app initialization
   - `app/config.py` - Configuration management
   - `app/routers/health.py` - Health endpoint
   - `app/routers/auth.py` - Authentication endpoints
   - `app/models/auth.py` - Pydantic models
   - `app/services/auth_service.py` - Authentication logic
   - `app/utils/jwt_handler.py` - JWT utilities
   - `app/utils/password.py` - Password hashing utilities

2. **Tests:**
   - `tests/test_health.py` - Health endpoint tests
   - `tests/test_auth.py` - Authentication tests
   - `tests/conftest.py` - Pytest fixtures

3. **Documentation:**
   - Interactive Swagger UI at `/api/docs`
   - ReDoc at `/redoc`
   - OpenAPI 3.1 YAML at `/api/openapi.yaml`

4. **Configuration:**
   - `.env.example` - Environment variables template

---

## 🚀 **NEXT STEPS (Future Work Items)**

After completing this work item:

1. **Database Integration** - Connect to real PostgreSQL database
2. **RAG Endpoints** - Implement policy ingestion and query endpoints
3. **OpenAI Integration** - Add embeddings and LLM completion
4. **Qdrant Integration** - Add vector search capabilities
5. **Audit Logging** - Track all user queries
6. **Rate Limiting** - Add API rate limits
7. **Deployment** - Podman container configuration

---

## 📚 **REFERENCES**

* **FastAPI Documentation:** <https://fastapi.tiangolo.com/>
* **Pydantic Documentation:** <https://docs.pydantic.dev/latest/>
* **OpenAPI 3.1 Spec:** <https://swagger.io/specification/>
* **JWT Best Practices:** <https://tools.ietf.org/html/rfc7519>
* **Project Repository:** <https://github.com/Srivari-Hema-SSPL-2026/enterprise-policy-assistant>

---

**Work Item Created By:** GitHub Copilot (SMART Framework)  
**Review Required:** Yes  
**Estimated Completion:** 8 hours  
**Dependencies:** PostgreSQL database (already configured), Python 3.12+ environment  
