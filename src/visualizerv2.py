"""
Generación de gráficos interactivos con Plotly.
"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def plot_final_results_v2(df_t, df_s, df_stress, output_path='plots/'):
    if not os.path.exists(output_path): os.makedirs(output_path)
    
    # FIGURA 1: Pathloss y SINR Terrestre
    fig1 = make_subplots(rows=1, cols=2, subplot_titles=("Pathloss Terrestre", "SINR Terrestre"))
    
    for sc in df_t['Scenario'].unique():
        data = df_t[df_t['Scenario'] == sc]
        # Pathloss
        fig1.add_trace(
            go.Scatter(x=data['Distance_km'], y=data['PathLoss_dB'], mode='lines', name=sc, legendgroup=sc),
            row=1, col=1
        )
        # SINR
        fig1.add_trace(
            go.Scatter(x=data['Distance_km'], y=data['SINR_dB'], mode='lines', name=sc, legendgroup=sc, showlegend=False),
            row=1, col=2
        )

    # Umbral demod (SINR)
    fig1.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5, row=1, col=2, annotation_text="Umbral")

    fig1.update_xaxes(title_text="Distancia (km)", row=1, col=1)
    fig1.update_yaxes(title_text="Pérdida (dB)", row=1, col=1)
    fig1.update_xaxes(title_text="Distancia (km)", row=1, col=2)
    fig1.update_yaxes(title_text="SINR (dB)", row=1, col=2)
    
    fig1.update_layout(height=600, width=1200, title_text="Análisis Terrestre")
    fig1.write_html(f"{output_path}fig1_terrestrial_analysis.html")

    # FIGURA 2: Comparativa de Bandas Satelitales (Pathloss y SINR)
    fig2 = make_subplots(rows=1, cols=2, subplot_titles=("Pathloss Satelital: S vs Ka", "SINR Satelital: S vs Ka"))

    for sc in df_s['Band'].unique():
        data = df_s[df_s['Band'] == sc]
        # Pathloss
        fig2.add_trace(
            go.Scatter(x=data['Elevation_deg'], y=data['PathLoss_dB'], mode='lines', name=sc, legendgroup=sc),
            row=1, col=1
        )
        # SINR
        fig2.add_trace(
            go.Scatter(x=data['Elevation_deg'], y=data['SINR_dB'], mode='lines', name=sc, legendgroup=sc, showlegend=False),
            row=1, col=2
        )

    fig2.update_xaxes(title_text="Elevación (deg)", row=1, col=1)
    fig2.update_yaxes(title_text="Pérdida (dB)", row=1, col=1)
    fig2.update_xaxes(title_text="Elevación (deg)", row=1, col=2)
    fig2.update_yaxes(title_text="SINR (dB)", row=1, col=2)

    fig2.update_layout(height=600, width=1200, title_text="Bandas Satelitales")
    fig2.write_html(f"{output_path}fig2_satellite_bands.html")

    # FIGURA 3: Estrés Orbital (SINR)
    fig3 = go.Figure()

    for orb in df_stress['Orbit'].unique():
        data = df_stress[df_stress['Orbit'] == orb]
        fig3.add_trace(
            go.Scatter(x=data['Elevation_deg'], y=data['SINR_dB'], mode='lines', name=orb)
        )

    fig3.update_layout(
        title="SINR Satelital: Sensibilidad a la Altitud de Órbita",
        xaxis_title="Elevación (deg)",
        yaxis_title="SINR (dB)",
        height=600,
        width=1000
    )
    fig3.write_html(f"{output_path}fig3_orbit_stress.html")
