# ShelfSense
ShelfSense is a household inventory tracking application designed to make it easier to know what items you already have at home, how many are left, and what needs to be restocked.

The core idea is simple: most household products already have barcodes, so instead of relying on memory or manually checking cabinets, a user can scan or enter a product barcode, create or find the item, and update inventory as products are added or used.

## Project Goal

The goal of ShelfSense is to build a practical inventory system for personal or family use that reduces waste, improves organization, and makes restocking easier.

This project is also intended as a portfolio-grade backend application that demonstrates:

- REST API design
- inventory and transaction data modeling
- Python backend development with FastAPI
- database-backed CRUD workflows
- containerization and deployment
- optional AI-assisted product normalization and categorization

## Problem Statement

In many households, people lose track of what they already own. This can lead to:

- buying duplicates unnecessarily
- running out of essentials without realizing it
- poor pantry and household organization
- friction when multiple people share responsibility for shopping or stocking

ShelfSense aims to solve this by keeping a simple, structured record of products and quantities.

## MVP Scope

The MVP focuses on the core inventory workflow.

### Included in MVP

- Create a product
- Find a product by barcode
- Add inventory quantity
- Remove inventory quantity
- View current inventory
- View low-stock items
- Track inventory transaction history
- Manual barcode entry
- Local development setup with Python virtual environment
- Dockerized backend
- Basic automated test coverage
- GitHub repository with CI pipeline for test runs

### Not Included in MVP

The following are intentionally out of scope for the first version:

- live camera barcode scanning
- multi-user household accounts
- authentication and authorization
- receipt OCR
- recipe generation
- shopping site integrations
- notifications
- mobile app development
- microservices architecture
- advanced frontend styling

## Core Workflow

1. A user enters or scans a product barcode.
2. The system checks whether that product already exists.
3. If the product exists, the user can add or remove quantity.
4. If the product does not exist, the user can create it.
5. Every quantity update is recorded in transaction history.
6. The system can show which products are low on stock.

## High-Level Features

- Product management
- Inventory quantity tracking
- Low-stock visibility
- Transaction/audit history
- Barcode-based lookup
- Future AI-assisted data cleanup and categorization

## Planned Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic

### Database
- SQLite for local development
- Postgres later for stronger deployment story

### Tooling
- Git + GitHub
- Python virtual environment (`.venv`)
- Docker
- GitHub Actions for CI

### Future Enhancements
- barcode scanning through device camera
- AI-based product name normalization
- AI-based category suggestions
- smart shopping list generation

## Initial Success Criteria

The MVP will be considered successful when:

- the backend runs locally without issues
- products can be created and retrieved
- inventory can be increased and decreased safely
- quantity cannot drop below zero
- low-stock items can be queried
- transaction history is recorded for every inventory change
- the project is tracked in Git and pushed to GitHub
- automated tests run successfully in CI
- the app can be run in Docker

## Why This Project

ShelfSense is meant to solve a real-life organization problem while also serving as a practical engineering project. It is intentionally scoped to be useful, buildable, and extendable without becoming bloated too early.