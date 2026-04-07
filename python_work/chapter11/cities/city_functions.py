def get_city_information(city_name, country_name, population=""):

    if population:
        return f"{city_name.title()}, {country_name.title()} - population {population}"

    return f"{city_name}, {country_name}".title()


print(get_city_information("moscow", "russia"))
