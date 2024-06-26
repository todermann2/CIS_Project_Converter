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
			print(f'{self.miles_to_km(length):.4f} km')
		
		elif original_metric == "kilometers" and convert_to == "miles":
			print(f'{self.km_to_miles(length):.4f} miles')
		
		elif original_metric == "inches" and convert_to == "centimeters":
			print(f'{self.inches_to_cm(length):.4f} cm')
			
		elif original_metric == "centimeters" and convert_to == "inches":
			print(f'{self.cm_to_inches(length):.4f} in')
			
		elif original_metric == "meters" and convert_to == "feet":
			print(f'{self.meters_to_feet(length):.4f} ft')
		
		elif original_metric == "feet" and convert_to == "meters":
			print(f'{self.feet_to_meters(length):.4f} m')
			
		elif original_metric == "meters" and convert_to == "yards":
			print(f'{self.meters_to_yards(length):.4f} yards')
		
		elif original_metric == "yards" and convert_to == "meters":
			print(f'{self.yards_to_meters(length):.4f} m')
		
		else:
			print(f'Conversion not supported.')

class TemperatureConverter:
	def __init__(self, temperature):
		self.temperature = temperature
	
	def celsius_to_fahrenheit(self):
		return (self.temperature * (9/5)) + 32
		
	def fahrenheit_to_celsius(self):
		return (self.temperature - 32) * (5/9)

class AreaConverter:
    def __init__(self):
        self.inches_to_feet_conversion = 1 / 144
        self.inches_to_yards_conversion = 1 / 1296
        
        self.feet_to_inches_conversion = 144
        self.feet_to_yards_conversion = 1 / 9
        
        self.yards_to_inches_conversion = 1296
        self.yards_to_feet_conversion = 9
        self.yards_to_acres_conversion = 1 / 4840
        
        self.acres_to_yards_conversion = 4840
        self.acres_to_miles_conversion = 1 / 640
        
        self.miles_to_acres_conversion = 640

    def inches_to_feet(self, square_inches):
        return square_inches * self.inches_to_feet_conversion

    def inches_to_yards(self, square_inches):
        return square_inches * self.inches_to_yards_conversion

    def feet_to_inches(self, square_feet):
        return square_feet * self.feet_to_inches_conversion

    def feet_to_yards(self, square_feet):
        return square_feet * self.feet_to_yards_conversion

    def yards_to_inches(self, square_yards):
        return square_yards * self.yards_to_inches_conversion

    def yards_to_feet(self, square_yards):
        return square_yards * self.yards_to_feet_conversion

    def yards_to_acres(self, square_yards):
        return square_yards * self.yards_to_acres_conversion

    def acres_to_yards(self, acres):
        return acres * self.acres_to_yards_conversion

    def acres_to_miles(self, acres):
        return acres * self.acres_to_miles_conversion

    def miles_to_acres(self, square_miles):
        return square_miles * self.miles_to_acres_conversion

    def use_convert(self, original_metric, convert_to, area):
        original_metric = original_metric.lower()
        convert_to = convert_to.lower()

        if original_metric == "square inches" and convert_to == "square feet":
            return self.inches_to_feet(area)

        elif original_metric == "square inches" and convert_to == "square yards":
            return self.inches_to_yards(area)

        elif original_metric == "square feet" and convert_to == "square inches":
            return self.feet_to_inches(area)

        elif original_metric == "square feet" and convert_to == "square yards":
            return self.feet_to_yards(area)

        elif original_metric == "square yards" and convert_to == "square inches":
            return self.yards_to_inches(area)

        elif original_metric == "square yards" and convert_to == "square feet":
            return self.yards_to_feet(area)

        elif original_metric == "square yards" and convert_to == "acres":
            return self.yards_to_acres(area)

        elif original_metric == "acres" and convert_to == "square yards":
            return self.acres_to_yards(area)

        elif original_metric == "acres" and convert_to == "square miles":
            return self.acres_to_miles(area)

        elif original_metric == "square miles" and convert_to == "acres":
            return self.miles_to_acres(area)

        else:
            print(f'Conversion not supported.')

class VolumeConverter:
    def __init__(self):
        self.quart_to_liters_conversion = 0.946353
        self.gallon_to_liters_conversion = 3.78541
        self.pint_to_liters_conversion = 0.473176
        self.fluid_ounce_to_ml_conversion = 29.5735
    
    def quart_to_liters(self, quart):
        return quart * self.quart_to_liters_conversion
    
    def liters_to_quart(self, liters):
        return liters / self.quart_to_liters_conversion
    
    def gallon_to_liters(self, gallon):
        return gallon * self.gallon_to_liters_conversion
    
    def liters_to_gallon(self, liters):
        return liters / self.gallon_to_liters_conversion
    
    def pint_to_liters(self, pint):
        return pint * self.pint_to_liters_conversion
    
    def liters_to_pint(self, liters):
        return liters / self.pint_to_liters_conversion
    
    def fluid_ounce_to_ml(self, fluid_ounce):
        return fluid_ounce * self.fluid_ounce_to_ml_conversion
    
    def ml_to_fluid_ounce(self, ml):
        return ml / self.fluid_ounce_to_ml_conversion
    
    def use_convert(self, original_metric, convert_to, volume):
        original_metric = original_metric.lower()
        convert_to = convert_to.lower()
        
        if original_metric == "quarts" and convert_to == "liters":
            return self.quart_to_liters(volume)
        
        elif original_metric == "liters" and convert_to == "quarts":
            return self.liters_to_quart(volume)
        
        elif original_metric == "gallons" and convert_to == "liters":
            return self.gallon_to_liters(volume)
        
        elif original_metric == "liters" and convert_to == "gallons":
            return self.liters_to_gallon(volume)
        
        elif original_metric == "pints" and convert_to == "liters":
            return self.pint_to_liters(volume)
        
        elif original_metric == "liters" and convert_to == "pints":
            return self.liters_to_pint(volume)
        
        elif original_metric == "fluid ounces" and convert_to == "milliliters":
            return self.fluid_ounce_to_ml(volume)
        
        elif original_metric == "milliliters" and convert_to == "fluid ounces":
            return self.ml_to_fluid_ounce(volume)
        
        else:
            print(f'Conversion not supported.')
