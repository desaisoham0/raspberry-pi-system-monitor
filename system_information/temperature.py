from system_component import SystemComponent
from config import Config

class Temperature(SystemComponent):
    def get_usage(self):
        """
        Reads the CPU temperature from the system file and returns it in Celsius as a float.
        """
        try:
            temp_file = Config.get('TEMP_FILE_PATH', '/sys/class/thermal/thermal_zone0/temp')
            with open(temp_file, 'r') as f:
                temp_str = f.read().strip()
                temp_c = float(temp_str) / 1000.0
                return temp_c
        except FileNotFoundError:
            return None
        except ValueError:
            return None
        except Exception as e:
            print(f"Error reading temperature: {e}")
            return None

    def get_formatted_usage(self):
        """
        Returns the temperature as a formatted string, or an error message if unavailable.
        """
        temp = self.get_usage()
        if temp is not None:
            return f"CPU Temperature: {temp:.2f}°C"
        else:
            return "CPU Temperature: Unavailable"