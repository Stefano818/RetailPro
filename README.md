# 🛒 RetailPro

> Sistema profesional de gestión de ventas e inventario desarrollado en Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Version](https://img.shields.io/badge/Version-v0.1.0-blue)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Descripción

RetailPro es un sistema profesional de gestión de ventas e inventario diseñado para administrar productos, proveedores, clientes, compras y ventas desde una arquitectura moderna y escalable.

El objetivo del proyecto es aplicar buenas prácticas de desarrollo de software, principios de **Clean Code**, arquitectura por capas y una estructura preparada para evolucionar hacia un sistema empresarial completo.

---

## ✨ Funcionalidades implementadas (v0.01.1)

### 📦 Inventario

- Gestión de productos.
- Gestión de categorías.
- Gestión de proveedores.
- Control de stock.
- Actualización automática del stock.
- Registro de movimientos de inventario.

### 💰 Ventas

- Registro de ventas.
- Soporte para ventas minoristas.
- Soporte para ventas mayoristas.
- Selección automática del precio.
- Cálculo automático del total.

### 🛒 Compras

- Registro de compras.
- Incremento automático del stock.

### 🗄️ Base de datos

- SQLite.
- SQLAlchemy ORM.
- Relaciones entre entidades.
- Integridad referencial.
- Arquitectura preparada para PostgreSQL.

### 🏗️ Arquitectura

- Models.
- Repositories.
- Services.
- Separación de responsabilidades.
- Clean Code.

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python | Lenguaje principal |
| SQLAlchemy | ORM |
| SQLite | Base de datos de desarrollo |
| PostgreSQL | Compatible para producción |
| Flet | Aplicación de escritorio *(próximamente)* |
| Streamlit | Dashboard *(próximamente)* |
| Docker | Despliegue *(próximamente)* |

---

## 📂 Estructura del proyecto

```text
RetailPro/
│
├── app/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── views/
│   ├── database/
│   ├── utils/
│   └── config/
│
├── docs/
├── tests/
├── requirements.txt
├── README.md
└── main.py
```

---

## 🌎 Convención de idioma

Aunque la interfaz del sistema está en español, **todo el código fuente está escrito completamente en inglés**.

Esto incluye:

- Variables
- Funciones
- Clases
- Modelos
- Tablas
- Columnas
- Archivos
- Servicios
- Repositorios
- Rutas

Esta decisión sigue estándares internacionales de desarrollo y facilita la colaboración con desarrolladores de cualquier parte del mundo.

---

## 🎯 Objetivos

Este proyecto busca demostrar conocimientos en:

- Arquitectura de Software
- Programación Orientada a Objetos
- SQL y Bases de Datos
- SQLAlchemy
- Gestión de Inventario
- Backend Development
- Clean Code
- Docker
- PostgreSQL
- Automatización
- Diseño Escalable

---

# 🗺️ Roadmap

## ✅ v0.01.1 — 01/08/2026

- Arquitectura por capas.
- SQLAlchemy.
- SQLite.
- Gestión de productos.
- Gestión de categorías.
- Gestión de proveedores.
- Registro de compras.
- Registro de ventas.
- Actualización automática del stock.
- Movimientos de inventario.
- Soporte para ventas mayoristas y minoristas.

---

## 🚧 Próxima versión (v0.02.0)

- CRUD de clientes.
- Sistema de autenticación.
- Roles y permisos.
- Validaciones.
- Mejoras en seguridad.

---

## 🚧 Versiones futuras

- Interfaz de escritorio con Flet.
- Dashboard con Streamlit.
- Reportes.
- Exportación a Excel.
- Exportación a PDF.
- API REST.
- Docker.
- PostgreSQL.
- Integración con ARCA.
- Integración bancaria.
- Multi sucursal.
- Sistema de notificaciones.
- Código de barras.
- Pruebas automatizadas.

---

## ⚙️ Instalación

### Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/RetailPro.git
```

### Ingresar al proyecto

```bash
cd RetailPro
```

### Crear entorno virtual

```bash
python -m venv .venv
```

### Activarlo

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar la aplicación

```bash
python main.py
```

---

## 📈 Estado del proyecto

**Versión actual:** **v0.01.1**

**Fecha de actualización:** **01 de agosto de 2026**

🚧 El proyecto se encuentra en desarrollo activo. Actualmente se está construyendo una base sólida del backend antes de comenzar con la interfaz gráfica y las integraciones externas.

---

## 📜 Historial de versiones

### v0.01.1 — 01/08/2026

**Implementado**

- Arquitectura modular.
- SQLAlchemy.
- SQLite.
- Gestión de productos.
- Gestión de categorías.
- Gestión de proveedores.
- Compras.
- Ventas.
- Actualización automática de stock.
- Movimientos de inventario.
- Soporte para ventas mayoristas y minoristas.

---

## 👨‍💻 Autor

Desarrollado como proyecto de portfolio para demostrar habilidades en:

- Desarrollo de Software
- Python
- SQL
- SQLAlchemy
- Arquitectura de Software
- Backend Development
- Clean Code
- Automatización
- Desarrollo de aplicaciones empresariales

