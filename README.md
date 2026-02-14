# Data Structures and Algorithms in Python

[![License](https://img.shields.io/badge/License-MIT-purple)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Focus](https://img.shields.io/badge/Focus-DSA%20%7C%20Problem%20Solving-orange)](#)
[![Maintainer](https://img.shields.io/badge/Maintainer-Viswanatha%20Swamy%20P%20K-blue)](#)

A structured, implementation-focused journey through **Data Structures and Algorithms using Python**.

This repository is designed for:

* Students preparing for technical interviews
* Engineers strengthening problem-solving skills
* Developers building algorithmic thinking
* Backend/AI engineers revisiting computational foundations

---

## 📑 Table of Contents

* [Abstract](#-abstract)
* [Learning Objectives](#-learning-objectives)
* [Curriculum Structure](#-curriculum-structure)
* [Topics Covered](#-topics-covered)
* [Complexity Analysis Philosophy](#-complexity-analysis-philosophy)
* [Repository Structure](#-repository-structure)
* [Execution Guide](#-execution-guide)
* [Coding Standards](#-coding-standards)
* [Problem Solving Methodology](#-problem-solving-methodology)
* [Success Criteria](#-success-criteria)
* [License](#-license)

---

## 📌 Abstract

This repository provides a **systematic, bottom-up approach** to mastering Data Structures and Algorithms using Python.

The curriculum emphasizes:

* Strong fundamentals
* Time and Space Complexity mastery
* Clean implementation
* Pattern recognition
* Interview-grade problem solving
* Real-world engineering relevance

Rather than memorizing solutions, this repo focuses on **thinking models, trade-offs, and computational efficiency**.

---

## 🎯 Learning Objectives

By completing this repository, learners will:

* Understand **Big-O analysis** rigorously
* Implement core data structures from scratch
* Analyze algorithmic trade-offs
* Master recursion and problem decomposition
* Recognize common problem-solving patterns
* Solve interview-level problems confidently
* Write clean, testable Python implementations

---

## 🗂 Curriculum Structure

This repository is divided into **7 structured modules**:

```
01_complexity_analysis
02_arrays_and_strings
03_recursion_and_backtracking
04_linked_list_stack_queue
05_searching_and_sorting
06_trees_and_binary_search_tree
07_hashing_and_problem_patterns
```

Each module contains:

* Concept notes
* Implementation files
* Practice problems
* Interview-style challenges

---

## 📚 Topics Covered

### 1️⃣ Complexity Analysis

* Time Complexity
* Space Complexity
* Asymptotic Notations (O, Ω, Θ)
* Recurrence Relations
* Amortized Analysis

---

### 2️⃣ Arrays & Strings

* Static vs Dynamic arrays
* Two Pointer technique
* Sliding Window
* Prefix Sum
* In-place transformations

---

### 3️⃣ Recursion & Backtracking

* Call stack mechanics
* Tail recursion
* Divide & Conquer
* Subsets / Permutations
* Constraint-based search

---

### 4️⃣ Linked List, Stack & Queue

* Singly & Doubly Linked List
* Stack implementation (Array & Linked List)
* Queue / Circular Queue
* Deque
* LIFO vs FIFO semantics

---

### 5️⃣ Searching & Sorting

* Linear & Binary Search
* Merge Sort
* Quick Sort
* Heap Sort
* Stability & In-place analysis

---

### 6️⃣ Trees & Binary Search Tree

* Tree traversal (DFS, BFS)
* Binary Tree properties
* BST operations
* Height & Depth analysis
* Recursive tree problems

---

### 7️⃣ Hashing & Problem-Solving Patterns

* Hash Tables in Python
* Collision handling
* Frequency maps
* Pattern recognition
* Interview templates

---

## 🧠 Complexity Analysis Philosophy

This repository emphasizes:

* **Every solution must include complexity analysis**
* Compare brute-force vs optimized solution
* Identify space-time trade-offs
* Understand worst-case vs average-case

We treat complexity analysis as a **first-class engineering skill**, not an afterthought.

---

## 📂 Repository Structure

```
dsa-foundations-in-python/
│
├── 01_complexity_analysis/
│   ├── notes.md
│   ├── examples.py
│   └── exercises.py
│
├── 02_arrays_and_strings/
│   ├── theory.md
│   ├── implementations.py
│   └── problems.py
│
├── 03_recursion_and_backtracking/
├── 04_linked_list_stack_queue/
├── 05_searching_and_sorting/
├── 06_trees_and_binary_search_tree/
├── 07_hashing_and_problem_patterns/
│
├── tests/
├── practice_sets/
├── docs/
└── README.md
```

---

## ▶️ Execution Guide

### Prerequisites

* Python 3.12+
* Basic Python syntax knowledge

### Clone Repository

```bash
git clone https://github.com/<your-username>/dsa-foundations-in-python.git
cd dsa-foundations-in-python
```

### Run a Module

```bash
cd 02_arrays_and_strings
python implementations.py
```

### Run Tests (Optional)

```bash
pytest
```

---

## 🧾 Coding Standards

All implementations follow:

* Clear function signatures
* Docstrings for explanation
* Type hints
* Edge case handling
* Complexity comments at the bottom

Example:

```python
def binary_search(arr: list[int], target: int) -> int:
    """
    Performs binary search on a sorted array.
    Returns index of target if found, else -1.
    """
```

---

## 🧩 Problem Solving Methodology

Every problem should follow this approach:

1. Clarify constraints
2. Identify brute-force approach
3. Optimize step-by-step
4. Analyze complexity
5. Test edge cases
6. Refactor for readability

We prioritize **clarity before cleverness**.

---

## 🏁 Success Criteria

A learner is considered proficient when they can:

* Solve medium-level problems in under 30 minutes
* Derive time complexity without guesswork
* Recognize patterns immediately
* Write implementation without syntax struggle
* Explain trade-offs confidently

---

## 📜 License

Licensed under MIT License.

---

## 💡 Instructor Note

Data Structures and Algorithms are not just for interviews.

They shape:

* System design thinking
* Performance engineering
* Backend optimization
* Distributed systems understanding
* AI/ML data pipeline efficiency

Mastering DSA builds long-term engineering depth.
