from Q11_1 import city_country

def test_city_country():
    name = city_country("Santiago", "Chile")
    assert name == "Santiago, Chile"