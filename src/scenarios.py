"""
Configuración de escenarios para simulación STIN.
"""

def get_all_scenarios():
    """
    Define los diccionarios de configuración para todas las pruebas.
    """
    return {
        # Casos Terrestres: Varían según el exponente de pérdida phi
        'terrestrial': [
            {'name': 'Rural (Baseline)', 'phi': 3.5, 'color': '#3498db'},
            {'name': 'Suburban', 'phi': 3.8, 'color': '#2ecc71'},
            {'name': 'Urban (Dense)', 'phi': 4.5, 'color': '#e74c3c'}
        ],
        # Casos Satelitales: Comparan bandas de frecuencia (S vs Ka)
        'satellite': [
            {'name': 'S-Band (2 GHz)', 'f': 2.0, 'h': 600},
            {'name': 'Ka-Band (28 GHz)', 'f': 28.0, 'h': 600}
        ],
        # Prueba de Estrés: Impacto de la altitud orbital
        'stress': [
            {'name': 'V-LEO (300 km)', 'f': 2.0, 'h': 300, 'color': '#1abc9c'},
            {'name': 'LEO (600 km)', 'f': 2.0, 'h': 600, 'color': '#f1c40f'},
            {'name': 'M-LEO (1200 km)', 'f': 2.0, 'h': 1200, 'color': '#34495e'}
        ]
    }