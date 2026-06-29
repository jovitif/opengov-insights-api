# Canonical Data Model

## Overview

Different public data sources describe similar business entities using different schemas, field names, and structures.

The purpose of the Canonical Data Model is to standardize those differences into a single internal representation.

All connectors must transform their source data into this canonical model before loading the analytical layers.

---

# Core Business Entities

## Municipality

Represents a Brazilian municipality.

Attributes

* municipality_id
* ibge_code
* municipality_name
* state

---

## Organization

Represents a municipal department or government organization.

Examples

* Health Department
* Education Department
* Finance Department

Attributes

* organization_id
* organization_name

---

## Supplier

Represents companies or individuals receiving government payments.

Attributes

* supplier_id
* supplier_name
* supplier_cnpj
* supplier_type

---

## Contract

Represents a government contract.

Attributes

* contract_number
* supplier_id
* organization_id
* contract_amount
* start_date
* end_date

---

## Procurement

Represents a procurement process.

Attributes

* procurement_number
* procurement_type
* organization_id
* publication_date

---

## Revenue

Represents municipal revenue.

Attributes

* revenue_id
* organization_id
* fiscal_year
* revenue_category
* amount

---

## Expense

Represents government expenditures.

Attributes

* expense_id
* organization_id
* supplier_id
* fiscal_year
* expense_category
* amount
* payment_date

---

## Fiscal Report

Represents information imported from SICONFI.

Attributes

* report_type
* fiscal_year
* organization_id
* reported_amount

---

# Canonical Mapping

Example

Municipal API

supplier

company

vendor

↓

Canonical Model

supplier_name

---

Municipal API

department

secretariat

organization

↓

Canonical Model

organization_name

---

Municipal API

contract_value

value

amount

↓

Canonical Model

amount

---

# Canonical Pipeline

```text
Municipal API
                 \
                  \
                   ---> Canonical Model ---> Silver Layer ---> Gold Layer
                  /
SICONFI API -----/
```

---

# Benefits

The Canonical Data Model provides:

* Standardized business entities
* Simplified transformations
* Easier integration of new data sources
* Consistent analytical models
* Reusable validation rules
* Improved data quality
