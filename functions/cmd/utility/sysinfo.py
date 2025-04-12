from functions.base.utils import slow_type, log
import platform

def sysinfo():
        sys_info = (
            f"System: {platform.system()}\n"
            f"Node Name: {platform.node()}\n"
            f"Release: {platform.release()}\n"
            f"Version: {platform.version()}\n"
            f"Machine: {platform.machine()}\n"
            f"Processor: {platform.processor()}"
        )
        slow_type(sys_info)
        log("System info displayed")