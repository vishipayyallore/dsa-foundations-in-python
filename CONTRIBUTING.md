# Contributing to DSA Foundations in Python

Thank you for your interest in contributing to this Data Structures and Algorithms learning repository! This guide will help you get started.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Code Standards](#code-standards)
- [Submitting Changes](#submitting-changes)

---

## Code of Conduct

This project follows a **zero-copy policy** to ensure all content is original and demonstrates understanding rather than memorization. When contributing:

- **No copy-paste** from LeetCode, HackerRank, or other solution sites
- Solutions must demonstrate **understanding**, not just memorization
- Comments should reflect **personal understanding**
- Code must be **original implementations**

---

## How Can I Contribute?

### 1. Reporting Bugs

Found a bug in an implementation or test? Please:

- Check if the issue already exists
- Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md)
- Include clear steps to reproduce
- Provide error messages and environment details

### 2. Suggesting Enhancements

Have ideas for improvements? You can suggest:

- New data structures or algorithms
- Additional practice problems
- Better explanations or examples
- Improved test coverage
- Documentation enhancements

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md)

### 3. Improving Content

Spotted unclear explanations or missing information?

- Use the [Content Improvement template](.github/ISSUE_TEMPLATE/content_improvement.md)
- Suggest clearer explanations
- Add better examples
- Improve complexity analysis

### 4. Contributing Code

Want to implement new problems or data structures? Great! Follow the guidelines below.

---

## Getting Started

### Prerequisites

- **Python 3.12+** installed
- **Git** for version control
- Familiarity with DSA concepts

### Setting Up Your Development Environment

1. **Fork the repository**

   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR-USERNAME/dsa-foundations-in-python.git
   cd dsa-foundations-in-python
   ```

2. **Create a virtual environment**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Create a branch for your work**

   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## Contribution Guidelines

### Zero-Copy Policy

All contributions must be original work:

- ✅ **Original implementations** based on understanding
- ✅ **Transformative content** with personal insights
- ✅ **Educational explanations** in your own words
- ❌ Copy-paste from coding challenge sites
- ❌ Direct translations from other languages without understanding
- ❌ Solutions memorized without comprehension

### Content Structure

Each module should contain:

- **Theory files** (`notes.md`, `theory.md`) - Concept explanations
- **Implementation files** (`implementations.py`) - Data structure/algorithm implementations
- **Problem files** (`problems.py`) - Practice problems
- **Test files** (`tests/test_*.py`) - Comprehensive unit tests

### Adding a New Problem

1. **Place in appropriate module** (e.g., `02_arrays_and_strings/`)
2. **Include problem statement** in docstring
3. **Provide multiple approaches** (brute-force + optimized)
4. **Add complexity analysis** for each approach
5. **Write comprehensive tests** in `tests/` directory
6. **Handle edge cases** (empty input, single element, duplicates)
7. **Update module README** if present

Example structure:

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target.
    
    Approach 1: Brute Force
    - Check all pairs: O(n²) time, O(1) space
    
    Approach 2: Hash Table
    - Store complements: O(n) time, O(n) space
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        Indices of the two numbers
    
    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    # Implementation here
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
```

### Adding a New Data Structure

1. **Implement core operations** (insert, delete, search, etc.)
2. **Add time/space complexity comments** for each operation
3. **Provide usage examples** in docstring
4. **Write unit tests** covering all operations
5. **Include edge case handling**
6. **Compare with Python built-ins** when applicable

### Adding Tests

Tests should cover:

- ✅ **Happy path** - Normal expected inputs
- ✅ **Edge cases** - Empty, single element, maximum size
- ✅ **Boundary conditions** - Min/max values
- ✅ **Invalid inputs** - Wrong types, out of range
- ✅ **Performance** - Large inputs where applicable

---

## Code Standards

### Python Style

- **Follow PEP 8** strictly
- **Type hints** required for all function signatures
- **Docstrings** required for all public functions and classes
- **Line length**: Max 88 characters (Black formatter)
- **Imports**: Organized (standard lib, third-party, local)

### Required Elements

Every solution MUST include:

```python
# Time Complexity: O(...) - explanation
# Space Complexity: O(...) - explanation
# Where n = description of input size variable
```

### Code Quality Checklist

Before submitting:

- [ ] Code follows PEP 8
- [ ] Type hints on all functions
- [ ] Comprehensive docstrings
- [ ] Complexity analysis included
- [ ] Variable names are descriptive
- [ ] Tests written and passing
- [ ] All edge cases handled
- [ ] No linting errors

### Running Quality Checks

```powershell
# Format code
black .

# Check imports
isort .

# Lint code
flake8 . --max-line-length=88 --exclude=.venv

# Type check (optional)
mypy . --exclude=.venv

# Run tests
pytest

# Check coverage
pytest --cov=. --cov-report=html
```

---

## Submitting Changes

### Pull Request Process

1. **Ensure all tests pass**

   ```powershell
   pytest
   ```

2. **Format your code**

   ```powershell
   black .
   isort .
   ```

3. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request**
   - Use the [PR template](.github/pull_request_template.md)
   - Fill out all relevant sections
   - Link related issues
   - Provide clear description

5. **Respond to feedback**
   - Address review comments
   - Make requested changes
   - Update tests if needed

### PR Review Criteria

Your PR will be reviewed for:

- **Originality**: No copy-paste violations
- **Code quality**: Follows standards and best practices
- **Testing**: Comprehensive test coverage (90%+)
- **Documentation**: Clear explanations and complexity analysis
- **Learning value**: Demonstrates understanding and teaches concepts

---

## Questions?

- **Issues**: Open an issue for questions or clarifications
- **Discussions**: Use GitHub Discussions for general questions
- **Email**: Contact maintainers for private concerns

---

## Recognition

All contributors will be recognized in project acknowledgments. Thank you for helping improve DSA learning for everyone!

---

**Remember**: The goal is understanding, not just working code. Focus on building mental models and pattern recognition.

Happy coding! 🚀
