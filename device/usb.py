import subprocess
from system_component import SystemComponent

class USB(SystemComponent):
    def get_usage(self):
        try:
            output = subprocess.check_output(['lsusb']).decode('utf-8')
            devices = [line.strip() for line in output.split('\n') if line]
            return devices
        except Exception as e:
            return [f"Error listing USB devices: {e}"]
    
    def get_formatted_usage(self):
        devices = self.get_usage()
        if devices:
            return "\n".join(devices)
        else:
            return "No USB devices found or error occurred."