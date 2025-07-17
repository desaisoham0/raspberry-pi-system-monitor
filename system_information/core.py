import psutil
from system_component import SystemComponent

class Core(SystemComponent):
    def get_usage(self):
        try:
            # Get the number of physical CPU cores
            return psutil.cpu_count(logical=False)
        except Exception:
            return "Error retrieving CPU core count"
    
    def get_formatted_usage(self):
        usage = self.get_usage()
        if isinstance(usage, str):
            return [usage]
        return [f"{usage}"]