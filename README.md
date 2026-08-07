# 🛒 RetailPro

> Sistema profesional de gestión de ventas e inventario desarrollado en Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Version](https://img.shields.io/badge/Version-v0.01.2-blue)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Descripción

RetailPro es un sistema profesional de gestión de ventas e inventario diseñado para administrar productos, proveedores, clientes, usuarios, compras y ventas desde una arquitectura moderna, modular y escalable.

El proyecto está desarrollado aplicando buenas prácticas de ingeniería de software, principios de **Clean Code**, arquitectura por capas y separación de responsabilidades.

Actualmente, la versión **v0.01.2** representa el cierre de la primera etapa del **backend funcional**.

---

## ✨ Funcionalidades implementadas — v0.01.2

### 📦 Inventario

- Gestión de productos.
- Gestión de categorías.
- Gestión de proveedores.
- Control de stock.
- Control de stock mínimo.
- Consulta de productos con stock bajo.
- Incremento de stock.
- Decremento de stock.
- Ajuste manual de stock.
- Verificación de disponibilidad.
- Actualización automática del stock.
- Registro de movimientos de inventario.
- Registro de stock anterior y stock nuevo.
- Trazabilidad mediante usuario y referencia.

### 💰 Ventas

- Registro de ventas.
- Registro de detalle de ventas.
- Soporte para ventas minoristas.
- Soporte para ventas mayoristas.
- Selección automática del precio según cantidad.
- Validación de stock disponible.
- Descuentos.
- Selección del método de pago.
- Cálculo automático del subtotal.
- Cálculo automático del total.
- Descuento automático del stock.
- Registro automático del movimiento de inventario.
- Rollback de transacciones ante errores.

### 🛒 Compras

- Registro de compras.
- Registro de detalle de compras.
- Asociación con proveedores.
- Registro del usuario responsable.
- Cálculo automático del subtotal.
- Cálculo de impuestos.
- Cálculo automático del total.
- Incremento automático del stock.
- Registro automático del movimiento de inventario.
- Rollback de transacciones ante errores.

### 👥 Clientes

- CRUD completo de clientes.
- Búsqueda de clientes.
- Consulta de clientes activos.
- Activación y desactivación.
- Validaciones de datos.

### 🏢 Proveedores

- CRUD completo de proveedores.
- Información fiscal.
- Información de contacto.
- Estado activo/inactivo.
- Validaciones.
- Asociación con productos y compras.

### 👤 Usuarios

- CRUD completo de usuarios.
- Registro de nombre.
- DNI.
- Email.
- Password protegida mediante hash.
- Roles de usuario.
- Activación y desactivación.
- Restauración de usuarios.
- Búsqueda de usuarios.
- Filtrado por rol.
- Validación de email.
- Validación de DNI.

### 🔐 Autenticación

- Sistema de login.
- Validación de credenciales.
- Hash de contraseñas mediante `bcrypt`.
- Verificación segura de contraseñas.
- Validación de usuarios activos.
- Validación de roles.
- Manejo de credenciales inválidas.
- `AuthService` independiente de la interfaz.

### 🗄️ Base de datos

- SQLite.
- SQLAlchemy ORM 2.x.
- Modelos tipados mediante `Mapped` y `mapped_column`.
- Relaciones entre entidades.
- Foreign Keys.
- Integridad referencial.
- `SessionLocal`.
- Configuración mediante variables de entorno.
- Arquitectura preparada para PostgreSQL.
- Inicialización automática de la base de datos.
- Seed de datos de prueba.

### 🏗️ Arquitectura

- Models.
- Repositories.
- Services.
- Authentication.
- Database Layer.
- Separación de responsabilidades.
- Repository Pattern.
- Service Layer.
- Manejo de transacciones.
- Rollback ante errores.
- Clean Code.

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python | Lenguaje principal |
| SQLAlchemy | ORM |
| SQLite | Base de datos de desarrollo |
| PostgreSQL | Compatible para producción |
| python-dotenv | Variables de entorno |
| bcrypt | Hash y verificación de contraseñas |
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
│   ├── auth/
│   ├── database/
│   ├── views/
│   ├── utils/
│   └── config/
│
├── docs/
├── tests/
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

---

## 🌎 Convención de idioma

Aunque la documentación y la futura interfaz del sistema están en español, **todo el código fuente está escrito completamente en inglés**.

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
- Métodos
- Relaciones
- Nombres de módulos

Esta decisión sigue estándares internacionales de desarrollo y facilita la colaboración con desarrolladores de cualquier parte del mundo.

El objetivo es mantener una base de código consistente, profesional y alineada con principios de **Clean Code**.

---

## 🎯 Objetivos

Este proyecto busca demostrar conocimientos en:

- Arquitectura de Software
- Programación Orientada a Objetos
- Python
- SQL
- Bases de Datos
- SQLAlchemy
- Repository Pattern
- Service Layer
- Gestión de Inventario
- Gestión de Ventas
- Gestión de Compras
- Backend Development
- Autenticación
- Gestión de usuarios
- Clean Code
- Manejo de transacciones
- PostgreSQL
- Docker
- Automatización
- Diseño escalable
- Desarrollo de aplicaciones empresariales

---

# 🚀 Próxima etapa — v0.02.0

La próxima versión estará enfocada en comenzar el desarrollo de la **interfaz gráfica de RetailPro**.

### 🖥️ Interfaz gráfica

- Interfaz desarrollada con Flet.
- Pantalla de Login.
- Dashboard principal.
- Navegación lateral.
- Gestión visual de productos.
- Gestión visual de categorías.
- Gestión visual de clientes.
- Gestión visual de proveedores.
- Gestión visual de usuarios.
- Gestión visual del inventario.
- Gestión visual de ventas.
- Gestión visual de compras.
- Dashboard con estadísticas.
- Dark Mode.
- Light Mode.

La prioridad será conectar la interfaz con el backend existente, manteniendo la separación entre la presentación, la lógica de negocio y el acceso a datos.

---

# 🔮 Futuras actualizaciones

Después de completar la interfaz gráfica, el proyecto continuará evolucionando hacia una solución empresarial más completa.

### 🔌 Backend y API

- API REST.
- Autenticación mediante JWT.
- Sistema avanzado de permisos.
- Documentación de API.
- Integraciones externas.

### 🗄️ Infraestructura

- PostgreSQL.
- Docker.
- Docker Compose.
- Configuración para producción.
- Migraciones de base de datos.

### 🤖 Automatización e integraciones

- Integración con ARCA.
- Facturación electrónica.
- Integración bancaria.
- Detección de transferencias.
- Sistema de notificaciones.
- Automatización de procesos.

### 📊 Reportes

- Reportes de ventas.
- Reportes de compras.
- Reportes de inventario.
- Exportación a Excel.
- Exportación a PDF.
- Estadísticas y análisis de ventas.

### 🏢 Funcionalidades comerciales

- Multi sucursal.
- Código de barras.
- Gestión avanzada de precios.
- Descuentos por cantidad.
- Alertas de stock.
- Historial de movimientos.
- Auditoría de operaciones.

---

## 📈 Estado del proyecto

**Versión actual:** `v0.01.2`

**Fecha de actualización:** `07 de agosto de 2026`

🟢 **Backend funcional completado.**

El backend de RetailPro cuenta actualmente con modelos, repositories, services, autenticación, gestión de inventario, compras, ventas, clientes, proveedores y usuarios.

La próxima etapa será el desarrollo de la **interfaz gráfica**, comenzando por el sistema de **Login** y el **Dashboard principal**.

---

## 📜 Historial de versiones

### v0.01.2 — 07/08/2026

**Backend funcional completado.**

- CRUD de productos.
- CRUD de categorías.
- CRUD de clientes.
- CRUD de proveedores.
- CRUD de usuarios.
- Gestión de inventario.
- Movimientos de stock.
- Compras.
- Ventas.
- Precios minoristas y mayoristas.
- Descuentos.
- Métodos de pago.
- Autenticación.
- Hash de contraseñas.
- Roles.
- Validaciones.
- Transacciones.
- Rollback.
- Seed de base de datos.
- Arquitectura por capas.

### v0.01.1 — 01/08/2026

**Backend inicial.**

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
- Repository Pattern
- Service Layer
- Clean Code
- Gestión de Inventario
- Autenticación
- Automatización
- Desarrollo de aplicaciones empresariales
````
