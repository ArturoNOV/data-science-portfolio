# Vehicle Sales Dashboard

## Project objective

This project is a web application developed with Streamlit to explore a dataset of used vehicle advertisements in the United States.

The main objective of the application is to provide a simple and interactive way to visualize information related to vehicle mileage and price using Plotly charts.

The project also includes a basic exploratory data analysis (EDA) performed in a Jupyter Notebook.

## Visualizations

The application includes the following interactive visualizations:

- **Mileage distribution histogram:** shows the distribution of vehicle mileage (`odometer`) in the dataset.
- **Price vs. mileage scatter plot:** shows the relationship between vehicle mileage (`odometer`) and vehicle price (`price`).

The user can also select an option to include the scatter plot together with the histogram before generating the visualizations.

## Technologies used

- Python
- pandas
- Plotly
- Streamlit
- Jupyter Notebook

## Web application

The application is deployed publicly on Render and can be accessed here:

[Open the Streamlit application](https://project-sprint7-js21.onrender.com)

## Project structure

The repository includes:

- `app.py` — Streamlit web application.
- `vehicles_us.csv` — dataset used by the application.
- `requirements.txt` — required Python libraries.
- `notebooks/EDA.ipynb` — exploratory data analysis and Plotly visualizations.
