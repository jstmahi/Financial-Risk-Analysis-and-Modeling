# Financial Risk Analysis and Expected Loss Pipeline

## Overview

This repository contains an end-to-end, machine learning-powered credit risk modeling pipeline. Designed in compliance with the Internal Ratings-Based (IRB) approach of the Basel Accords, this project calculates **Expected Loss (EL)** for consumer loans.

The pipeline bridges the gap between raw financial data and actionable business intelligence, translating complex statistical probabilities into an intuitive, production-ready Credit Scorecard. This is particularly relevant for operations and data analysis within the banking and fintech sectors, where assessing creditworthiness accurately dictates capital reserve requirements.

## Business Value

Financial institutions must accurately estimate the risk of borrower default to maintain adequate capital reserves. This project calculates Expected Loss using the standard risk equation:

**Expected Loss (EL) = Probability of Default (PD) × Loss Given Default (LGD) × Exposure at Default (EAD)**

By moving beyond standard accuracy metrics and generating a business-facing Scorecard, this project allows credit operations teams to establish clear cutoff scores for loan approvals and rejections based on their risk appetite.

## Project Architecture

The project is structured sequentially across four main stages:

### 1\. Data Preprocessing & Feature Engineering

  * **Weight of Evidence (WoE) & Information Value (IV):** Continuous and categorical variables are binned using fine and coarse classing to handle non-linear relationships and missing data effectively.
  * **Dummy Variable Creation:** Significant variables are transformed into dummy variables for stable logistic regression modeling.

### 2\. Probability of Default (PD) & Credit Scorecard

  * **PD Modeling:** A Logistic Regression model predicts the likelihood of a borrower defaulting within a one-year timeframe.
  * **Scorecard Generation:** Statistical coefficients are scaled into a human-readable credit scorecard. This allows a layperson to interpret how specific borrower attributes (e.g., annual income, employment length) impact their final credit score.

### 3\. LGD & EAD Modeling

  * **Loss Given Default (LGD):** Modeled using a two-stage approach:
    1.  Logistic Regression to predict if any recovery is possible (\>0).
    2.  Linear Regression to estimate the actual recovery rate percentage.
  * **Exposure at Default (EAD):** Predicts the Credit Conversion Factor (CCF) to determine the total exposure amount at the exact time of default.

### 4\. Model Monitoring (Population Stability Index)

  * **PSI Check:** Evaluates whether the distribution of new loan applicants has shifted significantly compared to the training data. This automated check is crucial for determining when models have degraded and require retraining.


## Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed.

### Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/jstmahi/Financial-Risk-Analysis-and-Modeling.git
    cd Financial-Risk-Analysis
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Execution

The project is built using Jupyter Notebooks. To reproduce the pipeline, launch Jupyter and run the notebooks in sequential order from `L01` to `L04`:

```bash
jupyter notebook
```

## Future Enhancements

  * **Application Development:** Wrapping the serialized `.sav` models into a lightweight web application or REST API (using Streamlit or FastAPI) to allow users to input borrower details and receive instant credit scores and Expected Loss calculations.
  * **Code Modularization:** Refactoring notebook logic into object-oriented Python scripts for easier integration into automated CI/CD pipelines.

---

## 👨‍💻 Architected By

**Mahidhar Ramayanam** [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/mahidharramayanam)
