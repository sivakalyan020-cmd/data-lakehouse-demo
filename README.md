# Secure Data Lakehouse Pipeline & Quality Platform Demo

This repository contains a minimal demonstration of the architecture proposed in the research report for JPMorgan Data Engineer III. The goal of the demo is to illustrate how to combine Airflow orchestration, Great Expectations for data validation, open table formats (Hudi or Iceberg), CI/CD, and Kubernetes infrastructure into a cohesive data engineering platform.

## Contents

- `airflow_dags/demo_dag.py` – An example Airflow DAG that ingests sample data, runs validation using Great Expectations, and writes to a placeholder lakehouse layer.
- `expectations/demo_expectations.py` – A simple Great Expectations suite used by the DAG to validate data.
- `helm-chart/` – A skeleton Helm chart for deploying the platform components to Kubernetes.
- `.github/workflows/ci.yml` – A simple CI pipeline that runs minimal checks.
- `requirements.txt` – Python dependencies for the demo.

See the accompanying report for details on the architecture and rationale.
