# EPW reader

This is a small script that reads EPW files to extract information regarding
the location, etc. as well as the following time series:

- "date", # (Year, Month, Day, Hour, Minute)
- "time", # Time in hours, beginning with 0
- "temperature", # Ambient temperature in °C
- "relative humidity", # In %
- "pressure", # In Pa
- "beam", # Direct horizontal radiation in Wh/m2 (resp. W/m2)
- "diffuse", # Diffuse horizontal radiation in Wh/m2 (resp. W/m2)
- "wind direction", # In °
- "wind velocity", # In m/s
- "cloudiness"
