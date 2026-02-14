# Enterprise Policy Assistant Repository Verification and Content Enhancement

## Context

You are working with **Enterprise Policy Assistant**, an N-Tier web application that enables employees to query enterprise policy documents using natural language. The repository implements a React.js with TypeScript frontend, FastAPI REST API backend, PostgreSQL database for metadata, Qdrant Vector Database for embeddings, and OpenAI API integration.

**Repository Structure:**

- `src/frontend/` - React.js 19 with TypeScript application
- `src/backend/` - FastAPI REST API with routes, services, and models
- `infra/` - Docker Compose and environment configuration
- `docs/` - Project documentation and architecture diagrams
- `.github/` - GitHub workflows and templates

**Primary Objective:**
Perform a COMPREHENSIVE audit of the repository using Enterprise Policy Assistant standards and quality criteria. Verify file contents, run structured checks, and produce actionable reports with suggestions and fixes.

---

## RAG System Verification Checks

### A. File Content Inspection

- Open and verify every file (no file skipped)
- Ensure markdown formatting compliance
- Check for completeness and consistency with project objectives
- Verify ZERO copy policy compliance (no copy-paste artifacts from other projects)

### B. Architecture Pattern Alignment

- Verify N-Tier architecture separation (Presentation, Application, Data, RAG Service layers)
- Validate frontend and backend are properly decoupled
- Check API endpoints follow RESTful conventions
- Ensure vector operations are handled by Qdrant integration
- Verify prompt engineering follows context-aware patterns

### C. Content Accuracy and Quality

- Verify technical correctness and OpenAI API alignment
- Ensure completeness for stated objectives
- Check alignment with RAG best practices
- Validate code examples are current, relevant, and runnable
- Verify TypeScript types and Python type hints are correct

### D. Project Metadata Requirements

Check for presence of:

- Component type designation (frontend, backend, database, rag-service)
- Use case description (policy retrieval, document ingestion)
- Clear objectives (specific, measurable)
- Code examples in TypeScript/React and Python/FastAPI

### E. Naming Convention Compliance

- Use PascalCase for React components: `ChatInterface.tsx`
- Use snake_case for Python files: `rag_service.py`
- Verify folder structure follows repository standards

### F. Broken Links and References

- Verify all internal cross-references work correctly
- Check README files and navigation structure

### G. Content Quality Standards

- Spellcheck and grammar verification
- Markdown formatting compliance (markdownlint standards)
- Code example correctness and completeness (FastAPI/React/Qdrant/OpenAI)

### H. Code Organization

- Verify proper placement in correct layer
- Check cross-references are accurate
- Verify N-Tier architecture separation maintained

---

## Output Requirements

### 1. SUMMARY

```json
{
  "repo_name": "enterprise-policy-assistant",
  "system_compliance_percentage": 0.0,
  "suggested_next_steps": ["step1", "step2"]
}
```

### 2. DETAILED_REPORT

For each file:

```json
{
  "file_path": "string",
  "issues": [
    {
      "severity": "high|medium|low",
      "description": "string",
      "suggested_fix": "string"
    }
  ],
  "overall_status": "compliant|needs_updates|remove"
}
```

## Start Now

Open every file in the repository tree, run Enterprise Policy Assistant-specific checks, and produce the structured JSON report following these requirements. Focus on N-Tier architecture compliance, RAG pipeline integration quality, and code example correctness.
