from CISProject import LengthConverter, TemperatureConverter, AreaConverter, VolumeConverter

def main():
	print("")
	print("")
	print("                 Measuerment                  ")
	print("                  Converter                   ")
	print("")
	print("")
	print("~~~~~~~POSSIBLE CONVERSIONS ARE AS FOLLOWS.~~~~~~~")
	print("")
	print("")
	print("1. Length Conversions:")
	print("")
	print("	Miles to Kilometers.")
	print("	Kilometers to Miles.") 
	print("	Inches to Centimeters.")
	print("	Centimeters to Inches.")
	print("	Meters to Feet.")
	print("	Feet to Meters.")
	print("	Meters to Yards.")
	print("	Yards to Meters.")
	print("")
	print("2. Temperature Conversions:")
	print("")
	print("	Celsius to Fahrenheit.") 
	print("	Fahrenheit to Celsius.")
	print("")
	print("3. Area Conversions:")
	print("")
	print("	Square Inches to Square Feet.")
	print("	Square Inches to Square Yards.")
	print("	Square Feet to Square Inches.")
	print("	Square Feet to Square Yards.")
	print("	Square Yards to Square Inches.")
	print("	Square Yards to Square Feet.")
	print("	Square Yards to Acres.")
	print("	Acres to Square Yards.")
	print("	Acres to Square Miles.")
	print("	Square Miles to Acres.")
	print("")
	print("4. Volume Conversions:")
	print("")
	print("	Quarts to Liters.") 
	print("	Liters to Quarts.")
	print("	Gallons to Liters.")
	print("	Liters to Gallons.")
	print("	Pints to Liters.")
	print("	Liters to Pints.")
	print("	Fluid Ounces to Milliliters.")
	print("	Milliliters to Fluid Ounces.")
	print("")
	print("")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("")
	print("")
	
	conversions = []  # List to store converted data

	class_selection = ""
	
	while class_selection != "exit":
		class_selection = input("What is being converted today? ~ Length ~ Temp ~ Area ~ Volume ~ (Type 'exit' to quit): ")
		class_selection = class_selection.lower()


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
			print(f"{converted_area:.2f} {convert}")
			conversions.append((metric, convert, area, converted_area))
		
		elif class_selection == "volume":
			converter = VolumeConverter()
			metric = input("Enter the original metric type for your volume: ")
			convert = input("Enter the metric to convert to: ")
			volume = float(input("Enter the volume: "))
			
			converted_volume = converter.use_convert(metric, convert, volume)
			print(f"{converted_volume:.2f} {convert}")
			conversions.append((metric, convert, volume, converted_volume))

		elif class_selection == "exit":
			break
		
		else:
			print("Invalid selection.")

			
	print("\nAll conversions:")
	for conversion in conversions:
		print(conversion)
		
	save_file = input("Would you like to save the conversions to a file? (yes or no): ").lower()
	
	
	if save_file == "yes":
		file_name = input("Enter your desired name of the file!(one word, no spaces): ")
		with open(file_name, "w") as conversion_file:
			for conversion in conversions:
				conversion_file.write(f"{conversion}\n")
			print(f"Conversions saved to {file_name}.txt")
	else:
		print("Conversions not saved.")
		
            
if __name__ == "__main__":
    main()
