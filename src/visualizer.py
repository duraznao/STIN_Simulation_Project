"""
Generación de gráficos usando Matplotlib.
"""
import matplotlib.pyplot as plt
import os

def plot_final_results(df_t, df_s, df_stress, output_path='plots/'):
    if not os.path.exists(output_path): os.makedirs(output_path)
    plt.style.use('bmh')

    # FIGURA 1: Pathloss y SINR Terrestre
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    for sc in df_t['Scenario'].unique():
        data = df_t[df_t['Scenario'] == sc]
        ax1.plot(data['Distance_km'], data['PathLoss_dB'], label=sc, linewidth=2)
        ax2.plot(data['Distance_km'], data['SINR_dB'], label=sc, linewidth=2)
    ax1.set_title('Pathloss Terrestre', fontweight='bold')
    ax1.set_xlabel('Distancia (km)')
    ax1.set_ylabel('Pérdida (dB)')
    ax2.set_title('SINR Terrestre', fontweight='bold')
    ax2.set_xlabel('Distancia (km)')
    ax2.set_ylabel('SINR (dB)')
    ax2.axhline(0, color='black', linestyle='--', alpha=0.5) # Umbral demod
    ax1.legend(); ax2.legend()
    fig1.savefig(f"{output_path}fig1_terrestrial_analysis.png", dpi=300)

    # FIGURA 2: Comparativa de Bandas Satelitales (Pathloss y SINR)
    fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(15, 6))
    for sc in df_s['Band'].unique():
        data = df_s[df_s['Band'] == sc]
        ax3.plot(data['Elevation_deg'], data['PathLoss_dB'], label=sc, linewidth=2)
        ax4.plot(data['Elevation_deg'], data['SINR_dB'], label=sc, linewidth=2)
    ax3.set_title('Pathloss Satelital: S vs Ka', fontweight='bold')
    ax3.set_xlabel('Elevación (deg)')
    ax3.set_ylabel('Pérdida (dB)')
    ax4.set_title('SINR Satelital: S vs Ka', fontweight='bold')
    ax4.set_xlabel('Elevación (deg)')
    ax4.set_ylabel('SINR (dB)')
    ax3.legend(); ax4.legend()
    fig2.savefig(f"{output_path}fig2_satellite_bands.png", dpi=300)

    # FIGURA 3: Estrés Orbital (SINR)
    plt.figure(figsize=(10, 6))
    for orb in df_stress['Orbit'].unique():
        data = df_stress[df_stress['Orbit'] == orb]
        plt.plot(data['Elevation_deg'], data['SINR_dB'], label=orb, linewidth=2.5)
    plt.title('SINR Satelital: Sensibilidad a la Altitud de Órbita', fontweight='bold')
    plt.xlabel('Elevación (deg)')
    plt.ylabel('SINR (dB)')
    plt.legend()
    plt.savefig(f"{output_path}fig3_orbit_stress.png", dpi=300)