"""
Módulo: main.py
Descripción: Script principal que coordina la simulación y visualización de resultados.
"""
import pandas as pd
import numpy as np
import os
from src.scenarios import get_all_scenarios
from src.physics import pathloss_terrestrial, pathloss_satellite, calculate_sinr
from src.constants import P_TX_BS, P_TX_LEO, BW_BS, BW_LEO
from src.visualizer import plot_final_results
from src.visualizerv2 import plot_final_results_v2

def main():
    # Creación de directorios para resultados
    for folder in ['data', 'plots']:
        if not os.path.exists(folder): os.makedirs(folder)

    sc = get_all_scenarios()
    dist_km = np.linspace(0.1, 15, 200)
    elev_deg = np.linspace(5, 90, 180)

    # 1. Simulación Terrestre
    data_t = []
    for s in sc['terrestrial']:
        pl = pathloss_terrestrial(dist_km, s['phi'])
        sinr = [calculate_sinr(p, P_TX_BS, BW_BS) for p in pl]
        for d, p, snr in zip(dist_km, pl, sinr):
            data_t.append({'Distance_km': d, 'PathLoss_dB': p, 'SINR_dB': snr, 'Scenario': s['name']})
    df_t = pd.DataFrame(data_t)
    df_t.to_csv('data/terrestrial_analysis_sinr.csv', index=False)

    # 2. Simulación Satelital (Bandas)
    data_s = []
    for s in sc['satellite']:
        pl = [pathloss_satellite(s['f'], a, s['h']) for a in elev_deg]
        sinr = [calculate_sinr(p, P_TX_LEO, BW_LEO) for p in pl]
        for a, p, snr in zip(elev_deg, pl, sinr):
            data_s.append({'Elevation_deg': a, 'PathLoss_dB': p, 'SINR_dB': snr, 'Band': s['name']})
    df_s = pd.DataFrame(data_s)
    df_s.to_csv('data/satellite_bands_sinr.csv', index=False)

    # 3. Prueba de Estrés (Altitudes)
    data_stress = []
    for s in sc['stress']:
        pl = [pathloss_satellite(s['f'], a, s['h']) for a in elev_deg]
        sinr = [calculate_sinr(p, P_TX_LEO, BW_LEO) for p in pl]
        for a, p, snr in zip(elev_deg, pl, sinr):
            data_stress.append({'Elevation_deg': a, 'PathLoss_dB': p, 'SINR_dB': snr, 'Orbit': s['name']})
    df_stress = pd.DataFrame(data_stress)
    df_stress.to_csv('data/orbit_stress_test_sinr.csv', index=False)

    # Visualización Final
    
    # Con MatPlotLib 
    plot_final_results(df_t, df_s, df_stress)

    # Con Plotly
    plot_final_results_v2(df_t, df_s, df_stress, output_path='plots/')
    
    # Confirmación de Simulación
    print("""Simulación Completa. En /plot y /data se encuentran los resultados de la simulación. 
    Para las gráficas estáticas se utiliza la librería Matplotlib y para gráficas interactivas se utiliza la librería Plotly.""")

if __name__ == "__main__":
    main()