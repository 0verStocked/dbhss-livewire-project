import tkinter as tk
import requests
from prettytable import PrettyTable

def fetch_data():
    try:
        country_code = ccd_entry.get()
        sub_country_code = scd_entry.get()

        url = "https://livescore6.p.rapidapi.com/leagues/v2/get-table"
        querystring = {"Category": "soccer", "Ccd": country_code, "Scd": sub_country_code}
        headers = {
            "X-RapidAPI-Key": "789934d09amshd53ef6cfa09b940p1cd65cjsn86deb634114e",
            "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        if "LeagueTable" in data:
            standings = data["LeagueTable"]["L"][0]["Tables"][0]["team"]

            # Create a table to display the data
            table = PrettyTable()
            table.field_names = ["Rank", "Team", "Wins", "Draws", "Losses", "Goals For", "Goals Against", "Points"]

            for team_data in standings:
                table.add_row([
                    team_data["rnk"],
                    team_data["Tnm"],
                    team_data["win"],
                    team_data["drw"],
                    team_data["lst"],
                    team_data["gf"],
                    team_data["ga"],
                    team_data["ptsn"]
                ])

            result_text.delete(1.0, tk.END)  # Clear the previous result
            result_text.insert(tk.END, table)
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "No data found.")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(e))

# Create the main window
root = tk.Tk()
root.title("LiveScore Data Fetcher")

# Create and pack labels and entry widgets
ccd_label = tk.Label(root, text="Country Code (e.g., spain):")
ccd_label.pack()
ccd_entry = tk.Entry(root)
ccd_entry.pack()

scd_label = tk.Label(root, text="Sub-Country Code (e.g., laliga):")
scd_label.pack()
scd_entry = tk.Entry(root)
scd_entry.pack()

# Create and pack a fetch button
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack()

# Create and pack a text widget to display the result
result_text = tk.Text(root, wrap=tk.WORD)
result_text.pack()

# Start the GUI main loop
root.mainloop()
