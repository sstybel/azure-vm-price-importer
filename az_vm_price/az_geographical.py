az_geographicalalal = {
    "united-states": {
        "country_name": "United States",
        "geographical": "north-america",
        "geographical_name": "North America"
    },
    "united-kingdom": {
        "country_name": "United Kingdom",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "united-arab-emirates": {
        "country_name": "United Arab Emirates",
        "geographical": "asia",
        "geographical_name": "Asia"
    },
    "switzerland": {
        "country_name": "Switzerland",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "sweden": {
        "country_name": "Sweden",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "spain": {
        "country_name": "Spain",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "qatar": {
        "country_name": "Qatar",
        "geographical": "asia",
        "geographical_name": "Asia"
    },
    "poland": {
        "country_name": "Poland",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "norway": {
        "country_name": "Norway",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "new-zealand": {
        "country_name": "New Zealand",
        "geographical": "oceania",
        "geographical_name": "Oceania"
    },
    "mexico": {
        "country_name": "Mexico",
        "geographical": "north-america",
        "geographical_name": "North America"
    },
    "malaysia": {
        "country_name": "Malaysia",
        "geographical": "oceania",
        "geographical_name": "Oceania"
    },
    "korea": {
        "country_name": "Korea",
        "geographical": "asia",
        "geographical_name": "Asia"
    },
    "japan": {
        "country_name": "Japan",
        "geographical": "asia",
        "geographical_name": "Asia"
    },
    "italy": {
        "country_name": "Italy",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "israel": {
        "country_name": "Israel",
        "geographical": "asia",
        "geographical_name": "Asia"
    },
    "indonesia": {
        "country_name": "Indonesia",
        "geographical": "asia",
        "geographical_name": "Asia"
    },
    "india": {
        "country_name": "India",
        "geographical": "asia",
        "geographical_name": "Asia"
    },
    "germany": {
        "country_name": "Germany",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "france": {
        "country_name": "France",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "europe": {
        "country_name": "Europe",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "chile": {
        "country_name": "Chile",
        "geographical": "south-america",
        "geographical_name": "South America"
    },
    "canada": {
        "country_name": "Canada",
        "geographical": "north-america",
        "geographical_name": "North America"
    },
    "brazil": {
        "country_name": "Brazil",
        "geographical": "south-america",
        "geographical_name": "South America"
    },
    "belgium": {
        "country_name": "Belgium",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "azure-government": {
        "country_name": "Azure Government",
        "geographical": "north-america",
        "geographical_name": "North America"
    },
    "austria": {
        "country_name": "Austria",
        "geographical": "europe",
        "geographical_name": "Europe"
    },
    "australia": {
        "country_name": "Australia",
        "geographical": "oceania",
        "geographical_name": "Oceania"
    },
    "asia-pacific": {
        "country_name": "Asia Pacific",
        "geographical": "asia",
        "geographical_name": "Asia"
    },
    "africa": {
        "country_name": "Africa",
        "geographical": "africa",
        "geographical_name": "Africa"
    }
}

def az_geographicalal_by_country(country_key):
    return az_geographicalalal[country_key]

def az_geographical_name_by_country(country_key):
    return az_geographicalalal[country_key]["geographical_name"]


def az_geographical_key_by_country(country_key):
    return az_geographicalalal[country_key]["geographical"]

def az_country_name_by_country(country_key):
    return az_geographicalalal[country_key]["country_name"]
