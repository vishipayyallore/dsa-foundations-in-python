# GitHub Copilot Instructions for DSA Foundations in Python

**Version**: 1.0  
**Last Updated**: February 13, 2026  
**Repository**: `dsa-foundations-in-python`

**Environment**: Windows 11, PowerShell  
**Note**: All commands and scripts should use PowerShell syntax. File paths use Windows format.

---

## 🎯 Repository Purpose

**DSA Foundations in Python** is a structured, implementation-focused learning repository for mastering Data Structures and Algorithms using Python 3.12+.

### What This Repository Provides

- **7 Structured Learning Modules**: From complexity analysis to advanced problem patterns
- **Interview Preparation**: Practice problems with solution patterns
- **Complexity-First Approach**: Every solution includes time/space analysis
- **Clean Python Implementations**: Type hints, docstrings, and best practices
- **Pattern Recognition**: Common algorithms and data structure patterns
- **Test-Driven Learning**: Unit tests for validation

### Target Audience

- Students preparing for technical interviews
- Software engineers strengthening problem-solving skills
- Backend/AI engineers revisiting computational foundations
- Developers building algorithmic thinking

### Learning Value

- Rigorous Big-O analysis and complexity reasoning
- Pattern recognition for interview problems
- Trade-off analysis between different approaches
- Clean, production-quality Python implementations
- Engineering depth beyond memorization

---

## 📁 Repository Structure

> **📖 Single Source of Truth**: For complete structure, see [README.md](../README.md)

**Quick Reference:**

```
01_complexity_analysis/       # Big-O, asymptotic notation, recurrence
02_arrays_and_strings/        # Two pointers, sliding window, prefix sum
03_recursion_and_backtracking/# Call stack, divide & conquer, subsets
04_linked_list_stack_queue/   # Linked structures, LIFO/FIFO semantics
05_searching_and_sorting/     # Binary search, merge/quick/heap sort
06_trees_and_binary_search_tree/  # Tree traversal, BST operations
07_hashing_and_problem_patterns/  # Hash tables, frequency maps
tests/                        # Unit tests for all implementations
practice_sets/                # Additional problems and challenges
docs/                         # Supporting documentation
```

---

## 🔧 Development Guidelines

### Zero-Copy Policy

- All code must be original implementations for learning purposes
- No copy-paste from LeetCode, HackerRank, or other solution sites
- Solutions must demonstrate understanding, not memorization
- Educational transformations are encouraged (explain trade-offs)
- Comments should reflect personal understanding

### Project Focus

This is a **learning-focused DSA repository** that:

- Implements fundamental data structures from scratch
- Analyzes algorithmic complexity rigorously
- Emphasizes pattern recognition and problem-solving methodology
- Provides clean, testable Python implementations
- Prepares learners for technical interviews and engineering depth

### Current State

- ✅ Project planning and documentation complete
- ✅ Repository structure defined
- ⏳ Module implementations - In Progress
- ⏳ Test suite development - In Progress
- ⏳ Practice problems collection - In Progress

### Code Quality Standards

#### Python Style
- **Follow PEP 8** strictly
- **Type hints**: Use for all function signatures
- **Docstrings**: Required for all public functions, classes
- **Variable names**: Descriptive, no single-letter names except loop counters
- **Line length**: Max 88 characters (Black formatter standard)
- **Imports**: Organized (standard lib, third-party, local)

#### Complexity Analysis Requirements
Every solution MUST include:
```python
# Time Complexity: O(n log n) - explanation of why
# Space Complexity: O(n) - explanation of auxiliary space used
# Where n = length of input array
```

#### Solution Structure
```python
def problem_name(input_param: type) -> return_type:
    """
    Brief description of what the function does.
    
    Approach:
    - Step 1: Explain approach
    - Step 2: Key insight or optimization
    
    Args:
        input_param: Description of parameter
    
    Returns:
        Description of return value
    
    Examples:
        >>> problem_name([1, 2, 3])
        expected_output
    """
    # Implementation here
    
    # Time Complexity: O(...)
    # Space Complexity: O(...)
```

### When Adding New Content

#### Adding a New Problem
1. Place in appropriate module folder
2. Include problem statement as docstring
3. Provide at least 2 approaches (brute-force + optimized)
4. Add comprehensive tests in `tests/` directory
5. Include edge cases (empty input, single element, duplicates)
6. Add complexity analysis for each approach
7. Update module README if present

#### Adding a New Data Structure
1. Implement core operations (insert, delete, search, etc.)
2. Add time/space complexity comments for each operation
3. Provide usage examples in docstring
4. Write unit tests covering all operations
5. Include edge case handling
6. Compare with Python built-in alternatives

#### Adding a New Algorithm
1. Start with brute-force approach
2. Optimize incrementally (document each step)
3. Explain trade-offs between approaches
4. Provide visual/mental model in comments
5. Add test cases with varying input sizes
6. Benchmark if performance-critical

### File Naming Conventions

- **Module folders**: Use `##_descriptive_name/` (e.g., `02_arrays_and_strings/`)
- **Theory files**: `notes.md`, `theory.md`, `concepts.md`
- **Implementation files**: `implementations.py`, `solutions.py`
- **Problem files**: `problems.py`, `exercises.py`
- **Test files**: `test_<module_name>.py` (e.g., `test_arrays.py`)
- Keep names descriptive and consistent within each module

### Error Handling

- Validate input parameters (type, range, null checks)
- Raise appropriate exceptions with descriptive messages
  - `ValueError`: Invalid input values
  - `TypeError`: Wrong input types
  - `IndexError`: Out of bounds access
- Document preconditions in docstrings
- Handle edge cases gracefully

### Testing Requirements

#### Unit Test Standards
- Use `pytest` as the testing framework
- Aim for 90%+ code coverage
- Test structure:
  ```python
  def test_function_name():
      # Arrange
      input_data = ...
      expected = ...
      
      # Act
      result = function_name(input_data)
      
      # Assert
      assert result == expected
  ```

#### Test Coverage
- **Happy path**: Normal, expected inputs
- **Edge cases**: Empty, single element, maximum size
- **Boundary conditions**: Min/max values, overflow
- **Invalid inputs**: Null, wrong type, out of range
- **Performance**: Large inputs where applicable

#### Running Tests
```powershell
# Run all tests
pytest

# Run specific module tests
pytest tests/test_arrays.py

# Run with coverage
pytest --cov=. --cov-report=html

# Run with verbose output
pytest -v
```

### Documentation Standards

- Keep README.md current with new modules/problems
- Use Markdown for all documentation
- Include visual diagrams where helpful (ASCII art acceptable)
- Provide complexity analysis in plain English
- Add "Why this matters" context for engineering relevance
- Update Table of Contents when adding sections

### Problem-Solving Methodology

When implementing solutions, follow this structured approach:

#### 1. Clarify
- Understand problem constraints
- Identify input/output format
- Ask clarifying questions (as comments)

#### 2. Brute Force
- Start with simplest working solution
- Document why it's inefficient
- Analyze complexity

#### 3. Optimize
- Identify bottlenecks
- Consider data structure alternatives
- Apply known patterns (two pointers, sliding window, etc.)

#### 4. Implement
- Write clean, readable code
- Use meaningful variable names
- Add inline comments for complex logic

#### 5. Test
- Write comprehensive test cases
- Test edge cases
- Verify complexity claims with larger inputs

#### 6. Refactor
- Improve readability
- Remove redundancy
- Ensure consistency with codebase style

### Quality Assurance Checklist

Before committing code, verify:

#### Code Quality
- [ ] Follows PEP 8 style guide
- [ ] Type hints on all function signatures
- [ ] Comprehensive docstrings present
- [ ] No linting errors (`pylint` or `flake8`)
- [ ] Complexity analysis included
- [ ] Variable names are descriptive

#### Testing
- [ ] Unit tests written and passing
- [ ] Edge cases covered
- [ ] Tests are documented
- [ ] Coverage is adequate (90%+)

#### Documentation
- [ ] Problem statement clear
- [ ] Approach explained
- [ ] Examples provided
- [ ] Complexity justified
- [ ] Trade-offs discussed

#### Learning Value
- [ ] Demonstrates understanding (not just memorization)
- [ ] Compares multiple approaches
- [ ] Explains "why" not just "how"
- [ ] Applicable to similar problems

---

## 🧠 DSA-Specific Guidelines

### Complexity Analysis Best Practices

#### Time Complexity
- Count primitive operations (comparisons, assignments, arithmetic)
- Identify loops and recursion depth
- Use Master Theorem for divide-and-conquer
- Consider best, average, and worst cases
- Explain in terms of input size variables

#### Space Complexity
- Count auxiliary space (not input)
- Include recursion call stack
- Identify space-time trade-offs
- Mention in-place vs out-of-place

#### Common Complexities to Recognize
```python
O(1)       # Constant - hash table lookup, array access
O(log n)   # Logarithmic - binary search, balanced tree operations
O(n)       # Linear - single array traversal
O(n log n) # Linearithmic - efficient sorting (merge, heap)
O(n²)      # Quadratic - nested loops, bubble sort
O(2ⁿ)      # Exponential - recursive subsets, fibonacci (naive)
O(n!)      # Factorial - permutations
```

### Pattern Recognition Guide

#### Two Pointers
- Sorted array problems
- Palindrome checking
- Pair finding with target sum
- In-place array manipulation

#### Sliding Window
- Subarray/substring problems
- Fixed or variable window size
- Optimization problems (max/min)

#### Fast & Slow Pointers
- Cycle detection (linked list)
- Middle element finding
- Intersection problems

#### Recursion & Backtracking
- Tree/graph traversal
- Combinatorial problems (subsets, permutations)
- Constraint satisfaction

#### Dynamic Programming Recognition
- Optimal substructure present
- Overlapping subproblems
- Optimization or counting problems
- Consider memoization first, then tabulation

### Data Structure Selection Guide

| Problem Type | Consider | Avoid |
|-------------|----------|-------|
| Fast lookup | Hash table, BST | Unsorted array |
| Order matters | Array, Linked list | Set |
| Range queries | Binary Indexed Tree, Segment tree | Hash table |
| Priority | Heap | Sorted array |
| LIFO operations | Stack | Queue |
| FIFO operations | Queue | Stack |
| Predecessor/Successor | BST | Hash table |

---

## 🚀 Running the System

### Quick Start

```powershell
# Clone repository
git clone https://github.com/vishipayyallore/dsa-foundations-in-python.git
cd dsa-foundations-in-python

# Set up Python environment (recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies (if any)
pip install -r requirements.txt

# Run a module
cd 02_arrays_and_strings
python implementations.py

# Run tests
pytest

# Run tests with coverage
pytest --cov=. --cov-report=html
```

### Development Workflow

1. **Start with theory**: Read `notes.md` in the module
2. **Study implementations**: Review `implementations.py`
3. **Practice problems**: Attempt `problems.py` independently
4. **Check solutions**: Compare your approach with provided solutions
5. **Run tests**: Validate understanding with unit tests
6. **Iterate**: Optimize and refactor

---

## 📋 Module-Specific Guidelines

### 01_complexity_analysis
- Focus on deriving time/space complexity
- Practice recurrence relations (Master Theorem)
- Understand amortized analysis
- Compare empirical vs theoretical complexity

### 02_arrays_and_strings
- Master two-pointer technique variations
- Understand sliding window optimization
- Practice in-place transformations
- Recognize prefix sum applications

### 03_recursion_and_backtracking
- Visualize call stack and base cases
- Identify recursive subproblems
- Optimize with memoization
- Understand constraint pruning in backtracking

### 04_linked_list_stack_queue
- Implement without using built-in collections
- Handle edge cases (empty, single node)
- Practice pointer manipulation carefully
- Understand when to use singly vs doubly linked

### 05_searching_and_sorting
- Implement sorts from scratch (no `sorted()` or `.sort()`)
- Understand stability implications
- Analyze space complexity (in-place vs auxiliary)
- Practice binary search variations

### 06_trees_and_binary_search_tree
- Master recursive and iterative traversals
- Understand BST invariants
- Practice tree construction from traversals
- Analyze height-balanced vs skewed trees

### 07_hashing_and_problem_patterns
- Understand hash function design
- Practice collision handling
- Use frequency maps effectively
- Recognize hashing patterns in problems

---

## 💡 Teaching Philosophy

When generating or reviewing code:

1. **Clarity over cleverness**: Readable code beats clever one-liners
2. **Explain trade-offs**: Why this approach over alternatives?
3. **Progressive optimization**: Show brute-force → optimized journey
4. **Real-world relevance**: Connect to engineering applications
5. **Systematic thinking**: Teach the "why" behind patterns
6. **Avoid spoilers**: Guide thinking without giving away solutions immediately

### For Interview Preparation
- Practice problem-solving methodology consistently
- Think aloud (add comment explaining thought process)
- Discuss alternatives and trade-offs
- Test with edge cases
- Optimize iteratively, not prematurely

### For Long-Term Learning
- DSA skills transfer to:
  - System design (choosing right data structures)
  - Performance optimization (complexity analysis)
  - Backend engineering (efficient algorithms)
  - AI/ML (understanding algorithmic foundations)
  - Distributed systems (consensus algorithms)

Mastering DSA builds **engineering depth**, not just interview skills.

---

## 📞 Support

- **Issues**: Use GitHub Issues for bug reports or clarifications
- **Discussions**: Ask questions about approaches or patterns
- **Pull Requests**: Contribute improvements or new problems
- **Documentation**: See [README.md](../README.md) for learning path

---

## 🎓 Success Indicators

A learner has achieved proficiency when they can:

- Derive time/space complexity without guesswork (< 2 minutes)
- Recognize patterns immediately (two pointers, sliding window, etc.)
- Implement medium-level problems in < 30 minutes
- Explain trade-offs between approaches confidently
- Write clean, testable code without syntax struggle
- Debug efficiently by reasoning about invariants

**Remember**: The goal is understanding, not memorization. Focus on building mental models and pattern recognition.

