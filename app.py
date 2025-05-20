import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV (reemplaza 'TU_USUARIO' por tu usuario real de GitHub)
clientes_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/TU_USUARIO/DashboardChocolate-Export/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/TU_USUARIO/DashboardChocolate-Export/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/barreras.csv"

# Lectura de los archivos CSV
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)

# Título del Dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país
paises = exportaciones["País"].dropna().unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", sorted(paises))

# Mostrar datos de clientes
st.subheader("Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]

if not exportaciones_filtradas.empty:
    fig, ax = plt.subplots()
    ax.bar(exportaciones_filtradas["Producto"], exportaciones_filtradas["Exportaciones (USD millones)"], color='#2E86C1')
    ax.set_xlabel("Producto")
    ax.set_ylabel("Exportaciones (USD millones)")
    ax.set_title(f"Exportaciones de Chocolates en {pais_seleccionado}")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.write("No hay datos de exportación para este país.")

# Mostrar datos de mercados
st.subheader("Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
st.dataframe(mercados_filtrados)

# Mostrar barreras de entrada
st.subheader("Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
st.dataframe(barreras_filtradas)

# Análisis Comparativo
st.subheader("Análisis Comparativo del Tamaño de Mercado")
if not mercados.empty:
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.bar(mercados["País"], mercados["Tamaño del Mercado (USD millones)"], color='#F39C12')
    ax2.set_xlabel("País")
    ax2.set_ylabel("Tamaño del Mercado (USD millones)")
    ax2.set_title("Comparación de Tamaños de Mercado por País")
    plt.xticks(rotation=45)
    st.pyplot(fig2)
else:
    st.write(""No hay datos disponibles para comparación de mercados.")
