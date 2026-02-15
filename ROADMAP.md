# ROADMAP - Invertir Online To Google Spreadsheet

## v0.2.0 - Estabilización (Prioridad Alta)

### Tests
- [ ] Setup pytest con fixtures
- [ ] Tests unitarios para `InvertirOnlineAPI`:
  - [ ] Test de autenticación (mock requests)
  - [ ] Test de refresh token
  - [ ] Test de get_estado_cuenta
  - [ ] Test de get_valor_dolar_mep
- [ ] Tests de integración con mocks de Google Sheets

### Seguridad
- [ ] Migrar de config.py a variables de entorno (.env)
- [ ] Agregar python-dotenv a requirements
- [ ] Documentar variables de entorno requeridas

### CI/CD
- [ ] Actualizar workflow para ejecutar tests
- [ ] Agregar badge de coverage al README

---

## v0.3.0 - Mejoras de Código (Prioridad Media)

### Type Hints
- [ ] Agregar anotaciones de tipos a `InvertirOnlineAPI`
- [ ] Agregar anotaciones de tipos a `main.py`
- [ ] Configurar mypy en CI

### Manejo de Errores
- [ ] Crear excepciones personalizadas (AuthError, APIError)
- [ ] Manejo específico de errores HTTP (401, 403, 500)
- [ ] Retry con backoff exponencial para errores transitorios

### Logging
- [ ] Configurar logging estructurado
- [ ] Logs con niveles apropiados (DEBUG, INFO, ERROR)
- [ ] Rotación de logs para ejecución prolongada

---

## v0.4.0 - Nuevas Funcionalidades (Prioridad Baja)

### Más Endpoints de IOL
- [ ] get_portfolio() - Ya existe, integrar en main
- [ ] get_cotizaciones_históricas()
- [ ] get_ordenes_activas()
- [ ] post_nueva_orden() (con confirmación)

### Análisis de Cartera
- [ ] Cálculo de rendimiento por período
- [ ] Comparación con benchmarks (S&P500, Merval)
- [ ] Gráficos de evolución (matplotlib/plotly)

### Multi-hoja
- [ ] Hoja separada para operaciones
- [ ] Hoja de rendimiento mensual
- [ ] Dashboard consolidado

---

## v1.0.0 - Release Público

### Publicación
- [ ] Publicar en PyPI como `iol-sheets` o similar
- [ ] Documentación completa con ejemplos
- [ ] Artículo en Medium sobre el proyecto

### Integración Continua
- [ ] Tests en múltiples versiones de Python (3.9, 3.10, 3.11)
- [ ] Deploy automático a PyPI en tags
- [ ] Semantic versioning automático

---

## Backlog (Sin Priorizar)

- [ ] Soporte para múltiples cuentas IOL
- [ ] Notificaciones (email/Telegram) ante cambios significativos
- [ ] Interfaz CLI con argparse/click
- [ ] Docker container para ejecución aislada
- [ ] Integración con Home Assistant para dashboard domótico
