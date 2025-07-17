from system_component import SystemComponent

class Model(SystemComponent):
    def get_usage(self):
        try:
            with open('/proc/device-tree/model', 'r') as f:
                return f.read().strip()
        except Exception:
            return "Unknown Model"
    
    def get_formatted_usage(self):
        model = self.get_usage()
        return f"Device Model: {model}" if model else "Device Model: Unavailable"