from CISProject import LengthConverter, TemperatureConverter, AreaConverter, VolumeConverter

def main():
	print("-----POSSIBLE LENGTH CONVERSIONS ARE AS FOLLOWS.-----")
	print("-----------------------------------------------------")
	print("Miles to Kilometers.")
	print("Kilometers to Miles.") 
	print("Inches to Centimeters.")
	print("Centimeters to Inches.")
	print("Meters to Feet.")
	print("Feet to Meters.")
	print("Meters to Yards.")
	print("Yards to Meters.")
	print("------POSSIBLE TEMP CONVERSIONS ARE AS FOLLOWS-----")
	print("----------------------------------------------------")
	print("Celsius to Fahrenheit.") 
	print("Fahrenheit to Celsius.")
	print("-----POSSIBLE AREA CONVERSIONS ARE AS FOLLOWS.-----")
	print("---------------------------------------------------")
	print("Inches to Feet.")
	print("Inches to Yards.")
	print("Feet to Inches.")
	print("Feet to Yards.")
	print("Yards to Inches.")
	print("Yards to Feet.")
	print("Yards to Acres.")
	print("Acres to Yards.")
	print("Acres to Miles.")
	print("Miles to Acres.")
	print("-----POSSIBLE VOLUME CONVERSIONS ARE AS FOLLOWS.-----")
	print("-----------------------------------------------------")
	print("Quart to Liters.") 
	print("Liters to Quart.")
	print("Gallon to Liters.")
	print("Liters to Gallon.")
	print("Pint to Liters.")
	print("Liters to Pint.")
	print("Fluid Ounce to Milliliters.")
	print("Milliliters to Fluid Ounce.")
	
	conversions = []  # List to store converted data
	
	class_selection = input("What is being converted today? \n(Select from: Temp, Volume, Area, Length): ")
	
	class_selection = class_selection.lower()
	
	while class_selection != "exit":
		if class_selection == "length":
			converter = LengthConverter()
			metric = input("Enter the original metric type for your length: ")
			convert = input("Enter the metric to convert to: ")
			length = float(input("Enter the length: "))
			
			converted_length = converter.use_convert(metric, convert, length)
			conversions.append((metric, convert, length, converted_length))
			
		
		elif class_selection == "temp":
			metric = input("Enter the metric in use \n(Select from: C, F): ")
			metric = metric.lower()
			temp = float(input("Enter the temperature : "))
			converter = TemperatureConverter(temp)
			
			if metric == "c":
				celsius = converter.celsius_to_fahrenheit()
				print(f"{temp} Celsius is {celsius:.2f} Fahrenheit!")
				
				conversions.append(("Celsius", "Fahrenheit", temp, celsius))
			
			elif metric == 'f':
				fahrenheit = converter.fahrenheit_to_celsius()
				print(f"{temp} Fahrenheit is {fahrenheit:.2f} Celsius!")
				
				conversions.append(("Fahrenheit", "Celsius", temp, fahrenheit))
		
		elif class_selection == "area":
			converter = AreaConverter()
			metric = input("Enter the original metric type for your area: ")
			convert = input("Enter the metric to convert to: ")
			area = float(input("Enter the area: "))
			
			converted_area = converter.use_convert(metric, convert, area)
			conversions.append((metric, convert, area, converted_area))
		
		elif class_selection == "volume":
			converter = VolumeConverter()
			metric = input("Enter the original metric type for your volume: ")
			convert = input("Enter the metric to convert to: ")
			volume = float(input("Enter the volume: "))
			
			converted_volume = converter.use_convert(metric, convert, volume)
			conversions.append((metric, convert, volume, converted_volume))
		
		else:
			print("Invalid selection.")
			
			class_selection = input("What is being converted today? \n(Select from: Temp, Volume, Area, Length): ")
			class_selection = class_selection.lower()
			
	print("\nAll conversions:")
	for conversion in conversions:
		print(conversion)
		
	answers = input("Would you like to save the evidence of your conversions in a file?(yes or no): ")
	
	make_a_file = answers.lower()
	
	if make_a_file == "yes":
		file_name = input("Enter your desired name of the file!(one word, no spaces): ")
		with open(file_name, "w") as conversion_file:
			conversion_file.append(conversions)
		
            
if __name__ == "__main__":
    main()
