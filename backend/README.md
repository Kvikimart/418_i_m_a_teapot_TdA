# Python Flask Backend Šablona

Vítame ťa v šablóne pre Python Flask backend! Tento projekt je jednoduché API na správu produktov v školskom bufete, vytvorené pomocou Flask a Flask-SQLAlchemy. Je navrhnutý ako východiskový bod pre začínajúcich vývojárov. Definícia API sa nachádza v [`base_template.yml`](base_template.yml).

## Požiadavky

*   **Python 3.12 alebo novší:** [Stiahnuť Python](https://www.python.org/downloads/)
*   **Docker Desktop:** Projekt používa Docker na spustenie MySQL databázy. [Stiahnuť Docker](https://www.docker.com/products/docker-desktop/)

---

## Začíname

### 1. Vytvorenie virtuálneho prostredia

**Na Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Na macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Inštalácia závislostí
```bash
pip install -r requirements.txt
```

### 3. Spustenie databázy (MySQL)
```bash
./start-db.sh        # macOS/Linux
start-db.bat         # Windows
```
Alternatívne spúšťa celý stack aj súbor `docker/compose.yaml`.

---

## Spustenie projektu

*   **Na Windows:** `./start.bat`
*   **Na macOS/Linux:** `./start.sh`

Server beží na adrese `http://127.0.0.1:8080`. API odpovedá na koncových bodoch `/api/product`. Tabuľky sa v databáze vytvoria automaticky pri štarte aplikácie.

---

## API Endpointy

| Metóda | Endpoint | Popis |
| :--- | :--- | :--- |
| `GET` | `/api/product` | Zoznam všetkých produktov |
| `POST` | `/api/product` | Vytvoriť nový produkt |
| `PUT` | `/api/product/<id>` | Aktualizovať existujúci produkt |
| `DELETE` | `/api/product/<id>` | Zmazať produkt |

### Príklad tela produktu (JSON):
```json
{
    "name": "Ukážkový produkt",
    "cost": 100
}
```

---

## Použitie Dockeru

```bash
docker compose -f docker/compose.yaml up -d --build
```
API bude k dispozícii na `http://127.0.0.1:8080`.

---

## Štruktúra projektu

*   `app/` — hlavná aplikácia (továreň aplikácie, konfigurácia, model, routy)
*   `run.py` — vstupný bod aplikácie
*   `requirements.txt` — zoznam Python závislostí
*   `docker/` — Docker konfigurácia (Dockerfile, init.sql, compose.yaml)
*   `base_template.yml` — OpenAPI špecifikácia, ktorú API implementuje

Šťastné kódovanie! 🚀

---

# Python Flask Backend Template

Welcome to the Python Flask Backend Template! This project is a simple API for managing products in a school buffet, built with Flask and Flask-SQLAlchemy. It is designed to be a starting point for beginner developers. The API definition lives in [`base_template.yml`](base_template.yml).

## Prerequisites

*   **Python 3.12 or higher:** [Download Python](https://www.python.org/downloads/)
*   **Docker Desktop:** This project uses Docker to run the MySQL database. [Download Docker](https://www.docker.com/products/docker-desktop/)

---

## Getting Started

### 1. Create a Virtual Environment

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Database (MySQL)
```bash
./start-db.sh        # macOS/Linux
start-db.bat         # Windows
```
Alternatively, `docker/compose.yaml` runs the whole stack.

---

## Running the Project

*   **On Windows:** `./start.bat`
*   **On macOS/Linux:** `./start.sh`

The server runs at `http://127.0.0.1:8080`. The API responds on `/api/product` endpoints. Tables are created automatically on application startup.

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/product` | List all products |
| `POST` | `/api/product` | Create a new product |
| `PUT` | `/api/product/<id>` | Update an existing product |
| `DELETE` | `/api/product/<id>` | Delete a product |

### Example Product Body (JSON):
```json
{
    "name": "Sample Product",
    "cost": 100
}
```

---

## Using Docker

```bash
docker compose -f docker/compose.yaml up -d --build
```
The API will be available at `http://127.0.0.1:8080`.

---

## Project Structure

*   `app/` — the main application (app factory, config, model, routes)
*   `run.py` — application entry point
*   `requirements.txt` — list of Python dependencies
*   `docker/` — Docker configuration (Dockerfile, init.sql, compose.yaml)
*   `base_template.yml` — the OpenAPI spec this API implements

Happy coding! 🚀
