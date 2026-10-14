from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Convocatorias abiertas | SysTime",
    page_icon="📣",
    layout="wide",
)

DATA_PATH = Path(__file__).with_name("convocatorias_publicas.csv")


@st.cache_data(ttl=300)
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
df = cargar_convocatorias()
if df.empty:
    st.info("Aún no hay oportunidades cargadas en la versión pública.")
else:
    if "Última revisión" in df.columns:
        revisiones = pd.to_datetime(df["Última revisión"], errors="coerce")
        ultima_revision = revisiones.max()
        if pd.notna(ultima_revision):
            st.caption(f"Fuentes revisadas por última vez: {ultima_revision:%d/%m/%Y}.")
            hoy = datetime.now(ZoneInfo("America/Bogota")).date()
            if (hoy - ultima_revision.date()).days > 2:
                st.warning("La búsqueda automática no se ha actualizado en más de 48 horas. Confirma la vigencia en la fuente oficial antes de postular.")
                if "Estado" in df.columns:
                    df.loc[:, "Estado"] = "Pendiente de revalidar — última revisión antigua"
        else:
            st.warning("No se encontró la fecha de la última revisión. Confirma la vigencia en la fuente oficial.")
    st.caption("La vigencia y los requisitos pueden cambiar. Confirma siempre las bases oficiales antes de postular.")
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
