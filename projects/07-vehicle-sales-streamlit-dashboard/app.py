import pandas as pd
import plotly.graph_objects as go
import streamlit as st


# Función para acceder a los datasets.
def read_file(file, **kwargs):
    from pathlib import Path

    folder = Path(__file__).resolve().parent / 'datasets'
    path = folder / file

    extension = path.suffix.lower()

    if extension == '.csv':
        kwargs.setdefault('encoding', 'latin1')
        return pd.read_csv(path, **kwargs)

    elif extension in ['.xlsx', '.xls']:
        return pd.read_excel(path, **kwargs)

    else:
        raise ValueError(f'Formato no soportado: {extension}')


# Leer los datos del archivo CSV
car_data = read_file('vehicles_us.csv')

# Mostrar un encabezado para la aplicación
st.header('Análisis exploratorio de datos')

# Crear una casilla de verificación
build_od_dispersion = st.checkbox(
    'Incluir un gráfico de la relación precio y kilometraje'
)

if build_od_dispersion:
    # Mostrar un mensaje si la casilla está seleccionada
    st.write('Se incluirá además la relación entre Odómetro y Precio')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir')

# Ejecutar la lógica cuando se hace clic en el botón
if hist_button:
    st.write('Histograma distribución del odómetro')

    # Crear un histograma de la distribución del odómetro
    fig = go.Figure(
        data=[
            go.Histogram(x=car_data['odometer'])
        ]
    )
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, width='stretch')

    if build_od_dispersion:
        # Crear un gráfico de dispersión de kilometraje y precio
        fig = go.Figure(
            data=[
                go.Scatter(
                    x=car_data['odometer'],
                    y=car_data['price'],
                    mode='markers',
                )
            ]
        )
        fig.update_layout(title_text='Relación entre Odómetro y Precio')

        # Mostrar el gráfico Plotly interactivo
        st.plotly_chart(fig, width='stretch')