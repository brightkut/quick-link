import tkinter as tk
import webbrowser

# Your grouped URLs
env_links = {
    "dev": {
        "Google Dev": "https://www.google.com",
        "Localhost Dev": "http://localhost:8000",
    },
    "uat": {
        "Google UAT": "https://www.google2.com",
        "Localhost UAT": "http://localhost:8080",
    },
}


def open_url(url):
    webbrowser.open(url)


def create_env_section(root, env_name, sites):
    frame = tk.LabelFrame(root, text=env_name.upper(), padx=10, pady=5)
    frame.pack(fill="x", padx=10, pady=5)
    for name, url in sites.items():
        btn = tk.Button(
            frame, text=f"{name}: {url}", anchor="w", command=lambda u=url: open_url(u)
        )
        btn.pack(fill="x", pady=2)


# Main app
root = tk.Tk()
root.title("Quick Link App")
root.geometry("500x300")

# Create all env sections
for env, links in env_links.items():
    create_env_section(root, env, links)

root.mainloop()
