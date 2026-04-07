from city_functions import get_city_information


def test_city_country():
    """Do countries information like 'Santiago, Chile' work?"""
    formatted_answer = get_city_information("santiago", "chile")
    assert formatted_answer == "Santiago, Chile"


def test_city_country_population():
    """Do countries information like 'Santiago, Chile and pop' work?"""
    formatted_answer = get_city_information("santiago", "chile", "500000")
    assert formatted_answer == "Santiago, Chile - population 500000"
