from CISProject import LengthConverter, TemperatureConverter, AreaConverter, VolumeConverter

def main():
    
    class_selection = input("What is being converted today ? \n(select from Temp, Volume, Area, Length): ")

    class_selection.lower()
    
    if class_selection == "length":
      converter = LengthConverter()
      metric = input("Enter the original metric type for your length: ")
      convert = input("Enter the metric to convert to: ")
      length = float(input("Enter the length: "))
      converter.use_convert(metric, convert, length)

    if class_selection == "temp":
        converter = TemperatureConverter
        metric = input("Enter the metric in use : ")
        temp = input("Enter the temperature : ")
    
    if class_selection == "volume":
        converter = AreaConverter()
        metric = input("Enter the original metric type for your volume: ")
        convert = input("Enter the metric to convert to: ")
        length = float(input("Enter the volume: "))
        converter.use_convert(metric, convert, length)

if __name__ == "__main__":
    main() 