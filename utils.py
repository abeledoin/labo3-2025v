import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Función para graficar evolución de toneladas por variable categórica
def plot_tn_by_category(df, category_col):
    grouped = df.groupby(['periodo', category_col])['tn'].sum().reset_index()
    #grouped['periodo'] = pd.to_datetime(grouped['periodo'].astype(str), format='%Y%m')

    # Calcular totales por categoría para ordenar las curvas
    total_by_cat = grouped.groupby(category_col)['tn'].sum().sort_values(ascending=False)
    ordered_categories = total_by_cat.index.tolist()

    pivot = grouped.pivot(index='periodo', columns=category_col, values='tn')
    pivot = pivot[ordered_categories]  # reordenar columnas por volumen total

    plt.figure(figsize=(14, 7))
    for column in pivot.columns:
        plt.plot(pivot.index, pivot[column], label=str(column))

    plt.title(f'Toneladas vendidas por mes - {category_col}')
    plt.xlabel('Periodo')
    plt.ylabel('Toneladas (tn)')
    plt.xticks(rotation=45)
    plt.legend(title=category_col, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid(True)
    plt.show()