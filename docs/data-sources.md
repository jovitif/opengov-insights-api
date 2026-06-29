# Data Sources

## Overview

This document describes the external data sources currently supported by OpenGov Insights.

The initial version of the platform focuses on integrating municipal transparency data with the official fiscal reports submitted to the Brazilian National Treasury.

---

# Source 1 — Municipal Transparency Portal (Mossoró)

## Description

The Municipal Transparency Portal provides public administrative and financial data published by the Municipality of Mossoró.

This is considered the primary operational data source.

## Access Method

REST API

## Data Format

JSON

## Available Datasets

* Revenue
* Budget Expenses
* Execution Expenses
* Contracts
* Procurement
* Personnel Management

## Main Business Entities

### Revenue

Possible attributes

* Revenue Code
* Revenue Category
* Organization
* Date
* Amount

---

### Budget Expense

Possible attributes

* Expense Code
* Budget Classification
* Organization
* Amount
* Fiscal Year

---

### Execution Expense

Possible attributes

* Commitment Number
* Liquidation
* Payment
* Organization
* Supplier
* Amount
* Date

---

### Contract

Possible attributes

* Contract Number
* Supplier
* Supplier CNPJ
* Organization
* Start Date
* End Date
* Contract Amount

---

### Procurement

Possible attributes

* Procurement Number
* Procurement Type
* Organization
* Publication Date
* Winning Supplier

---

## Update Frequency

Defined by the municipality.

The pipeline should support periodic synchronization.

---

# Source 2 — SICONFI

## Description

SICONFI is the official fiscal reporting platform maintained by the Brazilian National Treasury.

It contains the financial reports officially submitted by municipalities.

Unlike the Municipal Transparency Portal, SICONFI is considered the official reporting source used for fiscal analysis.

## Access Method

REST API

## Data Format

JSON

## Initial Datasets

* RREO
* RGF
* DCA
* MSC
* Entities

---

## Main Business Entities

### RREO

Contains summarized budget execution information.

Examples

* Revenue
* Expenses
* Budget Balance

---

### DCA

Annual accounting statements.

Examples

* Assets
* Liabilities
* Equity

---

### MSC

Accounting balances.

Examples

* Budget Accounts
* Accounting Accounts
* Control Accounts

---

# Integration Strategy

The platform treats both sources as complementary.

Municipal Transparency Portal

↓

Operational Data

↓

Canonical Model

↓

Analytical Data Warehouse

↑

Official Fiscal Reports

↓

SICONFI

The goal is not to determine legal irregularities.

Instead, the platform identifies differences, inconsistencies, and data quality issues between official public datasets.

---

# Future Sources

Future versions of the platform may include:

* IBGE
* PNCP
* Receita Federal
* State Transparency Portals
* Open Government Data Portals
