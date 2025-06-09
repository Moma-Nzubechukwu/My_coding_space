import customtkinter as ctk
from PIL import Image

class BankingApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # --- Window Configuration ---
        self.title("Gemini Bank - Modern Banking")
        self.geometry("1100x700")
        self.resizable(False, False)

        # --- Appearance ---
        # Modes: "System" (standard), "Dark", "Light"
        ctk.set_appearance_mode("Dark")
        # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_default_color_theme("blue")

        # --- Grid Layout (2x1) ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Load Icons ---
        # Using Pillow to handle images for customtkinter
        # Note: Provide the correct path to your icon files.
        # For this example, we'll create simple placeholder icons if files aren't found.
        try:
            self.logo_image = ctk.CTkImage(Image.open("assets/logo.png"), size=(26, 26))
            self.dashboard_image = ctk.CTkImage(Image.open("assets/dashboard_icon.png"), size=(20, 20))
            self.transactions_image = ctk.CTkImage(Image.open("assets/transactions_icon.png"), size=(20, 20))
            self.accounts_image = ctk.CTkImage(Image.open("assets/accounts_icon.png"), size=(20, 20))
        except FileNotFoundError:
            # Create placeholder images if real icons are not found
            self.logo_image = self._create_placeholder_image((26, 26))
            self.dashboard_image = self._create_placeholder_image((20, 20))
            self.transactions_image = self._create_placeholder_image((20, 20))
            self.accounts_image = self._create_placeholder_image((20, 20))


        # --- Navigation Frame (Left Sidebar) ---
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # App Logo and Name
        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Gemini Bank", image=self.logo_image,
                                                      compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Navigation Buttons
        self.dashboard_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Dashboard", fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), image=self.dashboard_image, anchor="w",
                                                   command=self.dashboard_button_event)
        self.dashboard_button.grid(row=1, column=0, sticky="ew")

        self.transactions_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                     text="Transactions", fg_color="transparent", text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"), image=self.transactions_image, anchor="w",
                                                     command=self.transactions_button_event)
        self.transactions_button.grid(row=2, column=0, sticky="ew")

        self.accounts_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                 text="Accounts", fg_color="transparent", text_color=("gray10", "gray90"),
                                                 hover_color=("gray70", "gray30"), image=self.accounts_image, anchor="w",
                                                 command=self.accounts_button_event)
        self.accounts_button.grid(row=3, column=0, sticky="ew")

        # Appearance Mode Toggler
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                         command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        # --- Content Frames ---
        # Create a dictionary to hold the different content frames
        self.content_frames = {}
        for F in (DashboardFrame, TransactionsFrame, AccountsFrame):
            frame = F(self, self)
            self.content_frames[F.__name__] = frame
            # Place the frame on the grid, but it will be hidden initially
            frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
            frame.grid_remove() # Hide the frame

        # --- Select Default Frame ---
        self.select_frame_by_name("DashboardFrame")


    def _create_placeholder_image(self, size):
        """Creates a simple placeholder image."""
        return ctk.CTkImage(Image.new("RGB", size, "gray50"), size=size)

    def select_frame_by_name(self, name):
        """Shows the selected frame and updates the button states."""
        # Set button colors to indicate selection
        self.dashboard_button.configure(fg_color=("gray75", "gray25") if name == "DashboardFrame" else "transparent")
        self.transactions_button.configure(fg_color=("gray75", "gray25") if name == "TransactionsFrame" else "transparent")
        self.accounts_button.configure(fg_color=("gray75", "gray25") if name == "AccountsFrame" else "transparent")

        # Hide all other frames
        for frame_name, frame in self.content_frames.items():
            if frame_name != name:
                frame.grid_remove()

        # Show the selected frame
        self.content_frames[name].grid()


    def dashboard_button_event(self):
        self.select_frame_by_name("DashboardFrame")

    def transactions_button_event(self):
        self.select_frame_by_name("TransactionsFrame")

    def accounts_button_event(self):
        self.select_frame_by_name("AccountsFrame")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

class DashboardFrame(ctk.CTkFrame):
    """Frame for the main dashboard view."""
    def __init__(self, container, app_instance):
        super().__init__(container, corner_radius=10, fg_color="transparent")
        self.app = app_instance

        # --- Welcome Header ---
        welcome_label = ctk.CTkLabel(self, text="Welcome back, User!", font=ctk.CTkFont(size=24, weight="bold"))
        welcome_label.pack(anchor="w", pady=(0, 20))

        # --- Account Summary Cards ---
        summary_frame = ctk.CTkFrame(self, fg_color="transparent")
        summary_frame.pack(fill="x", expand=True, pady=10)

        # Checking Account Card
        checking_card = ctk.CTkFrame(summary_frame, corner_radius=10)
        checking_card.pack(side="left", fill="both", expand=True, padx=(0, 10))
        ctk.CTkLabel(checking_card, text="Checking Account", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(20, 5), padx=20)
        ctk.CTkLabel(checking_card, text="$12,345.67", font=ctk.CTkFont(size=30)).pack(pady=10, padx=20)
        ctk.CTkLabel(checking_card, text="**** **** **** 1234", text_color="gray50").pack(pady=(0, 20), padx=20)

        # Savings Account Card
        savings_card = ctk.CTkFrame(summary_frame, corner_radius=10)
        savings_card.pack(side="left", fill="both", expand=True, padx=(10, 0))
        ctk.CTkLabel(savings_card, text="Savings Account", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(20, 5), padx=20)
        ctk.CTkLabel(savings_card, text="$54,321.98", font=ctk.CTkFont(size=30)).pack(pady=10, padx=20)
        ctk.CTkLabel(savings_card, text="**** **** **** 5678", text_color="gray50").pack(pady=(0, 20), padx=20)

        # --- Recent Transactions ---
        transactions_frame = ctk.CTkFrame(self, corner_radius=10)
        transactions_frame.pack(fill="both", expand=True, pady=20)

        ctk.CTkLabel(transactions_frame, text="Recent Transactions", font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", padx=20, pady=(10, 5))

        # Mock transaction data
        transactions = [
            ("Spotify Subscription", "-$9.99", "Music"),
            ("Starbucks Coffee", "-$4.50", "Food"),
            ("Salary Deposit", "+$2,500.00", "Income"),
            ("Amazon Purchase", "-$128.32", "Shopping")
        ]

        for desc, amount, category in transactions:
            item_frame = ctk.CTkFrame(transactions_frame, fg_color="transparent")
            item_frame.pack(fill="x", padx=20, pady=5)
            ctk.CTkLabel(item_frame, text=desc).pack(side="left")
            ctk.CTkLabel(item_frame, text=amount, font=ctk.CTkFont(weight="bold"), text_color="green" if "+" in amount else "red").pack(side="right")


class TransactionsFrame(ctk.CTkFrame):
    """Frame for viewing all transactions."""
    def __init__(self, container, app_instance):
        super().__init__(container, corner_radius=10, fg_color="transparent")
        self.app = app_instance
        label = ctk.CTkLabel(self, text="Transactions Page", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)
        # Content for this page can be built out here
        # For example, a detailed list or table of all transactions.


class AccountsFrame(ctk.CTkFrame):
    """Frame for managing accounts."""
    def __init__(self, container, app_instance):
        super().__init__(container, corner_radius=10, fg_color="transparent")
        self.app = app_instance
        label = ctk.CTkLabel(self, text="Accounts Management", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)
        # Content for this page can be built out here
        # For example, options to open new accounts, view details, etc.


if __name__ == "__main__":
    app = BankingApp()
    app.mainloop()

