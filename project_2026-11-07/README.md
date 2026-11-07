# Daily Project - 2026-11-07

## Overview

Today's project is a utility to calculate the great-circle distance between two points on a sphere given their longitudes and latitudes. This is known as the Haversine formula.

### Features
* Calculates distance in kilometers between two GPS coordinates (latitude, longitude in decimal degrees).
* Includes unit tests verifying accuracy against known distances, identical points, and coordinates in different hemispheres.

### How to use

```python
from haversine import calculate_haversine_distance

# New York to London
distance = calculate_haversine_distance(40.7128, -74.0060, 51.5074, -0.1278)
print(f"Distance: {distance} km")
```

### Running Tests

To run the tests for this project, run the following command from the root of the repository:

```bash
PYTHONPATH=project_2026-11-07 python3 -m unittest project_2026-11-07/test_haversine.py
```
