import pytest
from Barberia import BarberiaFilo

def test_calcular_total_solo_corte():
    # Solo corte ($180), cliente normal
    assert BarberiaFilo.calcular_total(True, False, 2) == 180.0

def test_calcular_total_solo_barba_frecuente():
    # Solo barba ($120), cliente frecuente (>=5 visitas), se restan $20 -> $100
    assert BarberiaFilo.calcular_total(False, True, 5) == 100.0

def test_calcular_total_corte_y_barba_con_descuento():
    # Corte + Barba = $300. Con 15% descuento = $255.
    assert BarberiaFilo.calcular_total(True, True, 3) == 255.0

def test_calcular_total_corte_barba_y_frecuente():
    # Corte + Barba = $300. Descuento 15% = $255. Menos $20 frecuente = $235.
    assert BarberiaFilo.calcular_total(True, True, 6) == 235.0

def test_cancelacion_anticipada():
    # 24 horas o más antes -> $0
    assert BarberiaFilo.calcular_cargo_cancelacion(200.0, 24.0) == 0.0
    assert BarberiaFilo.calcular_cargo_cancelacion(200.0, 48.0) == 0.0

def test_cancelacion_media():
    # Entre 2 y 24 horas antes -> 50%
    assert BarberiaFilo.calcular_cargo_cancelacion(200.0, 12.0) == 100.0

def test_cancelacion_tardia_o_no_show():
    # Menos de 2 horas o no se presenta -> 100%
    assert BarberiaFilo.calcular_cargo_cancelacion(200.0, 1.5) == 200.0
    assert BarberiaFilo.calcular_cargo_cancelacion(200.0, 0.0, se_presento=False) == 200.0