import os
import psutil
import time
from datetime import datetime
import statistics

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return disk_info.percent

def get_energy_usage():
    try:
        battery = psutil.sensors_battery()
        if battery is None:
            return "Energy usage data not available"
        power_now = battery.power_plugged
        if power_now:
            return "Using AC power"
        else:
            return f"Battery percent: {battery.percent}%"
    except Exception as e:
        return f"Error getting energy usage: {str(e)}"

def get_interrupt_count():
    try:
        stats = psutil.cpu_stats()
        return stats.ctx_switches + stats.interrupts
    except Exception as e:
        return f"Error getting interrupt count: {str(e)}"

def get_network_usage():
    try:
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent + net_io.bytes_recv
    except Exception as e:
        return f"Error getting network usage: {str(e)}"

def get_swap_usage():
    try:
        swap = psutil.swap_memory()
        return swap.percent
    except Exception as e:
        return f"Error getting swap usage: {str(e)}"

def get_cpu_temperature():
    try:
        temps = psutil.sensors_temperatures()
        if not temps:
            return "No temperature sensors found"
        for name, entries in temps.items():
            for entry in entries:
                return entry.current
    except Exception as e:
        return f"Error getting CPU temperature: {str(e)}"

def get_process_count():
    try:
        return len(psutil.pids())
    except Exception as e:
        return f"Error getting process count: {str(e)}"

def calculate_statistics(data):
    return {
        'min': min(data),
        'max': max(data),
        'mean': statistics.mean(data),
        'stdev': statistics.stdev(data) if len(data) > 1 else 'N/A',
        'variance': statistics.variance(data) if len(data) > 1 else 'N/A',
        'mode': statistics.mode(data) if len(data) > 1 else 'N/A'
    }

def main():
    metrics = {
        'timestamps': [],
        'cpu': [],
        'memory': [],
        'disk': [],
        'interrupt': [],
        'network': [],
        'swap': [],
        'cpu_temp': [],
        'process_count': []
    }

    try:
        print("Monitoring started. Perform your tasks in Astah UML...")
        for _ in range(4):  # Coletar dados por 10 vezes com intervalo de 10 segundos
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            metrics['timestamps'].append(current_time)
            metrics['cpu'].append(get_cpu_usage())
            metrics['memory'].append(get_memory_usage())
            metrics['disk'].append(get_disk_usage())
            metrics['interrupt'].append(get_interrupt_count())
            metrics['network'].append(get_network_usage())
            metrics['swap'].append(get_swap_usage())
            cpu_temp = get_cpu_temperature()
            if isinstance(cpu_temp, (int, float)):  # Apenas números são considerados
                metrics['cpu_temp'].append(cpu_temp)
            metrics['process_count'].append(get_process_count())
            
            time.sleep(8)  # Intervalo de 10 segundos entre cada coleta de métricas
        
        # Calcular estatísticas
        with open("metricas.txt", "w") as f:
            for i in range(len(metrics['timestamps'])):
                f.write(f"Timestamp: {metrics['timestamps'][i]}\n")
                f.write(f"CPU usage: {metrics['cpu'][i]}%\n")
                f.write(f"Memory usage: {metrics['memory'][i]}%\n")
                f.write(f"Disk usage: {metrics['disk'][i]}%\n")
                f.write(f"Interrupt count: {metrics['interrupt'][i]}\n")
                f.write(f"Network usage: {metrics['network'][i]} bytes\n")
                f.write(f"Swap usage: {metrics['swap'][i]}%\n")
                f.write(f"CPU temperature: {metrics['cpu_temp'][i] if i < len(metrics['cpu_temp']) else 'N/A'}\n")
                f.write(f"Process count: {metrics['process_count'][i]}\n")
                f.write("\n")
            
            for metric, values in metrics.items():
                if metric != 'timestamps' and values:
                    stats = calculate_statistics(values)
                    f.write(f"{metric.capitalize()} statistics: {stats}\n")
                    print(f"{metric.capitalize()} statistics: {stats}")
        
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()