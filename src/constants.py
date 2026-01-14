"""
CONSTANTES
Referencia: 3GPP TR 38.811 y Ahmed et al. (2025)
"""
# Geometría Terrestre y Orbital
R_EARTH = 6371.0       # Radio de la Tierra en km
H_LEO = 600.0          # Altitud orbital estándar LEO en km
D0 = 0.1               # Distancia de referencia terrestre (100m)
ZETA = 90.0            # Pathloss de referencia en dB a la distancia D0

# Parámetros de Propagación
L_ZENITH = 0.05        # Atenuación atmosférica en el cenit (dB)

# --- PARÁMETROS PARA ANÁLISIS SINR ---
P_TX_BS = 46.0         # Potencia de transmisión BS (dBm)
P_TX_LEO = 43.0        # Potencia de transmisión Satélite (dBm)
G_UE = 5.0             # Ganancia de antena del usuario (dBi)
BW_BS = 10e6           # Ancho de banda Terrestre (10 MHz)
BW_LEO = 20e6          # Ancho de banda Satelital (20 MHz)
NF = 7.0               # Figura de ruido del receptor (dB)
K_BOLTZMANN = 1.38e-23 # Constante de Boltzmann
T_ROOM = 290           # Temperatura de ruido (Kelvin)
INTERFERENCE_DBM = -110.0 # Nivel de interferencia asumido (dBm)