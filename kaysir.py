import tkinter as tk

window = tk.Tk()
window.title("iHANDA Dagupan")
window.geometry("900x650")
window.minsize(700, 500)


# =========================
# HEADER
# =========================

header = tk.Frame(
    window,
    height=120
)

header.pack(fill="x")
header.pack_propagate(False)


tk.Label(
    header,
    text="iHANDA Dagupan",
    font=("Arial", 30, "bold")
).pack(
    pady=(20, 0)
)


tk.Label(
    header,
    text="Disaster Preparedness System",
    font=("Arial", 12)
).pack()


# =========================
# NAVIGATION
# =========================

navigation = tk.Frame(
    window
)

navigation.pack(
    fill="x",
    pady=5
)


tk.Button(
    navigation,
    text="Home",
    width=20,
    command=lambda: show_home()
).pack(
    side="left",
    padx=5
)


tk.Button(
    navigation,
    text="Disaster Recognition",
    width=20,
    command=lambda: show_disaster()
).pack(
    side="left",
    padx=5
)


tk.Button(
    navigation,
    text="Safety Precautions / Ready Kit",
    width=25,
    command=lambda: show_ready_kit()
).pack(
    side="left",
    padx=5
)


# =========================
# CONTENT
# =========================

content = tk.Frame(
    window
)

content.pack(
    fill="both",
    expand=True
)


# =========================
# FOOTER
# =========================

tk.Label(
    window,
    text="© iHANDA Dagupan 2026",
    font=("Arial", 9)
).pack(
    fill="x",
    side="bottom",
    pady=8
)


# =========================
# CLEAR
# =========================

def clear():

    for item in content.winfo_children():
        item.destroy()


# =========================
# HOME
# =========================

def show_home():

    clear()

    area = tk.Frame(
        content
    )

    area.pack(
        fill="both",
        expand=True,
        padx=45,
        pady=20
    )

    canvas = tk.Canvas(
        area,
        highlightthickness=0
    )

    scrollbar = tk.Scrollbar(
        area,
        orient="vertical",
        command=canvas.yview
    )

    home_box = tk.Frame(
        canvas
    )

    canvas_window = canvas.create_window(
        (0, 0),
        window=home_box,
        anchor="nw"
    )


    def update_home_scroll(event):

        canvas.configure(
            scrollregion=canvas.bbox("all")
        )


    home_box.bind(
        "<Configure>",
        update_home_scroll
    )


    def resize_home(event):

        canvas.itemconfig(
            canvas_window,
            width=event.width
        )


    canvas.bind(
        "<Configure>",
        resize_home
    )


    canvas.configure(
        yscrollcommand=scrollbar.set
    )


    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )


    scrollbar.pack(
        side="right",
        fill="y"
    )


    # =========================
    # WELCOME
    # =========================

    tk.Label(
        home_box,
        text="Welcome to iHANDA Dagupan",
        font=("Arial", 23, "bold")
    ).pack(
        pady=(10, 15)
    )


    tk.Label(
        home_box,
        text="iHANDA Dagupan is a community-based disaster preparedness "
             "information system designed to help residents of Dagupan City "
             "become more informed and prepared for disasters.",
        font=("Arial", 11),
        wraplength=750,
        justify="left"
    ).pack(
        fill="x",
        pady=5
    )


    tk.Label(
        home_box,
        text="This platform aims to help residents stay informed, prepared, "
             "and safe before, during, and after disasters.",
        font=("Arial", 11),
        wraplength=750,
        justify="left"
    ).pack(
        fill="x",
        pady=(5, 20)
    )


    # =========================
    # WHAT YOU CAN FIND
    # =========================

    tk.Label(
        home_box,
        text="What You Can Find",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        pady=(5, 10)
    )


    tk.Label(
        home_box,
        text="• Disaster Recognition\n"
             "Learn about common disasters such as floods, earthquakes, "
             "fires, and tsunamis, including their warning signs and safety measures.\n\n"

             "• Safety Precautions / Ready Kit\n"
             "Learn what to prepare before an emergency and what important "
             "supplies should be included in an emergency kit.\n\n"

             "• Safe Zone Locations\n"
             "Identify safe areas and evacuation locations that may be used "
             "during emergencies.\n\n"

             "• Emergency Hotlines\n"
             "Access important emergency contact information for assistance "
             "during disasters.\n\n"

             "• Emergency Reporting\n"
             "Provide information about urgent situations so that proper "
             "authorities or responders can be informed.",
        font=("Arial", 10),
        wraplength=750,
        justify="left"
    ).pack(
        fill="x",
        pady=(0, 20)
    )


    # =========================
    # BE PREPARED
    # =========================

    tk.Label(
        home_box,
        text="Be Prepared, Stay Safe",
        font=("Arial", 17, "bold")
    ).pack(
        anchor="w",
        pady=(5, 10)
    )


    tk.Label(
        home_box,
        text="Disasters can happen unexpectedly. Being prepared, following "
             "official warnings, knowing evacuation routes, and having an "
             "emergency kit can help reduce risks and protect individuals, "
             "families, and communities.",
        font=("Arial", 10),
        wraplength=750,
        justify="left"
    ).pack(
        fill="x",
        pady=(0, 20)
    )


    tk.Label(
        home_box,
        text="© 2026 iHANDA Dagupan | Disaster Preparedness for Dagupan City",
        font=("Arial", 9)
    ).pack(
        pady=(5, 20)
    )


    def home_mouse_scroll(event):

        canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )


    canvas.bind(
        "<MouseWheel>",
        home_mouse_scroll
    )


# =========================
# READY KIT
# =========================

def show_ready_kit():

    clear()

    tk.Label(
        content,
        text="Safety Precautions / Ready Kit",
        font=("Arial", 22, "bold")
    ).pack(
        pady=(25, 10)
    )


    tk.Label(
        content,
        text="What is a Ready Kit?",
        font=("Arial", 15, "bold")
    ).pack(
        pady=(5, 5)
    )


    tk.Label(
        content,
        text="A ready kit or emergency kit contains important supplies "
             "that can help individuals and families during an emergency "
             "or disaster.",
        font=("Arial", 11),
        wraplength=700,
        justify="center"
    ).pack(
        pady=(0, 15)
    )


    # =========================
    # SCROLL AREA
    # =========================

    area = tk.Frame(
        content
    )

    area.pack(
        fill="both",
        expand=True,
        padx=60,
        pady=5
    )


    canvas = tk.Canvas(
        area,
        highlightthickness=0
    )


    scrollbar = tk.Scrollbar(
        area,
        orient="vertical",
        command=canvas.yview
    )


    box = tk.Frame(
        canvas
    )


    canvas_window = canvas.create_window(
        (0, 0),
        window=box,
        anchor="nw"
    )


    def update_ready_scroll(event):

        canvas.configure(
            scrollregion=canvas.bbox("all")
        )


    box.bind(
        "<Configure>",
        update_ready_scroll
    )


    def resize_ready(event):

        canvas.itemconfig(
            canvas_window,
            width=event.width
        )


    canvas.bind(
        "<Configure>",
        resize_ready
    )


    canvas.configure(
        yscrollcommand=scrollbar.set
    )


    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )


    scrollbar.pack(
        side="right",
        fill="y"
    )


    # =========================
    # RECOMMENDED ITEMS
    # =========================

    tk.Label(
        box,
        text="Recommended Items",
        font=("Arial", 15, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )


    items = [
        "Drinking water",
        "Ready-to-eat / non-perishable food",
        "Flashlight",
        "Extra batteries",
        "First aid kit",
        "Important documents",
        "Whistle",
        "Power bank",
        "Basic medicines",
        "Extra clothes",
        "Battery-powered or hand-crank radio",
        "Personal hygiene items",
        "Emergency contact information",
        "Cash",
        "Face masks"
    ]


    for item in items:

        tk.Label(
            box,
            text="• " + item,
            font=("Arial", 11),
            anchor="w"
        ).pack(
            fill="x",
            padx=25,
            pady=4
        )


    # =========================
    # GENERAL SAFETY
    # =========================

    tk.Label(
        box,
        text="General Safety Precautions",
        font=("Arial", 15, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )


    tk.Label(
        box,
        text="Before a Disaster",
        font=("Arial", 13, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(5, 5)
    )


    before_items = [
        "Know the hazards in your area.",
        "Prepare an emergency kit.",
        "Know your evacuation routes.",
        "Know your designated evacuation area.",
        "Keep important documents safe.",
        "Monitor official announcements.",
        "Make an emergency communication plan with your family."
    ]


    for item in before_items:

        tk.Label(
            box,
            text="• " + item,
            font=("Arial", 11),
            anchor="w",
            wraplength=700,
            justify="left"
        ).pack(
            fill="x",
            padx=25,
            pady=3
        )


    tk.Label(
        box,
        text="During a Disaster",
        font=("Arial", 13, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )


    during_items = [
        "Stay calm.",
        "Follow instructions from authorities.",
        "Stay in a safe location.",
        "Evacuate when instructed.",
        "Avoid dangerous areas.",
        "Do not spread unverified information."
    ]


    for item in during_items:

        tk.Label(
            box,
            text="• " + item,
            font=("Arial", 11),
            anchor="w",
            wraplength=700,
            justify="left"
        ).pack(
            fill="x",
            padx=25,
            pady=3
        )


    tk.Label(
        box,
        text="After a Disaster",
        font=("Arial", 13, "bold")
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )


    after_items = [
        "Wait for official announcements before returning to affected areas.",
        "Check for hazards around your home.",
        "Avoid damaged buildings and electrical wires.",
        "Continue monitoring official information.",
        "Help others when it is safe to do so."
    ]


    for item in after_items:

        tk.Label(
            box,
            text="• " + item,
            font=("Arial", 11),
            anchor="w",
            wraplength=700,
            justify="left"
        ).pack(
            fill="x",
            padx=25,
            pady=3
        )


    tk.Label(
        box,
        text="Sources: DOST-PAGASA and DOST-PHIVOLCS disaster preparedness guidance",
        font=("Arial", 9, "italic")
    ).pack(
        pady=20
    )


    def ready_mouse_scroll(event):

        canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )


    canvas.bind(
        "<MouseWheel>",
        ready_mouse_scroll
    )


# =========================
# DISASTER INFORMATION
# =========================

disasters = {

    "Flood": {

        "description":
            "A flood is the overflowing or accumulation of water that "
            "covers areas that are normally not submerged. Flooding can "
            "be caused by excessive rainfall, overflowing rivers and "
            "other bodies of water, and drainage problems.",

        "description_source":
            "[Source: DOST-PAGASA – Floods]",

        "Before": [
            "Know if your location is prone to flooding.",
            "Monitor weather conditions and flood warnings.",
            "Know your family's evacuation area and route.",
            "Prepare food and drinking water.",
            "Prepare a flashlight, radio, extra batteries, and first aid kit.",
            "Store important belongings above the expected flood level."
        ],

        "Before_source":
            "[Source: DOST-PAGASA – Flood Safety Rules: Before the Flood]",

        "During": [
            "Move to a safe area when evacuation is necessary.",
            "Avoid areas subject to sudden flooding.",
            "Do not cross rivers or flowing streams when the water is dangerous.",
            "Be careful around flooded roads and bridges.",
            "Listen to emergency instructions.",
            "Drink clean or preferably boiled water."
        ],

        "During_source":
            "[Source: DOST-PAGASA – Flood Safety Rules: During the Flood]",

        "After": [
            "Re-enter buildings with caution.",
            "Watch for broken electrical wires.",
            "Do not eat food or drink water that may have been contaminated.",
            "Report broken utility lines.",
            "Do not use electrical appliances until they have been checked.",
            "Continue following official instructions."
        ],

        "After_source":
            "[Source: DOST-PAGASA – Flood Safety Rules: After the Flood]"
    },


    "Earthquake": {

        "description":
            "An earthquake is the shaking of the ground caused by sudden "
            "movement beneath the Earth's surface. Strong earthquakes "
            "can damage buildings and other structures.",

        "description_source":
            "[Source: DOST-PHIVOLCS – Earthquake Preparedness]",

        "Before": [
            "Prepare an emergency kit.",
            "Secure heavy furniture and appliances.",
            "Fasten hanging objects.",
            "Know safe places inside your home, school, or workplace.",
            "Prepare a family communication and meeting plan."
        ],

        "Before_source":
            "[Source: DOST-PHIVOLCS – Earthquake Preparedness]",

        "During": [
            "DROP to the ground.",
            "COVER your head and body under a sturdy table or protect your head and neck.",
            "HOLD until the shaking stops.",
            "Stay away from windows and objects that may fall."
        ],

        "During_source":
            "[Source: DOST-PHIVOLCS – Earthquake Preparedness]",

        "After": [
            "Be prepared for possible aftershocks.",
            "Stay away from damaged buildings.",
            "Do not re-enter damaged buildings unless they have been declared safe.",
            "Watch for cracks and possible landslides.",
            "Follow official announcements and instructions."
        ],

        "After_source":
            "[Source: DOST-PHIVOLCS – Earthquake Preparedness]"
    },


    "Fire": {

        "description":
            "Fire is a rapid chemical reaction that produces heat and light. "
            "An uncontrolled fire can spread quickly and cause damage to "
            "people and property.",

        "description_source":
            "[Source: Bureau of Fire Protection – Fire Safety Guidelines]",

        "Before": [
            "Know the emergency exits.",
            "Keep exits clear.",
            "Know the location of fire extinguishers.",
            "Prepare an evacuation plan.",
            "Know the designated assembly area."
        ],

        "Before_source":
            "[Source: Bureau of Fire Protection – Fire Safety Guidelines]",

        "During": [
            "Stay calm.",
            "Follow the emergency evacuation route.",
            "Do not block exits.",
            "Do not use elevators during evacuation.",
            "Do not return for personal belongings.",
            "Follow instructions from firefighters and emergency responders."
        ],

        "During_source":
            "[Source: Bureau of Fire Protection – Fire Safety Guidelines]",

        "After": [
            "Do not immediately return to the building.",
            "Wait for authorities to determine if it is safe to re-enter.",
            "Stay away from damaged structures.",
            "Follow instructions from emergency responders."
        ],

        "After_source":
            "[Source: Bureau of Fire Protection – Fire Safety Guidelines]"
    },


    "Tsunami": {

        "description":
            "A tsunami is a series of sea waves commonly generated by "
            "undersea earthquakes. It can affect coastal areas and "
            "cause dangerous flooding.",

        "description_source":
            "[Source: DOST-PHIVOLCS – Introduction to Tsunami]",

        "Warning Signs": [
            "SHAKE – A strong earthquake is felt.",
            "DROP – The sea level suddenly rises or falls.",
            "ROAR – An unusual roaring sound from the sea may be heard."
        ],

        "Warning_source":
            "[Source: DOST-PHIVOLCS – Tsunami Safety and Preparedness]",

        "Before": [
            "Know if your community is near a tsunami-prone coastal area.",
            "Know your evacuation route.",
            "Identify higher ground or safer areas.",
            "Prepare an emergency kit.",
            "Learn the natural warning signs."
        ],

        "Before_source":
            "[Source: DOST-PHIVOLCS – Tsunami Safety and Preparedness]",

        "During": [
            "If you feel a strong earthquake near the coast, move to higher ground immediately.",
            "If the sea suddenly rises or falls, move to higher ground.",
            "Stay away from beaches and coastal areas.",
            "Do not go to the shoreline to watch the waves.",
            "Follow official tsunami warnings."
        ],

        "During_source":
            "[Source: DOST-PHIVOLCS – Tsunami Safety and Preparedness]",

        "After": [
            "Do not return to coastal areas until authorities say it is safe.",
            "Continue monitoring official announcements.",
            "Stay away from damaged and dangerous areas.",
            "Be alert for additional waves."
        ],

        "After_source":
            "[Source: DOST-PHIVOLCS – Tsunami Safety and Preparedness]"
    }
}


# =========================
# DISASTER PAGE
# =========================

def show_disaster(name=None):

    clear()

    tk.Label(
        content,
        text="Disaster Recognition",
        font=("Arial", 22, "bold")
    ).pack(
        pady=(20, 5)
    )


    tk.Label(
        content,
        text="Disaster Recognition helps residents understand different "
             "types of disasters and learn the proper actions to take "
             "before, during, and after an emergency. Select a disaster "
             "below to view important safety tips.",
        font=("Arial", 10),
        wraplength=750,
        justify="center"
    ).pack(
        pady=(0, 10)
    )


    # =========================
    # DISASTER BUTTONS
    # =========================

    buttons = tk.Frame(
        content
    )

    buttons.pack(
        pady=5
    )


    for disaster in disasters:

        tk.Button(
            buttons,
            text=disaster,
            width=12,
            command=lambda d=disaster: show_disaster(d)
        ).pack(
            side="left",
            padx=4
        )


    # =========================
    # SCROLL AREA
    # =========================

    area = tk.Frame(
        content
    )

    area.pack(
        fill="both",
        expand=True,
        padx=40,
        pady=10
    )


    canvas = tk.Canvas(
        area,
        highlightthickness=0
    )


    scrollbar = tk.Scrollbar(
        area,
        orient="vertical",
        command=canvas.yview
    )


    info = tk.Frame(
        canvas
    )


    canvas_window = canvas.create_window(
        (0, 0),
        window=info,
        anchor="nw"
    )


    def update_scroll(event):

        canvas.configure(
            scrollregion=canvas.bbox("all")
        )


    info.bind(
        "<Configure>",
        update_scroll
    )


    def resize_info(event):

        canvas.itemconfig(
            canvas_window,
            width=event.width
        )


    canvas.bind(
        "<Configure>",
        resize_info
    )


    canvas.configure(
        yscrollcommand=scrollbar.set
    )


    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )


    scrollbar.pack(
        side="right",
        fill="y"
    )


    # =========================
    # INFORMATION
    # =========================

    if name:

        tk.Label(
            info,
            text=name,
            font=("Arial", 20, "bold")
        ).pack(
            pady=(15, 8)
        )


        tk.Label(
            info,
            text="What is " + name + "?",
            font=("Arial", 15, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(5, 5)
        )


        tk.Label(
            info,
            text=disasters[name]["description"],
            font=("Arial", 11),
            wraplength=700,
            justify="left"
        ).pack(
            fill="x",
            padx=25,
            pady=(0, 5)
        )


        tk.Label(
            info,
            text=disasters[name]["description_source"],
            font=("Arial", 9, "italic"),
            wraplength=700,
            justify="left"
        ).pack(
            fill="x",
            padx=25,
            pady=(0, 15)
        )


        # =========================
        # TSUNAMI WARNING SIGNS
        # =========================

        if name == "Tsunami":

            tk.Label(
                info,
                text="Natural Warning Signs",
                font=("Arial", 15, "bold")
            ).pack(
                anchor="w",
                padx=25,
                pady=(5, 5)
            )


            for text in disasters[name]["Warning Signs"]:

                tk.Label(
                    info,
                    text="• " + text,
                    font=("Arial", 11),
                    wraplength=700,
                    justify="left",
                    anchor="w"
                ).pack(
                    fill="x",
                    padx=30,
                    pady=4
                )


            tk.Label(
                info,
                text=disasters[name]["Warning_source"],
                font=("Arial", 9, "italic"),
                wraplength=700,
                justify="left"
            ).pack(
                fill="x",
                padx=25,
                pady=(2, 15)
            )


        # =========================
        # BEFORE / DURING / AFTER
        # =========================

        for part in ["Before", "During", "After"]:

            tk.Label(
                info,
                text=part + " a " + name,
                font=("Arial", 15, "bold")
            ).pack(
                anchor="w",
                padx=25,
                pady=(10, 5)
            )


            for text in disasters[name][part]:

                tk.Label(
                    info,
                    text="• " + text,
                    font=("Arial", 11),
                    wraplength=700,
                    justify="left",
                    anchor="w"
                ).pack(
                    fill="x",
                    padx=30,
                    pady=4
                )


            tk.Label(
                info,
                text=disasters[name][part + "_source"],
                font=("Arial", 9, "italic"),
                wraplength=700,
                justify="left"
            ).pack(
                fill="x",
                padx=25,
                pady=(2, 10)
            )


    else:

        tk.Label(
            info,
            text="Select a disaster above to view its information.",
            font=("Arial", 12)
        ).pack(
            pady=40
        )


    # =========================
    # MOUSE SCROLL
    # =========================

    def disaster_mouse_scroll(event):

        canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )


    canvas.bind(
        "<MouseWheel>",
        disaster_mouse_scroll
    )


# =========================
# START
# =========================

show_home()

window.mainloop()
