# S.M.A.R.T. Prompt Framework for GitHub Copilot Coding Agents

**Enterprise Policy Assistant Edition** - Framework for creating high-quality coding agent instructions aligned with prompt engineering best practices and OpenAI + Qdrant integration patterns.

---

## 🎯 **The S.M.A.R.T. Framework**

Use this framework to create highly effective coding agent instructions:

```text
S - Specific Role Definition (Senior Python Developer, Frontend Engineer, AI Integration Specialist, etc.)
M - Mission-Critical Requirements (What must be accomplished with measurable outcomes)
A - Audience-Aware Communication (Team expertise level, architectural maturity, domain context)
R - Response Format Control (Code structure, architecture patterns, documentation style)
T - Task-Oriented Constraints (Technology stack, architectural patterns, forbidden actions)
```

---

## 🏛️ **RAG System Alignment**

When creating prompts, consider:

- **Prompt Pattern**: Is this instruction-based, role-based, chain-of-thought, or evaluation?
- **Use Case Context**: What task type (policy retrieval, document ingestion, embeddings, authentication)?
- **OpenAI Integration**: Which integration pattern (Python SDK, ChatCompletion, Embeddings)?
- **Qdrant Integration**: Vector search, payload filtering, or collections management?

## 🏗️ **Advanced Problem Statement Template**

Use this enhanced template for coding agent tasks:

```markdown
## ROLE DEFINITION

You are a [Specific Role] specializing in [Technology Stack] with expertise in [Domain Areas]

## MISSION

[Clear, specific objective with measurable outcomes]

## CONTEXT

[Brief overview of current situation and progress made]

## CURRENT STATUS

- **Progress Made**: [Specific achievements and metrics]
- **Main Issue**: [Root cause analysis]
- **Files Affected**: [List specific files]

## REMAINING WORK

### 1. [Priority Task Name] (Priority N)

- **Problem**: [Specific technical issue]
- **Current Error**: [Exact error messages]
- **Solution Approach**: [Concrete implementation steps]
- **Files to Modify**: [Specific file paths]

## TECHNICAL CONSTRAINTS

- **🚨 CRITICAL**: [Non-negotiable requirements]
- **Framework**: [Technology stack requirements]
- **Dependencies**: [Package/version constraints]

## RESPONSE FORMAT REQUIREMENTS

- [Specific code structure expectations]
- [Documentation requirements]
- [Testing requirements]

## WHAT NOT TO DO

- ❌ [Explicit forbidden actions with reasoning]

## WHAT TO DO

- ✅ [Explicit required actions with priority]

## SUCCESS CRITERIA

[Measurable outcomes with acceptance criteria]
```

## 🎭 **Role-Based Specialization Examples**

### **For Backend (Python/FastAPI) Development:**

```markdown
ROLE: You are a Senior Python Developer specializing in FastAPI REST API development, OpenAI API integration, and Qdrant Vector Database
EXPERTISE FOCUS: FastAPI route handlers, Pydantic models, async programming, RAG pipelines
```

### **For Frontend (TypeScript/React) Development:**

```markdown
ROLE: You are a Frontend Engineer specializing in React 19 with TypeScript, chat interfaces, and document management UI
EXPERTISE FOCUS: React hooks, component composition, state management, Tailwind CSS
```

### **For AI Integration & RAG Pipeline:**

```markdown
ROLE: You are an AI Integration Specialist specializing in OpenAI Embeddings, Qdrant Vector Search, and RAG Architecture
EXPERTISE FOCUS: 
- Embedding generation and vector storage
- Semantic search optimization
- Context-aware prompt construction
- Document chunking strategies
```

## 🚨 **Critical Constraint Guidelines**

### **Framework/Package Versions:**

```markdown
- 🚨 CRITICAL: Use Python 3.12+ ONLY
- 🚨 CRITICAL: Use React 19+ with TypeScript
- ❌ DO NOT modify pyproject.toml to downgrade packages
```

### **Effective Instruction Patterns**

- ✅ "Implement the `/ingest` endpoint in FastAPI to process PDF files and store embeddings in Qdrant."
- ✅ "Create a React component `ChatInterface.tsx` that displays cited sources from the RAG response."

## 🤖 **OpenAI & Qdrant Integration Framework**

### **RAG Integration Template:**

```markdown
## RAG INTEGRATION FRAMEWORK

### Integration Requirements
- **API Key Management**: Environment variables (OPENAI_API_KEY, QDRANT_URL)
- **Chunking**: Implement intelligent text chunking with overlap
- **Embeddings**: Use text-embedding-3-small (or configured model)
- **Vector Search**: Query Qdrant with cosine similarity

### Success Criteria
- Documents successfully ingested and vectorized
- Semantic search returns relevant context
- LLM generates accurate, grounded answers
- No API keys exposed
```

## 📋 **Universal PR Success Template**

```markdown
## 🎯 MANDATORY SUCCESS CRITERIA

### Backend Build Requirements
```powershell
# MUST PASS: Backend tests
cd src/backend
pytest tests/ -v
```

### Frontend Build Requirements

```powershell
# MUST PASS: Frontend build
cd src/frontend
npm run build
```

## 🚀 **Enterprise Policy Assistant Example**

```markdown
ROLE: You are a Senior Full-Stack Developer specializing in RAG applications
MISSION: Implement document ingestion pipeline using FastAPI, OpenAI, and Qdrant
TASK CONSTRAINTS:
- 🚨 CRITICAL: Maintain N-Tier architecture separation
- Architecture: Frontend -> FastAPI -> OpenAI/Qdrant
- Quality Standards: Zero build errors
```
