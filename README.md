# Cloud API Test Automation Framework

![API Tests](https://github.com/BrettBlomb/cloud-api-test-automation/actions/workflows/api-tests.yml/badge.svg)

A Python-based API test automation framework built with **Pytest** to validate live REST APIs using reusable clients, environment-driven configuration, and clearly defined smoke and regression test coverage.

This project focuses on **how API automation frameworks are designed and maintained**, not just on executing tests.

---

## 📌 Project Overview

This framework performs real integration testing against a live REST API, validating:

- Service availability (health checks)
- API response behavior
- Data structure and contracts
- Access behavior and error handling

The project is structured to run consistently both **locally and in CI**, making it suitable for production-like testing workflows.

---

## 🧪 Test Strategy

The test suite is intentionally split to reflect real-world QA practices:

- **Smoke Tests**
  - Quick checks to confirm the service is reachable
  - Used for fast feedback before deeper testing

- **Regression Tests**
  - Validate core API behavior and data structure
  - Ensure changes do not break existing contracts

- **Schema / Contract Validation**
  - Confirms required fields and data types are present
  - Helps detect breaking API changes early

---

## 🧱 Project Structure
cloud-api-test-automation/
├── tests/
│ ├── conftest.py # Shared Pytest fixtures
│ ├── test_health.py # Smoke tests
│ ├── test_data.py # Regression tests
│ └── test_schema.py # Schema validation
│
├── utils/
│ ├── api_client.py # Reusable API client with timeouts
│ └── config.py # Environment-based configuration
│
├── reports/ # Generated test reports
├── requirements.txt
├── pytest.ini
└── README.md

This layout mirrors how API automation frameworks are typically organized on QA and SDET team
---

## 🔧 Tech Stack

- **Language:** Python  
- **Test Framework:** Pytest  
- **HTTP Client:** requests  
- **Reporting:** pytest-html  
- **CI/CD:** GitHub Actions  
- **Testing Type:** API integration testing  

---

## ▶️ Running the Tests Locally

1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```
2. Run all tests:
 ```bash
python -m pytest -v
```
3. Run only smoke tests:
```bash
python -m pytest -m smoke
```
4. Run only regression tests:
```bash
python -m pytest -m regression
```
5. Generate an HTML report:
```bash
python -m pytest --html=reports/report.html --self-contained-html
```
---
## 🤖 CI Automation

The test suite is automated using **GitHub Actions**, allowing tests to run consistently in a CI environment without manual intervention.

The CI workflow:
- Runs on every push and pull request
- Supports scheduled execution
- Executes the full API test suite
- Generates an HTML test report
- Publishes pass/fail status via a repository badge

This setup ensures fast feedback and helps catch API issues early in the development cycle.

---

## 📊 Test Reporting

Test execution results are captured using **pytest-html**.

Each test run produces:
- A self-contained HTML report
- Clear pass/fail visibility for each test
- Detailed information to help troubleshoot failures

Reports can be generated locally or attached as CI artifacts for review.

---

## 🎯 Why This Project Exists

This project was built to demonstrate how API test automation can be designed as a maintainable and scalable system rather than a collection of one-off tests.

The focus is on:
- Reusable test infrastructure
- Clear test strategy (smoke vs regression)
- Reliable execution in CI environments
- Easy-to-understand test results

The goal is to show ownership of quality and testing strategy, not just test execution.

---

## 📈 Future Enhancements

Potential future improvements include:
- Contract testing using OpenAPI or Schemathesis
- Performance and load testing
- Authentication and authorization validation
- Cloud-based storage for test artifacts

These were intentionally left out to keep the framework focused and stable.

---

## 📫 Contact

Built and maintained by **Brett Blomberg**

- GitHub: https://github.com/BrettBlomb
- LinkedIn: https://www.linkedin.com/in/brett-blomberg/
