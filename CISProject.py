class LengthConverter:
	def __init__(self):
		self.miles_to_kilometers = 1.60934
		self.inches_to_centimeters = 2.54
		self.meters_to_feet = 3.28084
		self.meters_to_yards = 1.09361
	
	def miles_to_km(self, miles):
		return miles * self.miles_to_kilometers
	
	def km_to_miles(self, kilometers):
		return kilometers / self.miles_to_kilometers
	
	def inches_to_cm(self, inches):
		return inches * self.inches_to_centimeters
	
	def cm_to_inches(self, centimeters):
		return centimeters / self.inches_to_centimeters
	
	def meters_to_feet(self, meters):
		return meters * self.meters_to_feet
	
	def feet_to_meters(self, feet):
		return feet / self.meters_to_feet
	
	def meters_to_yards(self, meters):
		return meters * self.meters_to_yards
	
	def yards_to_meters(self, yards):
		return yards / self.meters_to_yards
	
	def use_convert(self, original_metric, convert_to, length):
		
		original_metric = original_metric.lower()
		convert_to = convert_to.lower()
		
		if original_metric == "miles" and convert_to == "kilometers":
			print(f'{self.miles_to_km(length):.2f} km')
		
		elif original_metric == "kilometers" and convert_to == "miles":
			print(f'{self.km_to_miles(length):.2f} miles')
		
		elif original_metric == "inches" and convert_to == "centimeters":
			print(f'{self.inches_to_cm(length):.2f} cm')
			
		elif original_metric == "centimeters" and convert_to == "inches":
			print(f'{self.cm_to_inches(length):.2f} in')
			
		elif original_metric == "meters" and convert_to == "feet":
			print(f'{self.meters_to_feet(length):.2f} ft')
		
		elif original_metric == "feet" and convert_to == "meters":
			print(f'{self.feet_to_meters(length):.2f} m')
			
		elif original_metric == "meters" and convert_to == "yards":
			print(f'{self.meters_to_yards(length):.2f} yards')
		
		elif original_metric == "yards" and convert_to == "meters":
			print(f'{self.yards_to_meters(length):.2f} m')
		
		else:
			print(f'Converter not found.')
        
'''
converter = LengthConverter()

converter.use_convert("miles", "kilometers", 40)
'''
class TemperatureConverter:
	def __init__(self, temperature):
		self.temperature = temperature
	
	def celsius_to_fahrenheit(self):
		return (self.temperature * (9/5)) + 32
		
	def fahrenheit_to_celsius(self):
		return (self.temperature - 32) * (5/9)
		
'''
temp_celsius = int(input(""))

converter = TemperatureConverter(temp_celsius)

temp_fahrenheit = converter.celsius_to_fahrenheit()

print(f"{temp_celsius:.2f} Celsius is {temp_fahrenheit:.2f} Fahrenheit!")
'''
class VolumeConverter:

class AreaConverter:
