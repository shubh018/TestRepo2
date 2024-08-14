from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Initialize the geolocator
geolocator = Nominatim(user_agent="zip_code_locator")

# Function to get latitude and longitude from a zip code
def get_coordinates(zip_code):
    location = geolocator.geocode(zip_code)
    if location:
        return (location.latitude, location.longitude)
    return None

# Function to find nearby zip codes (mock example)
def find_nearby_zipcodes(zip_code, radius=10, max_results=5):
    # Get coordinates of the zip code
    coords = get_coordinates(zip_code)
    if not coords:
        print(f"Could not find coordinates for zip code: {zip_code}")
        return []

    # Placeholder for zip code database (replace with actual database or API)
    zip_code_database = [
        {"zip": "10001", "lat": 40.7128, "lon": -74.0060},
        {"zip": "10002", "lat": 40.7158, "lon": -73.9985},
        {"zip": "10003", "lat": 40.7308, "lon": -73.9973},
        {"zip": "10004", "lat": 40.7074, "lon": -74.0113},
        # Add more zip codes here
    ]

    nearby_zipcodes = []
    for entry in zip_code_database:
        distance = geodesic(coords, (entry["lat"], entry["lon"])).miles
        if distance <= radius:
            nearby_zipcodes.append(entry["zip"])
        if len(nearby_zipcodes) >= max_results:
            break

    return nearby_zipcodes

# Example usage
zip_code = "75040"
nearby_zipcodes = find_nearby_zipcodes(zip_code, radius=5)
print("Nearby zip codes:", nearby_zipcodes)
