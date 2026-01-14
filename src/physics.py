
"""
Cada función implementa una ecuación del paper base.
"""

import numpy as np
from .constants import *

def get_slant_range(theta_deg, h):
    """
    Calcula la distancia real (Slant Range) entre el UE y el Satélite.
    Implementa la Ecuación (5) de Ahmed et al.
    
    Args:
        theta_deg (float): Ángulo de elevación en grados.
        h (float): Altitud de la órbita en km.
    Returns:
        float: Distancia d_LEO en km.
    """
    theta_rad = np.radians(theta_deg)
    # Geometría esférica considerando la curvatura terrestre
    term1 = (R_EARTH * np.sin(theta_rad))**2
    term2 = h**2 + 2 * R_EARTH * h
    d_leo = np.sqrt(term1 + term2) - R_EARTH * np.sin(theta_rad)
    return d_leo

def pathloss_terrestrial(d_km, phi):
    """
    Calcula la pérdida de trayectoria para el enlace terrestre (BS).
    Implementa la Ecuación (2): L = zeta + 10*phi*log10(d/d0)
    
    Args:
        d_km (float/array): Distancia entre UE y BS en km.
        phi (float): Exponente de pérdida (ej. 3.5 para Rural, 4.5 para Urbano).
    """
    # Evitamos log(0) asegurando una distancia mínima de 1 metro
    return ZETA + 10 * phi * np.log10(np.maximum(d_km, 0.001) / D0)

def pathloss_satellite(f_ghz, theta_deg, h):
    """
    Calcula la pérdida total para el enlace satelital LEO.
    Implementa la suma de L_a (Atmosfera) + L_fspl (Espacio Libre).
    
    Args:
        f_ghz (float): Frecuencia de portadora en GHz.
        theta_deg (float): Elevación.
        h (float): Altitud.
    """
    d_leo = get_slant_range(theta_deg, h)
    theta_rad = np.radians(theta_deg)
    
    # L_a: Atenuación atmosférica (Ecuación 3). Aumenta si la elevación es baja.
    L_a = L_ZENITH / np.sin(theta_rad)
    
    # L_fspl: Free Space Path Loss (Ecuación 4).
    # Se multiplica f_ghz * 1000 para usar la constante estándar 32.45 (f en MHz).
    L_fspl = 20 * np.log10(f_ghz * 1000) + 20 * np.log10(d_leo) + 32.45
    
    return L_a + L_fspl

def calculate_sinr(pl_db, p_tx, bw):
    """
    Calcula el SINR (Signal-to-Interference-plus-Noise Ratio).
    Implementa: SINR = Prx - (N + I)
    """
    # Potencia recibida
    p_rx = p_tx + G_UE - pl_db
    
    # Piso de Ruido Térmico: N = k*T*B*F
    noise_floor_watts = K_BOLTZMANN * T_ROOM * bw
    noise_floor_dbm = 10 * np.log10(noise_floor_watts) + 30 + NF
    
    # Suma lineal de Ruido + Interferencia
    total_noise_interf_w = 10**((noise_floor_dbm)/10) + 10**((INTERFERENCE_DBM)/10)
    total_noise_interf_dbm = 10 * np.log10(total_noise_interf_w)
    
    return p_rx - total_noise_interf_dbm