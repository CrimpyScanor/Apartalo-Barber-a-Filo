class BarberiaFilo:
    COSTO_CORTE = 180.0
    COSTO_BARBA = 120.0

    @classmethod
    def calcular_total(cls, incluye_corte: bool, incluye_barba: bool, visitas_mes: int) -> float:
        """
        R1 — Total del servicio:
        - Corte: $180. Barba: $120.
        - 15% de descuento si reserva corte y barba juntos.
        - -$20 adicionales si es cliente frecuente (5 o más visitas en el mes) después del descuento.
        """
        subtotal = 0.0
        if incluye_corte:
            subtotal += cls.COSTO_CORTE
        if incluye_barba:
            subtotal += cls.COSTO_BARBA

        # Aplicar 15% de descuento si lleva ambos servicios
        if incluye_corte and incluye_barba:
            subtotal *= 0.85

        # Aplicar descuento de cliente frecuente (>= 5 visitas) después del descuento anterior
        if visitas_mes >= 5:
            subtotal -= 20.0

        return round(max(0.0, subtotal), 2)

    @staticmethod
    def calcular_cargo_cancelacion(total_servicio: float, horas_anticipacion: float, se_presento: bool = True) -> float:
        """
        R2 — Cancelación:
        - Con 24 horas o más de anticipación: gratis ($0).
        - Con 2 horas o más, pero menos de 24: se cobra el 50% del total.
        - Con menos de 2 horas, o si no se presenta (no-show): se cobra el 100%.
        """
        if not se_presento:
            return round(total_servicio, 1)
        
        if horas_anticipacion >= 24:
            return 0.0
        elif 2 <= horas_anticipacion < 24:
            return round(total_servicio * 0.5, 2)
        else:
            return round(total_servicio, 2)