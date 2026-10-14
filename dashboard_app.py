from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Convocatorias abiertas | SysTime",
    page_icon="📣",
    layout="wide",
)

DATA_PATH = Path(__file__).with_name("convocatorias_publicas.csv")
CORTE_DATOS = "14 de octubre de 2026"


@st.cache_data
def cargar_convocatorias() -> pd.DataFrame:
    if not DATA_PATH.exists():
        return pd.DataFrame()
    return pd.read_csv(DATA_PATH, keep_default_na=False)


st.title("📣 Convocatorias públicas abiertas")
st.write(
    "Oportunidades encontradas en fuentes oficiales, con enlaces a la convocatoria "
    "y al sistema de postulación. La publicación es informativa y no constituye "
    "una evaluación de elegibilidad para una empresa específica."
)
st.warning(
    f"Fuentes oficiales revisadas el {CORTE_DATOS}. La vigencia y los requisitos "
    "pueden cambiar; confirma siempre en la convocatoria oficial antes de postular."
)

df = cargar_convocatorias()
if df.empty:
    st.info("Aún no hay oportunidades cargadas en la versión pública.")
else:
    busqueda = st.text_input("Buscar por convocatoria o entidad")
    vista = df.copy()
    if busqueda:
        mascara = vista.apply(
            lambda fila: busqueda.casefold() in " ".join(map(str, fila.values)).casefold(),
            axis=1,
        )
        vista = vista[mascara]

    st.metric("Oportunidades listadas", len(vista))
    st.dataframe(
        vista,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Iniciar postulación": st.column_config.LinkColumn(
                "Iniciar postulación", display_text="Abrir portal de postulación"
            ),
            "Convocatoria oficial": st.column_config.LinkColumn(
                "Convocatoria oficial", display_text="Ver fuente oficial"
            ),
        },
    )

st.caption(
    "La postulación se realiza en el portal oficial indicado. Esta página no "
    "envía formularios ni garantiza la elegibilidad de una empresa."
)
