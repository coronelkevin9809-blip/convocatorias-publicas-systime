# Dashboard público de convocatorias

Versión pública e informativa de convocatorias abiertas. Solo incluye datos y enlaces de fuentes oficiales. No contiene el Data Room institucional, documentos internos, claves de API ni hojas privadas del reporte original.

## Ejecución local

```powershell
python -m pip install -r requirements.txt
python -m streamlit run dashboard_app.py
```

## Publicación

Despliega `dashboard_app.py` desde este repositorio en Streamlit Community Cloud. La aplicación muestra únicamente los campos seleccionados en `convocatorias_publicas.csv`.

## Actualización automática

El agente de búsqueda actualiza `convocatorias_publicas.csv` después de cada escaneo satisfactorio. Solo envía oportunidades con estado abierto explícito, fecha vigente y enlace directo de postulación accesible. El dashboard refresca sus datos periódicamente y avisa cuando el feed lleva más de 48 horas sin revisión.

La lista es informativa. Revisa las bases y la disponibilidad del portal oficial antes de postular; la presencia de una oportunidad no confirma la elegibilidad de SysTime. Este repositorio no debe contener credenciales, el Data Room institucional, borradores ni reportes completos.
