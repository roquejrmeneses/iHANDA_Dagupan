from builtins import enumerate
import tkinter as tk
from tkinter import messagebox
import sqlite3

# ==============================
# DATABASE SETUP
# ==============================

def create_database():

    connection = sqlite3.connect("ihanda_dagupan.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emergency_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            emergency_type TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


create_database()


# ==============================
# FEATURE FUNCTIONS
# ==============================


def disaster_recognition():

    # Create new window
    disaster_window = tk.Toplevel(window)
    disaster_window.title("Disaster Recognition | iHANDA Dagupan")
    disaster_window.geometry("750x650")
    disaster_window.resizable(False, False)

    # Title
    title = tk.Label(
        disaster_window,
        text="Disaster Recognition",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=(25, 5))

    subtitle = tk.Label(
        disaster_window,
        text=(
            "Learn about common disasters and the proper actions "
            "to take before, during, and after an emergency."
        ),
        font=("Arial", 11),
        wraplength=650,
        justify="center"
    )
    subtitle.pack(pady=(0, 20))

    # Disaster selection
    selection_label = tk.Label(
        disaster_window,
        text="Select a disaster:",
        font=("Arial", 13, "bold")
    )
    selection_label.pack(pady=5)

    # Content area
    content_frame = tk.Frame(disaster_window)
    content_frame.pack(fill="both", expand=True, padx=30, pady=15)

    content_text = tk.Text(
        content_frame,
        width=75,
        height=22,
        font=("Arial", 11),
        wrap="word"
    )
    content_text.pack(fill="both", expand=True)

    # Disaster information
    disasters = {

        "Flood": """
FLOOD

What is a Flood?

Floods can be caused by heavy rainfall, overflowing rivers,
poor drainage, or coastal storm surges. Floodwater can be
dangerous because of strong currents and contamination.


BEFORE

• Prepare emergency supplies.
• Secure important belongings.
• Monitor official weather and emergency updates.


DURING

• Move to higher ground when necessary.
• Avoid walking or driving through floodwaters.
• Follow instructions from local authorities.


AFTER

• Avoid contaminated floodwater.
• Clean affected areas safely.
• Check for possible structural damage.
""",

        "Earthquake": """
EARTHQUAKE

What is an Earthquake?

Earthquakes occur when there is sudden movement beneath
the Earth's surface. They can damage buildings, roads,
and utilities.


BEFORE

• Secure heavy furniture and objects.
• Identify safe areas inside your home or building.
• Prepare an emergency kit.


DURING

• Stay calm.
• Perform DROP, COVER, and HOLD.
• Stay away from windows and objects that may fall.


AFTER

• Check for injuries.
• Move to a safe open area when necessary.
• Avoid damaged buildings and structures.
""",

        "Fire": """
FIRE

What is a Fire Emergency?

Fires may be caused by electrical problems, gas leaks,
unattended cooking, or other sources. Fires can spread
quickly and produce dangerous smoke.


BEFORE

• Check electrical wiring regularly.
• Avoid overloading electrical outlets.
• Know your building's fire exits.


DURING

• Evacuate immediately when necessary.
• Stay low if there is smoke.
• Call emergency services.


AFTER

• Do not return to the area until authorities declare it safe.
• Avoid damaged electrical equipment.
• Follow instructions from emergency personnel.
""",

        "Tsunami": """
TSUNAMI

What is a Tsunami?

A tsunami is a series of large waves that can be caused
by underwater earthquakes, landslides, or other disturbances.
Coastal areas may be at risk.


BEFORE

• Know evacuation routes.
• Learn the warning signs of a tsunami.
• Prepare an emergency go-bag.


DURING

• Move immediately to higher ground or a safe location.
• Stay away from coastal areas.
• Follow official warnings and evacuation orders.


AFTER

• Stay away from the coast until authorities declare it safe.
• Watch for official announcements.
• Do not return to evacuated areas without clearance.
"""
    }

    # Function to display disaster information
    def show_disaster(disaster_name):
        content_text.delete("1.0", tk.END)
        content_text.insert(
            tk.END,
            disasters[disaster_name]
        )

    # Buttons
    button_frame = tk.Frame(disaster_window)
    button_frame.pack(pady=10)

    for disaster in disasters:
        tk.Button(
            button_frame,
            text=disaster,
            width=15,
            font=("Arial", 10, "bold"),
            command=lambda d=disaster: show_disaster(d)
        ).pack(side="left", padx=5)

    # Back button
    tk.Button(
        disaster_window,
        text="BACK",
        width=15,
        height=2,
        font=("Arial", 10, "bold"),
        command=disaster_window.destroy
    ).pack(pady=15)




def safe_zone():

    # Create Safe Zone window
    safe_window = tk.Toplevel(window)
    safe_window.title("Safe Zone | iHANDA Dagupan")
    safe_window.geometry("700x600")
    safe_window.resizable(False, False)

    # Title
    title = tk.Label(
        safe_window,
        text="Safe Zone",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=(25, 5))

    subtitle = tk.Label(
        safe_window,
        text="Recommended evacuation and safety locations in Dagupan City",
        font=("Arial", 11),
        wraplength=600,
        justify="center"
    )
    subtitle.pack(pady=(0, 20))

    # Location information
    locations = {

        "Dagupan City Evacuation Center": (
            "Dagupan City Evacuation Center\n\n"
            "A designated location intended to provide temporary "
            "shelter for residents during emergencies and disasters.\n\n"
            "IMPORTANT:\n"
            "Follow official evacuation instructions before going "
            "to an evacuation center."
        ),

        "Region I Medical Center": (
            "Region I Medical Center\n\n"
            "A medical facility that can provide healthcare services "
            "during emergencies.\n\n"
            "IMPORTANT:\n"
            "For medical emergencies, contact emergency services "
            "or follow instructions from authorities."
        ),

        "Dagupan City Fire Station": (
            "Dagupan City Fire Station\n\n"
            "A facility responsible for fire response and related "
            "emergency assistance.\n\n"
            "IMPORTANT:\n"
            "Call the appropriate emergency hotline during a fire "
            "or other emergency."
        ),

        "Dagupan City Police Station": (
            "Dagupan City Police Station\n\n"
            "Provides police assistance and emergency response "
            "for public safety concerns.\n\n"
            "IMPORTANT:\n"
            "Contact authorities when immediate assistance is needed."
        ),

        "Public Schools / Evacuation Centers": (
            "Public Schools Used as Evacuation Centers\n\n"
            "Some public schools may be designated as temporary "
            "evacuation centers during disasters.\n\n"
            "IMPORTANT:\n"
            "The availability of a school as an evacuation center "
            "depends on official announcements."
        ),

        "PHINMA University of Pangasinan": (
            "PHINMA University of Pangasinan\n\n"
            "The university may serve as an accessible location "
            "for students and members of the community during "
            "certain emergencies.\n\n"
            "IMPORTANT:\n"
            "Always follow official evacuation instructions and "
            "confirm whether the location is currently being used "
            "as an evacuation area."
        )
    }

    # Location list
    list_frame = tk.Frame(safe_window)
    list_frame.pack(padx=30, pady=10)

    location_list = tk.Listbox(
        list_frame,
        width=55,
        height=10,
        font=("Arial", 11)
    )
    location_list.pack(side="left")

    # Scrollbar
    scrollbar = tk.Scrollbar(
        list_frame,
        command=location_list.yview
    )
    scrollbar.pack(side="right", fill="y")

    location_list.config(
        yscrollcommand=scrollbar.set
    )

    # Add locations to list
    for location in locations:
        location_list.insert(tk.END, location)

    # Information box
    info_label = tk.Label(
        safe_window,
        text="Location Information",
        font=("Arial", 13, "bold")
    )
    info_label.pack(pady=(15, 5))

    info_text = tk.Text(
        safe_window,
        width=70,
        height=9,
        font=("Arial", 10),
        wrap="word"
    )
    info_text.pack(padx=30)

    # Show selected location
    def show_location():
        selected = location_list.curselection()

        if not selected:
            messagebox.showwarning(
                "No Location Selected",
                "Please select a location first."
            )
            return

        location = location_list.get(selected[0])

        info_text.delete("1.0", tk.END)
        info_text.insert(
            tk.END,
            locations[location]
        )

    # View button
    tk.Button(
        safe_window,
        text="VIEW INFORMATION",
        width=22,
        height=2,
        font=("Arial", 10, "bold"),
        command=show_location
    ).pack(pady=12)

    # Back button
    tk.Button(
        safe_window,
        text="BACK",
        width=15,
        height=2,
        font=("Arial", 10, "bold"),
        command=safe_window.destroy
    ).pack()

def emergency_checklist():

    # Create Emergency Checklist window
    checklist_window = tk.Toplevel(window)
    checklist_window.title("Emergency Checklist | iHANDA Dagupan")
    checklist_window.geometry("700x650")
    checklist_window.resizable(False, False)

    # Title
    title = tk.Label(
        checklist_window,
        text="Emergency Checklist",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=(25, 5))

    subtitle = tk.Label(
        checklist_window,
        text="Prepare these important items before an emergency.",
        font=("Arial", 11),
        wraplength=600,
        justify="center"
    )
    subtitle.pack(pady=(0, 20))

    # Checklist items
    checklist_items = [
        "Emergency Go Bag",
        "3-Day Water Supply",
        "Non-Perishable Food",
        "Flashlight and Extra Batteries",
        "First Aid Kit",
        "Important Documents",
        "Whistle and Power Bank"
    ]

    # Variables for checkboxes
    checklist_vars = []

    # Checklist frame
    checklist_frame = tk.Frame(checklist_window)
    checklist_frame.pack(padx=40, fill="x")

    # Create checkboxes
    for item in checklist_items:

        var = tk.BooleanVar()
        checklist_vars.append(var)

        checkbox = tk.Checkbutton(
            checklist_frame,
            text=item,
            variable=var,
            font=("Arial", 12),
            anchor="w"
        )
        checkbox.pack(fill="x", pady=6)

    # Progress label
    progress_label = tk.Label(
        checklist_window,
        text="Checklist Progress: 0 / 7",
        font=("Arial", 13, "bold")
    )
    progress_label.pack(pady=(25, 10))

    # Check progress function
    def check_progress():

        completed = 0

        for var in checklist_vars:
            if var.get():
                completed += 1

        total = len(checklist_items)

        progress = (completed / total) * 100

        progress_label.config(
            text=f"Checklist Progress: {completed} / {total} ({progress:.0f}%)"
        )

        if completed == total:
            messagebox.showinfo(
                "Checklist Complete",
                "Great! You have checked all emergency preparedness items."
            )

        elif completed > 0:
            messagebox.showinfo(
                "Checklist Progress",
                f"You have completed {completed} out of {total} items.\n\n"
                "Continue preparing the remaining items."
            )

        else:
            messagebox.showwarning(
                "Checklist Empty",
                "Please check the items you already have prepared."
            )

    # Reset function
    def reset_checklist():

        for var in checklist_vars:
            var.set(False)

        progress_label.config(
            text="Checklist Progress: 0 / 7"
        )

    # Button frame
    button_frame = tk.Frame(checklist_window)
    button_frame.pack(pady=20)

    # Check progress button
    tk.Button(
        button_frame,
        text="CHECK PROGRESS",
        width=18,
        height=2,
        font=("Arial", 10, "bold"),
        command=check_progress
    ).pack(side="left", padx=5)

    # Reset button
    tk.Button(
        button_frame,
        text="RESET",
        width=12,
        height=2,
        font=("Arial", 10, "bold"),
        command=reset_checklist
    ).pack(side="left", padx=5)

    # Back button
    tk.Button(
        checklist_window,
        text="BACK",
        width=15,
        height=2,
        font=("Arial", 10, "bold"),
        command=checklist_window.destroy
    ).pack()


def emergency_hotlines():

    # Create Emergency Hotlines window
    hotline_window = tk.Toplevel(window)
    hotline_window.title("Emergency Hotlines | iHANDA Dagupan")
    hotline_window.geometry("700x650")
    hotline_window.resizable(False, False)

    # Title
    title = tk.Label(
        hotline_window,
        text="Emergency Hotlines",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=(25, 5))

    subtitle = tk.Label(
        hotline_window,
        text="Important emergency contact numbers",
        font=("Arial", 11)
    )
    subtitle.pack(pady=(0, 20))

    # Emergency hotline information
    hotlines = [
        ("National Emergency Hotline", "911"),
        ("CDRRMO", "0968-444-9598"),
        ("Dagupan City Police Station", "0933-502-4899 / 529-5604"),
        ("Panda Volunteer Fire Brigade", "0932-548-1545"),
        ("Philippine Red Cross", "(075) 515-4577"),
        ("POSO", "0998-173-9525"),
        ("Dagupan City Fire Station", "0917-184-2611"),
        ("PNP Maritime Group", "0967-008-0092"),
        ("City Health Office", "0997-840-1377")
    ]

    # Main frame
    hotline_frame = tk.Frame(hotline_window)
    hotline_frame.pack(padx=30, pady=10)

    # Header
    tk.Label(
        hotline_frame,
        text="OFFICE / SERVICE",
        font=("Arial", 11, "bold"),
        width=35,
        anchor="w"
    ).grid(row=0, column=0, padx=5, pady=8)

    tk.Label(
        hotline_frame,
        text="CONTACT NUMBER",
        font=("Arial", 11, "bold"),
        width=25,
        anchor="w"
    ).grid(row=0, column=1, padx=5, pady=8)

    # Display hotlines
    for row, (office, number) in enumerate(hotlines, start=1):

        tk.Label(
            hotline_frame,
            text=office,
            font=("Arial", 10),
            width=35,
            anchor="w"
        ).grid(row=row, column=0, padx=5, pady=6)

        tk.Label(
            hotline_frame,
            text=number,
            font=("Arial", 10, "bold"),
            width=25,
            anchor="w"
        ).grid(row=row, column=1, padx=5, pady=6)

    # Reminder
    reminder = tk.Label(
        hotline_window,
        text=(
            "IMPORTANT:\n"
            "Use emergency hotlines only when assistance is needed.\n"
            "For immediate emergencies, call 911."
        ),
        font=("Arial", 10),
        justify="center",
        wraplength=600
    )
    reminder.pack(pady=15)

    # Back button
    tk.Button(
        hotline_window,
        text="BACK",
        width=15,
        height=2,
        font=("Arial", 10, "bold"),
        command=hotline_window.destroy
    ).pack()


def report_emergency():

    # Create Report Emergency window
    report_window = tk.Toplevel(window)
    report_window.title("Report Emergency | iHANDA Dagupan")
    report_window.geometry("650x650")
    report_window.resizable(False, False)

    # Title
    title = tk.Label(
        report_window,
        text="Report Emergency",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=(25, 5))

    subtitle = tk.Label(
        report_window,
        text="Submit an emergency report through iHANDA Dagupan.",
        font=("Arial", 11),
        wraplength=550,
        justify="center"
    )
    subtitle.pack(pady=(0, 20))

    # Form frame
    form_frame = tk.Frame(report_window)
    form_frame.pack(padx=50, fill="x")

    # Name
    tk.Label(
        form_frame,
        text="Name:",
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    name_entry = tk.Entry(
        form_frame,
        font=("Arial", 11)
    )
    name_entry.pack(fill="x", pady=(5, 15))

    # Emergency Type
    tk.Label(
        form_frame,
        text="Emergency Type:",
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    emergency_type = tk.StringVar()
    emergency_type.set("Select Emergency Type")

    emergency_menu = tk.OptionMenu(
        form_frame,
        emergency_type,
        "Flood",
        "Earthquake",
        "Fire",
        "Tsunami",
        "Other"
    )
    emergency_menu.config(
        font=("Arial", 10)
    )
    emergency_menu.pack(fill="x", pady=(5, 15))

    # Location
    tk.Label(
        form_frame,
        text="Location:",
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    location_entry = tk.Entry(
        form_frame,
        font=("Arial", 11)
    )
    location_entry.pack(fill="x", pady=(5, 15))

    # Description
    tk.Label(
        form_frame,
        text="Description:",
        font=("Arial", 11, "bold")
    ).pack(anchor="w")

    description_text = tk.Text(
        form_frame,
        height=7,
        font=("Arial", 10),
        wrap="word"
    )
    description_text.pack(fill="x", pady=(5, 15))

    # Submit report
    def submit_report():

        name = name_entry.get().strip()
        emergency = emergency_type.get()
        location = location_entry.get().strip()
        description = description_text.get("1.0", tk.END).strip()

        # Check if fields are empty
        if not name or emergency == "Select Emergency Type" or not location or not description:

            messagebox.showwarning(
                "Incomplete Form",
                "Please complete all fields before submitting."
            )

            return

        # Save report to database
        connection = sqlite3.connect("ihanda_dagupan.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO emergency_reports
            (name, emergency_type, location, description)
            VALUES (?, ?, ?, ?)
        """, (
            name,
            emergency,
            location,
            description
        ))

        connection.commit()
        connection.close()

        # Confirmation
        messagebox.showinfo(
            "Report Submitted",
            "Your emergency report has been successfully submitted."
        )

        # Clear form
        name_entry.delete(0, tk.END)
        emergency_type.set("Select Emergency Type")
        location_entry.delete(0, tk.END)
        description_text.delete("1.0", tk.END)

    # Submit button
    tk.Button(
        report_window,
        text="SUBMIT REPORT",
        width=20,
        height=2,
        font=("Arial", 10, "bold"),
        command=submit_report
    ).pack(pady=10)

    # Back button
    tk.Button(
        report_window,
        text="BACK",
        width=15,
        height=2,
        font=("Arial", 10, "bold"),
        command=report_window.destroy
    ).pack()


def emergency_responses():

    # ==============================
    # LOGIN WINDOW
    # ==============================

    login_window = tk.Toplevel(window)
    login_window.title("Emergency Responses | iHANDA Dagupan")
    login_window.geometry("450x400")
    login_window.resizable(False, False)

    tk.Label(
        login_window,
        text="Emergency Responses",
        font=("Arial", 22, "bold")
    ).pack(pady=(40, 10))

    tk.Label(
        login_window,
        text="Authorized Access Only",
        font=("Arial", 11)
    ).pack(pady=(0, 30))

    # Username
    tk.Label(
        login_window,
        text="Username",
        font=("Arial", 11, "bold")
    ).pack()

    username_entry = tk.Entry(
        login_window,
        font=("Arial", 11),
        width=30
    )
    username_entry.pack(pady=(5, 15))

    # Password
    tk.Label(
        login_window,
        text="Password",
        font=("Arial", 11, "bold")
    ).pack()

    password_entry = tk.Entry(
        login_window,
        font=("Arial", 11),
        width=30,
        show="*"
    )
    password_entry.pack(pady=(5, 20))

    # Login function
    def login():

        username = username_entry.get().strip()
        password = password_entry.get()

        # Temporary project login
        if username == "admin" and password == "ict123":
            login_window.destroy()
            open_responses_window()

        else:
            messagebox.showerror(
                "Login Failed",
                "Incorrect username or password."
            )

    # Login button
    tk.Button(
        login_window,
        text="LOGIN",
        width=18,
        height=2,
        font=("Arial", 10, "bold"),
        command=login
    ).pack(pady=5)

    # Back button
    tk.Button(
        login_window,
        text="BACK",
        width=12,
        height=2,
        font=("Arial", 10, "bold"),
        command=login_window.destroy
    ).pack(pady=5)


    # ==============================
    # EMERGENCY RESPONSES WINDOW
    # ==============================

    def open_responses_window():

        response_window = tk.Toplevel(window)
        response_window.title("Emergency Responses | iHANDA Dagupan")
        response_window.geometry("950x650")
        response_window.resizable(False, False)

        # Title
        tk.Label(
            response_window,
            text="Emergency Responses",
            font=("Arial", 24, "bold")
        ).pack(pady=(25, 5))

        tk.Label(
            response_window,
            text="Submitted emergency reports",
            font=("Arial", 11)
        ).pack(pady=(0, 20))

        # Table frame
        table_frame = tk.Frame(response_window)
        table_frame.pack(padx=25, fill="both", expand=True)

        # Scrollbars
        vertical_scrollbar = tk.Scrollbar(
            table_frame,
            orient="vertical"
        )

        horizontal_scrollbar = tk.Scrollbar(
            table_frame,
            orient="horizontal"
        )

        # Listbox
        report_list = tk.Listbox(
            table_frame,
            width=115,
            height=18,
            font=("Arial", 10),
            xscrollcommand=horizontal_scrollbar.set,
            yscrollcommand=vertical_scrollbar.set
        )

        vertical_scrollbar.config(
            command=report_list.yview
        )

        horizontal_scrollbar.config(
            command=report_list.xview
        )

        report_list.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scrollbar.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        table_frame.grid_rowconfigure(
            0,
            weight=1
        )

        table_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # Store report IDs
        report_ids = []

        # ==============================
        # LOAD REPORTS
        # ==============================

        def load_reports():

            report_list.delete(0, tk.END)
            report_ids.clear()

            connection = sqlite3.connect(
                "ihanda_dagupan.db"
            )

            cursor = connection.cursor()

            cursor.execute("""
                SELECT id, name, emergency_type, location
                FROM emergency_reports
                ORDER BY id DESC
            """)

            reports = cursor.fetchall()

            connection.close()

            if not reports:

                report_list.insert(
                    tk.END,
                    "No emergency reports found."
                )

                return

            # Header
            report_list.insert(
                tk.END,
                "ID     | NAME                 | TYPE          | LOCATION"
            )

            report_list.insert(
                tk.END,
                "-" * 85
            )

            for report in reports:

                report_id = report[0]
                name = report[1]
                emergency_type = report[2]
                location = report[3]

                report_ids.append(report_id)

                display_text = (
                    f"{report_id:<6} | "
                    f"{name:<20} | "
                    f"{emergency_type:<13} | "
                    f"{location}"
                )

                report_list.insert(
                    tk.END,
                    display_text
                )

        # ==============================
        # VIEW REPORT DETAILS
        # ==============================

        def view_details():

            selected = report_list.curselection()

            if not selected:
                messagebox.showwarning(
                    "No Report Selected",
                    "Please select an emergency report first."
                )
                return

            # Header rows cannot be selected
            if selected[0] < 2:
                messagebox.showwarning(
                    "Invalid Selection",
                    "Please select an emergency report."
                )
                return

            index = selected[0] - 2

            if index >= len(report_ids):
                return

            report_id = report_ids[index]

            connection = sqlite3.connect(
                "ihanda_dagupan.db"
            )

            cursor = connection.cursor()

            cursor.execute("""
                SELECT id, name, emergency_type, location, description
                FROM emergency_reports
                WHERE id = ?
            """, (report_id,))

            report = cursor.fetchone()

            connection.close()

            if report:

                details = (
                    f"Report ID: {report[0]}\n\n"
                    f"Name: {report[1]}\n\n"
                    f"Emergency Type: {report[2]}\n\n"
                    f"Location: {report[3]}\n\n"
                    f"Description:\n{report[4]}"
                )

                messagebox.showinfo(
                    "Emergency Report Details",
                    details
                )

        # ==============================
        # DELETE REPORT
        # ==============================

        def delete_report():

            selected = report_list.curselection()

            if not selected:
                messagebox.showwarning(
                    "No Report Selected",
                    "Please select an emergency report first."
                )
                return

            if selected[0] < 2:
                messagebox.showwarning(
                    "Invalid Selection",
                    "Please select an emergency report."
                )
                return

            index = selected[0] - 2

            if index >= len(report_ids):
                return

            report_id = report_ids[index]

            confirm = messagebox.askyesno(
                "Delete Report",
                "Are you sure you want to delete this report?"
            )

            if not confirm:
                return

            connection = sqlite3.connect(
                "ihanda_dagupan.db"
            )

            cursor = connection.cursor()

            cursor.execute("""
                DELETE FROM emergency_reports
                WHERE id = ?
            """, (report_id,))

            connection.commit()
            connection.close()

            messagebox.showinfo(
                "Report Deleted",
                "The emergency report has been deleted."
            )

            load_reports()

        # ==============================
        # BUTTONS
        # ==============================

        button_frame = tk.Frame(response_window)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="VIEW DETAILS",
            width=18,
            height=2,
            font=("Arial", 10, "bold"),
            command=view_details
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="REFRESH",
            width=15,
            height=2,
            font=("Arial", 10, "bold"),
            command=load_reports
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="DELETE REPORT",
            width=18,
            height=2,
            font=("Arial", 10, "bold"),
            command=delete_report
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="LOGOUT",
            width=15,
            height=2,
            font=("Arial", 10, "bold"),
            command=response_window.destroy
        ).pack(side="left", padx=5)

        # Load reports immediately
        load_reports()


def exit_program():
    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit iHANDA Dagupan?"
    )

    if answer:
        window.destroy()


# ==============================
# MAIN WINDOW
# ==============================

# ==============================
# MAIN WINDOW
# ==============================

window = tk.Tk()
window.title("iHANDA Dagupan")
window.geometry("700x700")
window.resizable(False, False)


# ==============================
# MAIN FUNCTIONS
# ==============================

def show_about():
    messagebox.showinfo(
        "About iHANDA Dagupan",
        "iHANDA Dagupan\n\n"
        "A community-based disaster preparedness "
        "and emergency reporting system.\n\n"
        "Developed using Python, Tkinter, and SQLite."
    )


# ==============================
# HEADER
# ==============================

header_frame = tk.Frame(window)
header_frame.pack(pady=(35, 10))

tk.Label(
    header_frame,
    text="iHANDA Dagupan",
    font=("Arial", 30, "bold")
).pack()

tk.Label(
    header_frame,
    text="Disaster Preparedness & Emergency Reporting System",
    font=("Arial", 11)
).pack(pady=5)


# ==============================
# DESCRIPTION
# ==============================

description = tk.Label(
    window,
    text=(
        "Prepare. Stay informed. Respond responsibly.\n\n"
        "Access disaster information, safety locations,\n"
        "emergency checklists, hotlines, and reporting tools."
    ),
    font=("Arial", 11),
    justify="center"
)

description.pack(pady=(10, 25))


# ==============================
# FEATURES FRAME
# ==============================

features_frame = tk.Frame(window)
features_frame.pack()


# Row 1
tk.Button(
    features_frame,
    text="DISASTER RECOGNITION",
    width=28,
    height=2,
    font=("Arial", 10, "bold"),
    command=disaster_recognition
).grid(row=0, column=0, padx=8, pady=8)


tk.Button(
    features_frame,
    text="SAFE ZONE",
    width=28,
    height=2,
    font=("Arial", 10, "bold"),
    command=safe_zone
).grid(row=0, column=1, padx=8, pady=8)


# Row 2
tk.Button(
    features_frame,
    text="EMERGENCY CHECKLIST",
    width=28,
    height=2,
    font=("Arial", 10, "bold"),
    command=emergency_checklist
).grid(row=1, column=0, padx=8, pady=8)


tk.Button(
    features_frame,
    text="EMERGENCY HOTLINES",
    width=28,
    height=2,
    font=("Arial", 10, "bold"),
    command=emergency_hotlines
).grid(row=1, column=1, padx=8, pady=8)


# Row 3
tk.Button(
    features_frame,
    text="REPORT EMERGENCY",
    width=28,
    height=2,
    font=("Arial", 10, "bold"),
    command=report_emergency
).grid(row=2, column=0, padx=8, pady=8)


tk.Button(
    features_frame,
    text="EMERGENCY RESPONSES",
    width=28,
    height=2,
    font=("Arial", 10, "bold"),
    command=emergency_responses
).grid(row=2, column=1, padx=8, pady=8)


# ==============================
# BOTTOM BUTTONS
# ==============================

bottom_frame = tk.Frame(window)
bottom_frame.pack(pady=25)


tk.Button(
    bottom_frame,
    text="ABOUT",
    width=15,
    height=2,
    font=("Arial", 10, "bold"),
    command=show_about
).pack(side="left", padx=8)


tk.Button(
    bottom_frame,
    text="EXIT",
    width=15,
    height=2,
    font=("Arial", 10, "bold"),
    command=window.destroy
).pack(side="left", padx=8)


# ==============================
# FOOTER
# ==============================

tk.Label(
    window,
    text="iHANDA Dagupan • Python Project",
    font=("Arial", 9)
).pack(side="bottom", pady=15)


# ==============================
# RUN PROGRAM
# ==============================

window.mainloop()