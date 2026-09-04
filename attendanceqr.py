import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import qrcode
import cv2
import os
from datetime import datetime


# =========================
# DATABASE
# =========================

DB_NAME = "attendance.db"
QR_FOLDER = "qr_codes"

os.makedirs(QR_FOLDER, exist_ok=True)


def connect_db():
    return sqlite3.connect(DB_NAME)


def initialize_database():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            event TEXT NOT NULL,
            qr_code TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            event TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            UNIQUE(participant_id, date),
            FOREIGN KEY(participant_id) REFERENCES participants(id)
        )
    """)

    conn.commit()
    conn.close()


# =========================
# MAIN APPLICATION
# =========================

class AttendanceSystem:

    def __init__(self, root):
        self.root = root

        self.root.title("AttendEase - QR Attendance System")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

        self.bg_color = "#f4f7fb"
        self.blue = "#1565C0"
        self.dark_blue = "#0D47A1"
        self.red = "#D32F2F"
        self.white = "#FFFFFF"
        self.gray = "#555555"

        self.root.configure(bg=self.bg_color)

        initialize_database()

        self.create_header()
        self.create_main_interface()

    # =========================
    # HEADER
    # =========================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg=self.blue,
            height=80
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="AttendEase",
            font=("Arial", 25, "bold"),
            bg=self.blue,
            fg=self.white
        )

        title.pack(side="left", padx=30)

        subtitle = tk.Label(
            header,
            text="QR Code Attendance System",
            font=("Arial", 12),
            bg=self.blue,
            fg=self.white
        )

        subtitle.pack(side="left")

    # =========================
    # MAIN INTERFACE
    # =========================

    def create_main_interface(self):

        main = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        main.pack(fill="both", expand=True, padx=25, pady=25)

        # LEFT SIDE
        left_frame = tk.Frame(
            main,
            bg=self.white,
            width=450
        )

        left_frame.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        left_frame.pack_propagate(False)

        tk.Label(
            left_frame,
            text="Participant Registration",
            font=("Arial", 18, "bold"),
            bg=self.white,
            fg=self.dark_blue
        ).pack(pady=(25, 20))

        # Name
        tk.Label(
            left_frame,
            text="Full Name",
            font=("Arial", 11, "bold"),
            bg=self.white
        ).pack(anchor="w", padx=30)

        self.name_entry = tk.Entry(
            left_frame,
            font=("Arial", 12),
            width=38
        )

        self.name_entry.pack(
            padx=30,
            pady=(5, 15),
            ipady=6
        )

        # Email
        tk.Label(
            left_frame,
            text="Email",
            font=("Arial", 11, "bold"),
            bg=self.white
        ).pack(anchor="w", padx=30)

        self.email_entry = tk.Entry(
            left_frame,
            font=("Arial", 12),
            width=38
        )

        self.email_entry.pack(
            padx=30,
            pady=(5, 15),
            ipady=6
        )

        # Event
        tk.Label(
            left_frame,
            text="Event",
            font=("Arial", 11, "bold"),
            bg=self.white
        ).pack(anchor="w", padx=30)

        self.event_entry = tk.Entry(
            left_frame,
            font=("Arial", 12),
            width=38
        )

        self.event_entry.pack(
            padx=30,
            pady=(5, 20),
            ipady=6
        )

        # Register button
        register_button = tk.Button(
            left_frame,
            text="GENERATE QR CODE",
            font=("Arial", 12, "bold"),
            bg=self.blue,
            fg=self.white,
            activebackground=self.dark_blue,
            activeforeground=self.white,
            relief="flat",
            cursor="hand2",
            command=self.register_participant
        )

        register_button.pack(
            padx=30,
            pady=10,
            fill="x",
            ipady=8
        )

        # Scanner button
        scanner_button = tk.Button(
            left_frame,
            text="OPEN ADMIN SCANNER",
            font=("Arial", 12, "bold"),
            bg=self.red,
            fg=self.white,
            activebackground="#B71C1C",
            activeforeground=self.white,
            relief="flat",
            cursor="hand2",
            command=self.scan_qr
        )

        scanner_button.pack(
            padx=30,
            pady=10,
            fill="x",
            ipady=8
        )

        # Attendance button
        attendance_button = tk.Button(
            left_frame,
            text="VIEW ATTENDANCE",
            font=("Arial", 12, "bold"),
            bg="#333333",
            fg=self.white,
            relief="flat",
            cursor="hand2",
            command=self.show_attendance
        )

        attendance_button.pack(
            padx=30,
            pady=10,
            fill="x",
            ipady=8
        )

        # RIGHT SIDE
        right_frame = tk.Frame(
            main,
            bg=self.white
        )

        right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        tk.Label(
            right_frame,
            text="How It Works",
            font=("Arial", 20, "bold"),
            bg=self.white,
            fg=self.dark_blue
        ).pack(pady=(30, 20))

        steps = [
            ("1", "Register Participant"),
            ("2", "Generate Unique QR Code"),
            ("3", "Participant Receives QR Code"),
            ("4", "Admin Scans QR Code"),
            ("5", "Attendance Is Recorded")
        ]

        for number, text in steps:

            step_frame = tk.Frame(
                right_frame,
                bg=self.white
            )

            step_frame.pack(
                fill="x",
                padx=40,
                pady=10
            )

            number_label = tk.Label(
                step_frame,
                text=number,
                font=("Arial", 14, "bold"),
                bg=self.blue,
                fg=self.white,
                width=3,
                height=1
            )

            number_label.pack(
                side="left",
                padx=(0, 15)
            )

            tk.Label(
                step_frame,
                text=text,
                font=("Arial", 13),
                bg=self.white,
                fg="#333333"
            ).pack(
                side="left"
            )

        tk.Label(
            right_frame,
            text="Admin Scanner",
            font=("Arial", 16, "bold"),
            bg=self.white,
            fg=self.red
        ).pack(pady=(30, 10))

        tk.Label(
            right_frame,
            text="The admin scans the participant's QR code\n"
                 "to automatically record their attendance.",
            font=("Arial", 11),
            bg=self.white,
            fg=self.gray,
            justify="center"
        ).pack()

    # =========================
    # REGISTER PARTICIPANT
    # =========================

    def register_participant(self):

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        event = self.event_entry.get().strip()

        if not name or not email or not event:

            messagebox.showwarning(
                "Missing Information",
                "Please complete all fields."
            )

            return

        conn = connect_db()
        cursor = conn.cursor()

        # Check duplicate email + event
        cursor.execute("""
            SELECT id FROM participants
            WHERE email = ? AND event = ?
        """, (email, event))

        existing = cursor.fetchone()

        if existing:

            conn.close()

            messagebox.showerror(
                "Already Registered",
                "This participant is already registered for this event."
            )

            return

        # Insert temporary participant
        cursor.execute("""
            INSERT INTO participants
            (name, email, event, qr_code)
            VALUES (?, ?, ?, ?)
        """, (name, email, event, "TEMP"))

        participant_id = cursor.lastrowid

        qr_data = f"ATTEND-EASE|ID:{participant_id}|NAME:{name}|EVENT:{event}"

        # Update QR code
        cursor.execute("""
            UPDATE participants
            SET qr_code = ?
            WHERE id = ?
        """, (qr_data, participant_id))

        conn.commit()
        conn.close()

        # Generate QR
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(qr_data)
        qr.make(fit=True)

        qr_image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        filename = os.path.join(
            QR_FOLDER,
            f"participant_{participant_id}.png"
        )

        qr_image.save(filename)

        messagebox.showinfo(
            "Registration Successful",
            f"Participant registered successfully!\n\n"
            f"Name: {name}\n"
            f"Event: {event}\n\n"
            f"QR Code saved as:\n{filename}"
        )

        self.clear_form()

    # =========================
    # CLEAR FORM
    # =========================

    def clear_form(self):

        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.event_entry.delete(0, tk.END)

    # =========================
    # QR SCANNER
    # =========================

    def scan_qr(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():

            messagebox.showerror(
                "Camera Error",
                "Unable to access the camera."
            )

            return

        detector = cv2.QRCodeDetector()

        messagebox.showinfo(
            "Admin Scanner",
            "Scanner is ready.\n\n"
            "Show the participant's QR code to the camera.\n"
            "Press Q to stop scanning."
        )

        scanned = False

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            data, bbox, _ = detector.detectAndDecode(frame)

            if bbox is not None:

                bbox = bbox.astype(int)

                for i in range(len(bbox[0])):

                    point1 = tuple(bbox[0][i])
                    point2 = tuple(
                        bbox[0][(i + 1) % len(bbox[0])]
                    )

                    cv2.line(
                        frame,
                        point1,
                        point2,
                        (0, 255, 0),
                        3
                    )

            if data and not scanned:

                scanned = True

                self.process_attendance(data)

                cv2.putText(
                    frame,
                    "SCAN SUCCESSFUL",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    3
                )

            cv2.imshow(
                "AttendEase - Admin QR Scanner",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                break

            if scanned and key == ord("n"):

                scanned = False

        cap.release()
        cv2.destroyAllWindows()

    # =========================
    # PROCESS ATTENDANCE
    # =========================

    def process_attendance(self, qr_data):

        if not qr_data.startswith("ATTEND-EASE"):

            messagebox.showerror(
                "Invalid QR Code",
                "This QR code is not registered in AttendEase."
            )

            return

        try:

            parts = qr_data.split("|")

            participant_id = int(
                parts[1].split(":")[1]
            )

        except:

            messagebox.showerror(
                "Invalid QR Code",
                "Unable to read participant information."
            )

            return

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, event
            FROM participants
            WHERE id = ?
        """, (participant_id,))

        participant = cursor.fetchone()

        if not participant:

            conn.close()

            messagebox.showerror(
                "Not Registered",
                "Participant not found in the database."
            )

            return

        participant_id, name, event = participant

        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%I:%M:%S %p")

        # Check duplicate attendance
        cursor.execute("""
            SELECT id
            FROM attendance
            WHERE participant_id = ?
            AND date = ?
        """, (participant_id, current_date))

        existing = cursor.fetchone()

        if existing:

            conn.close()

            messagebox.showwarning(
                "Already Checked In",
                f"{name} is already marked present today."
            )

            return

        cursor.execute("""
            INSERT INTO attendance
            (
                participant_id,
                name,
                event,
                date,
                time
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            participant_id,
            name,
            event,
            current_date,
            current_time
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Attendance Recorded",
            f"ATTENDANCE SUCCESSFUL!\n\n"
            f"Name: {name}\n"
            f"Event: {event}\n"
            f"Date: {current_date}\n"
            f"Time: {current_time}"
        )

    # =========================
    # VIEW ATTENDANCE
    # =========================

    def show_attendance(self):

        window = tk.Toplevel(self.root)

        window.title("Attendance Records")
        window.geometry("850x500")

        window.configure(bg=self.bg_color)

        tk.Label(
            window,
            text="Attendance Records",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.dark_blue
        ).pack(pady=20)

        columns = (
            "ID",
            "Name",
            "Event",
            "Date",
            "Time"
        )

        table = ttk.Treeview(
            window,
            columns=columns,
            show="headings"
        )

        for column in columns:

            table.heading(
                column,
                text=column
            )

        table.column("ID", width=50)
        table.column("Name", width=200)
        table.column("Event", width=200)
        table.column("Date", width=120)
        table.column("Time", width=120)

        table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                participant_id,
                name,
                event,
                date,
                time
            FROM attendance
            ORDER BY id DESC
        """)

        records = cursor.fetchall()

        conn.close()

        for record in records:

            table.insert(
                "",
                tk.END,
                values=record
            )


# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":

    root = tk.Tk()

    app = AttendanceSystem(root)

    root.mainloop()