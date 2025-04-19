import tkinter as tk
from tkinter import messagebox
import requests

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        if data['status'] == 'success':
            return (
                f"IP: {data['query']}\n"
                f"ISP: {data['isp']}\n"
                f"Org: {data['org']}\n"
                f"Country: {data['country']} ({data['countryCode']})\n"
                f"Region: {data['regionName']}\n"
                f"City: {data['city']}\n"
                f"ZIP: {data['zip']}\n"
                f"Lat, Lon: {data['lat']}, {data['lon']}\n"
                f"Timezone: {data['timezone']}"
            )
        else:
            return f"❌ Error: {data['message']}"
    except Exception as e:
        return f"⚠️ Error: {e}"

def on_check():
    ip = entry.get().strip()
    if not ip:
        messagebox.showwarning("Input required", "Please enter an IP address.")
        return
    result = get_ip_info(ip)
    output_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("IP Info Tool")
root.geometry("400x350")

tk.Label(root, text="Enter IP Address:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack()

tk.Button(root, text="Check IP Info", command=on_check, font=("Arial", 12), bg="lightblue").pack(pady=15)

output_label = tk.Label(root, text="", font=("Arial", 11), justify="left", wraplength=370)
output_label.pack(pady=10)

root.mainloop()
