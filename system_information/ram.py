import psutil
from system_component import SystemComponent

class RAM(SystemComponent):
    def get_usage(self):
        try:
            memory = psutil.virtual_memory()
            return {
                'total': memory.total / 1024**3,
                'used': memory.used / 1024**3,
                'percent': memory.percent
            }
        except Exception:
            return "Error retrieving RAM usage"
    
    def get_formatted_usage(self):
        usage = self.get_usage()
        if isinstance(usage, dict):
            return {
                'total': f"{round(usage['total'], 2)} GB",
                'used': f"{round(usage['used'], 2)} GB",
                'percent': f"{usage['percent']}%"
            }
        else:
            return usage