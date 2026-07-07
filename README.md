# SIGIO

**Sistema de Gestión de Implementos Ortopédicos**

SIGIO es una aplicación web desarrollada para administrar el inventario y préstamo de implementos ortopédicos del Club de Leones San José de Mayo.

---

# Características

- Autenticación mediante JWT
- Gestión de usuarios y roles
- Gestión de implementos
- Gestión de beneficiarios
- Administración de préstamos
- Registro de mantenimientos
- Registro de adquisiciones
- Registro de bajas
- Dashboard con indicadores
- Reportes
- API REST documentada con Swagger

---

# Tecnologías

## Backend

- Python 3.14
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic v2

## Frontend

- React
- Vite
- TypeScript
- Material UI
- React Router
- Axios
- TanStack Query
- React Hook Form
- Zod
- Recharts

---

# Requisitos

- Python 3.14 o superior
- Node.js 24 o superior
- PostgreSQL 17 o superior
- Git

---

# Instalación

## Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd SIGIO
```

---

## Backend

```bash
cd backend

python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

---

## Variables de entorno

Crear el archivo:

```
backend/.env
```

utilizando como base:

```
backend/.env.example
```

---

## Migraciones

```bash
alembic upgrade head
```

---

## Ejecutar Backend

```bash
python -m uvicorn app.main:app --reload
```

La documentación estará disponible en:

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

La aplicación estará disponible en:

```
http://localhost:5173
```

(Vite utilizará otro puerto automáticamente si 5173 está ocupado.)

---

# Estructura del proyecto

```
SIGIO/

├── backend/
├── frontend/
├── database/
├── docs/
├── backups/
├── herramientas/
├── instalador/
├── reportes/
└── uploads/
```

---

# Estado del Proyecto

## Backend

- Finalizado
- Operativo
- Estable

## Frontend

En desarrollo.

---

# Licencia

Proyecto desarrollado para el Club de Leones San José de Mayo.

Todos los derechos reservados.