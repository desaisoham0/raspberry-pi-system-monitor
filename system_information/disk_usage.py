from system_component import SystemComponent
import psutil

class DiskUsage(SystemComponent):
    def get_usage(self):
        try:
            disk = psutil.disk_usage('/')
            return {
                'total': disk.total / 1024**3,
                'used': disk.used / 1024**3,
                'percent': disk.percent
        }
        except Exception:
            return "Disk usage not available"

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