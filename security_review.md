# CodeAlpha Secure Coding Review

## Task 3 - Secure Coding Review

### Project Description

This project is a security review of a small Python Flask login application.

The purpose of the review is to identify security weaknesses in the source code, explain their risks, and provide recommendations and remediation.

## Application Reviewed

**File:** `vulnerable_app.py`

**Language:** Python

**Framework:** Flask

**Environment:** Kali Linux

## Security Findings

### 1. Hardcoded Secret Key

**Severity:** High

**Vulnerable Code:**

```python
app.secret_key = "my-secret-key-123"
