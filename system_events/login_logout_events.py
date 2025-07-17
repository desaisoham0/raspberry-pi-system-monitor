import subprocess
from system_component import SystemComponent

class Events(SystemComponent):
    def get_usage(self):
        try:
            output = subprocess.check_output(['last', '-F', '-n', '10']).decode('utf-8')
            return output
        except Exception as e:
            return f"Error: {e}"
    
    def get_formatted_usage(self):
        events = self.get_usage()
        if events:
            return events.strip()
        else:
            return "No login/logout events found or error occurred."