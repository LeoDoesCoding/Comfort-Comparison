import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Sample data for countries by continent
continent_countries = {
    "Asia": ["China", "India", "Japan", "South Korea"],
    "Africa": ["Nigeria", "Egypt", "South Africa", "Kenya"],
    "North America": ["United States", "Canada", "Mexico"],
    "South America": ["Brazil", "Argentina", "Colombia", "Chile"],
    "Europe": ["Germany", "France", "United Kingdom", "Italy"],
    "Australia": ["Australia", "New Zealand"],
    "Antarctica": []
}

def update_countries(event):
    # Update the country combobox based on the selected continent
    selected_continent1 = combo_box1.get()
    selected_continent2 = combo_box2.get()
    
    # Check which combobox triggered the event
    widget = event.widget
    if widget == combo_box1:
        if selected_continent1 in continent_countries:
            combo_box1_country['values'] = continent_countries[selected_continent1]
            combo_box1_country.set("")  # Reset the selected value
        else:
            combo_box1_country['values'] = []
    elif widget == combo_box2:
        if selected_continent2 in continent_countries:
            combo_box2_country['values'] = continent_countries[selected_continent2]
            combo_box2_country.set("")  # Reset the selected value
        else:
            combo_box2_country['values'] = []

def on_compare():
    # Function to handle the compare button click
    country1 = combo_box1_country.get()
    country2 = combo_box2_country.get()

    # Check if both countries are selected
    if not country1 or not country2:
        messagebox.showwarning("Warning", "Please select both countries.")
        return

    comparison_text = f"Comparing {country1} and {country2}"

    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("Comparison Result")

    # Add a label to display the comparison result
    label_result = tk.Label(new_window, text=comparison_text, font=("Arial", 12))
    label_result.pack(padx=10, pady=5)

# Main window
root = tk.Tk()
root.title("Country Comparison")

# Create a label at the top of the window
label_heading = tk.Label(root, text="Compare Countries", font=("Arial", 16, "bold"))
label_heading.pack(pady=10)

# Create a frame to hold the continent and country selections
frame_selection = tk.Frame(root)
frame_selection.pack(pady=5)

# Create a frame for the first continent and first country
frame_continent1 = tk.Frame(frame_selection)
frame_continent1.pack(side=tk.LEFT)

# Create header for the left side
label_header1 = tk.Label(frame_continent1, text="First Country", font=("Arial", 12, "bold"))
label_header1.grid(row=0, column=0, columnspan=2, pady=5)

# Create label and Combobox for the first continent
label1 = tk.Label(frame_continent1, text="First Continent")
label1.grid(row=1, column=0, padx=5)
combo_box1 = ttk.Combobox(frame_continent1, values=list(continent_countries.keys()))
combo_box1.grid(row=2, column=0, padx=5)
combo_box1.bind("<<ComboboxSelected>>", update_countries)

# Create label and Combobox for the first country
label1_country = tk.Label(frame_continent1, text="First Country")
label1_country.grid(row=3, column=0, padx=5)
combo_box1_country = ttk.Combobox(frame_continent1)
combo_box1_country.grid(row=4, column=0, padx=5)

# Create a frame for the second continent and second country
frame_continent2 = tk.Frame(frame_selection)
frame_continent2.pack(side=tk.LEFT)

# Create header for the right side
label_header2 = tk.Label(frame_continent2, text="Second Country", font=("Arial", 12, "bold"))
label_header2.grid(row=0, column=0, columnspan=2, pady=5)

# Create label and Combobox for the second continent
label2 = tk.Label(frame_continent2, text="Second Continent")
label2.grid(row=1, column=0, padx=5)
combo_box2 = ttk.Combobox(frame_continent2, values=list(continent_countries.keys()))
combo_box2.grid(row=2, column=0, padx=5)
combo_box2.bind("<<ComboboxSelected>>", update_countries)

# Create label and Combobox for the second country
label2_country = tk.Label(frame_continent2, text="Second Country")
label2_country.grid(row=3, column=0, padx=5)
combo_box2_country = ttk.Combobox(frame_continent2)
combo_box2_country.grid(row=4, column=0, padx=5)

# Create the compare button
button_compare = tk.Button(root, text="Compare", command=on_compare)
button_compare.pack(pady=10)

# Main loop
root.mainloop()
