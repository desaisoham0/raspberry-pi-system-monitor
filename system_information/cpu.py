import psutil
import platform
from system_component import SystemComponent

class CPU(SystemComponent):
    def get_usage(self):
        try:
            # Get the CPU usage percentage
            return psutil.cpu_percent(interval=1)
        except Exception:
            return "Error retrieving CPU usage"
    
    def get_formatted_usage(self):
        # Format the CPU usage as a percentage string
        if isinstance(self.get_usage(), str):
            return self.get_usage()
        else:
            # Return the CPU usage as a formatted string
            return f"CPU Usage: {self.get_usage()}%"
    
    def get_speed(self):
        try:
            freq = psutil.cpu_freq()
            if freq:
                return f"{freq.current:.2f} MHz"
            else:
                return "Unknown CPU Speed"
        except Exception:
            return "Unknown CPU Speed"