import pytest
from app.inventario import Inventario

def test_agregar_producto_exitoso():
    """Caso Exitoso: Agregar un producto nuevo"""
    inv = Inventario()
    resultado = inv.agregar_producto("Manzanas", 10)
    assert resultado == 10
    assert inv.obtener_stock("Manzanas") == 10

def test_agregar_cantidad_negativa():
    """Caso de Error: Intentar agregar stock negativo"""
    inv = Inventario()
    with pytest.raises(ValueError, match="La cantidad no puede ser negativa"):
        inv.agregar_producto("Peras", -5)

def test_stock_producto_inexistente():
    """Caso Borde: Consultar stock de un producto que no existe"""
    inv = Inventario()
    # Debe devolver 0 en lugar de fallar
    assert inv.obtener_stock("Bananas") == 0