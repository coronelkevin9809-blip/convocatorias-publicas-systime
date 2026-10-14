# Dashboard público de convocatorias

Versión pública e informativa de convocatorias abiertas. Solo incluye datos y enlaces de fuentes oficiales. No contiene el Data Room institucional, documentos internos, claves de API ni hojas privadas del reporte original.

## Ejecución local

```powershell
python -m pip install -r requirements.txt
python -m streamlit run dashboard_app.py
```

## Publicación

Despliega `dashboard_app.py` desde este repositorio en Streamlit Community Cloud. La aplicación muestra únicamente los campos seleccionados en `convocatorias_publicas.csv`.

## Actualización

El listado tiene un corte informativo indicado dentro de la aplicación. Revisa fechas, bases y disponibilidad del portal en las fuentes oficiales antes de postular. La convocatoria incluida puede requerir aliados y cumplir requisitos territoriales; su presencia no confirma la elegibilidad de SysTime. No cargues credenciales, el Data Room institucional ni reportes completos en este repositorio.
