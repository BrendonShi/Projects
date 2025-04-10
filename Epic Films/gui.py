import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from save import movies
from functions import add_movie


def create_movie_card(parent, title, rating, our_rating, img_path, scale_factor):
    # Compute dynamic sizes based on scale_factor
    img_width = int(150 * scale_factor)
    img_height = int(220 * scale_factor)
    gradient_height = int(60 * scale_factor)

    # Load and resize the image
    img = Image.open(img_path).resize((img_width, img_height))
    img = ImageTk.PhotoImage(img)

    # Create a canvas to display the image
    canvas = tk.Canvas(parent, width=img_width, height=img_height, highlightthickness=0, bg="black")
    canvas.create_image(0, 0, anchor="nw", image=img)
    canvas.image = img  # Keep a reference to avoid garbage collection

    # Add a gradient overlay at the bottom
    gradient = Image.new("RGBA", (img_width, gradient_height), color=(0, 0, 0, 0))
    for i in range(gradient_height):
        opacity = int(i * (255 / gradient_height))
        for x in range(img_width):
            gradient.putpixel((x, i), (0, 0, 0, opacity))

    gradient_img = ImageTk.PhotoImage(gradient)
    canvas.create_image(0, img_height - gradient_height, anchor="nw", image=gradient_img)
    canvas.gradient_img = gradient_img  # Keep a reference to avoid garbage collection

    # Add overlay text with scaled font sizes
    title_font = ("Arial", int(12 * scale_factor), "bold")
    rating_font = ("Arial", int(10 * scale_factor))
    our_rating_font = ("Arial", int(9 * scale_factor))

    # Add title
    canvas.create_text(img_width // 2, img_height - gradient_height + int(20 * scale_factor),
                       text=title, fill="white", font=title_font, anchor="center")

    # Add rating
    canvas.create_text(img_width // 2, img_height - gradient_height + int(35 * scale_factor),
                       text=f"IMDb: {rating}", fill="white", font=rating_font, anchor="center")

    # Add genres
    canvas.create_text(img_width // 2, img_height - gradient_height + int(50 * scale_factor),
                       text="Custom Rating: " + str(our_rating), fill="white", font=our_rating_font, anchor="center")

    return canvas


def add_movie_button(parent, scale_factor):
    # Dynamic sizes based on scale_factor
    btn_width = int(150 * scale_factor)
    btn_height = int(220 * scale_factor)
    font_size = int(48 * scale_factor)

    # Create a frame for the add movie button styled like a card
    add_card = ttk.Frame(parent, style="Card.TFrame", width=btn_width, height=btn_height)
    add_card.grid_propagate(False)  # Prevent the frame from resizing to its content

    # Plus sign in the center
    plus_label = ttk.Label(add_card, text="+", font=("Arial", font_size, "bold"), foreground="white", background="#2e2e2e")
    plus_label.place(relx=0.5, rely=0.5, anchor="center")

    # Click functionality
    def on_click():
        open_movie_menu()

    add_card.bind("<Button-1>", lambda e: on_click())
    plus_label.bind("<Button-1>", lambda e: on_click())  # Ensure label also responds to clicks

    return add_card


def open_movie_menu():
    def validate_rate(P):
        if P == "":
            return True
        try:
            if P.count('.') <= 1:
                value = float(P)
                if 1.0 <= value <= 10.0:
                    if '.' in P:
                        if len(P.split('.')[1]) <= 1:
                            return True
                    else:
                        return True
        except ValueError:
            return False
        return False

    def submit_link_input():
        link = link_entry.get()
        r = our_rate_entry.get()
        if link:
            add_movie(link, r)
            new_menu.destroy()
        print("Link submitted:", link)

    # Create a new menu window
    new_menu = tk.Toplevel(root)
    new_menu.geometry(f"{window_width-1500}x{window_height-500}+{x}+{y}")
    new_menu.configure(bg="#101014")

    # Input for the IMDB link
    link_label = tk.Label(new_menu, text="Insert IMDB link:")
    link_label.configure(bg="#101014", foreground="white")
    link_label.pack(padx=10, pady=5)

    link_entry = tk.Entry(new_menu)
    link_entry.pack(padx=10, pady=5)

    # Input for the user's custom rating
    our_rate_label = tk.Label(new_menu, text="Type your rate:")
    our_rate_label.configure(bg="#101014", foreground="white")
    our_rate_label.pack(padx=10, pady=5)

    validate_command = new_menu.register(validate_rate)
    our_rate_entry = tk.Entry(new_menu, validate="key", validatecommand=(validate_command, '%P'))
    our_rate_entry.pack(padx=10, pady=5)

    # Submit and close buttons
    submit_button = tk.Button(new_menu, text="Submit", command=submit_link_input)
    submit_button.pack(padx=20, pady=20)

    close_button = tk.Button(new_menu, text="Close Menu", command=new_menu.destroy)
    close_button.pack(padx=10, pady=10)


def refresh_movies():
    # Clear the movies_frame
    for widget in movies_frame.winfo_children():
        widget.destroy()

    # Add the 'Add Movie' button
    add_movie_btn = add_movie_button(movies_frame, scale_factor)
    add_movie_btn.grid(row=0, column=0, padx=10, pady=10)

    # Add movie cards
    for i, (title, rating, our_rating, img_path) in enumerate(movies):
        row, col = divmod(i + 1, 5)  # Start from column 1
        card = create_movie_card(movies_frame, title, rating, our_rating, img_path, scale_factor)
        card.grid(row=row, column=col, padx=10, pady=10)

    # Schedule the next refresh
    root.after(2000, refresh_movies)  # Refresh every 2 seconds


# Root window
root = tk.Tk()
root.title("Movie Library")

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window dimensions relative to screen size
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#101014")

# Scaling factor based on screen size
base_width = 960
scale_factor = window_width / base_width

# Styles
style = ttk.Style()
style.configure("TButton", background="#2e2e2e", foreground="white", font=("Arial", int(12 * scale_factor)))
style.configure("TFrame", background="#101014")
style.configure("TLabel", background="#101014", foreground="white")
style.configure("Card.TFrame", background="#2e2e2e", relief="flat")
style.configure("Card.TLabel", background="#2e2e2e")
style.configure("CardTitle.TLabel", font=("Arial", int(12 * scale_factor), "bold"), foreground="white")
style.configure("CardRating.TLabel", font=("Arial", int(10 * scale_factor)), foreground="white")
style.configure("Cardour_rating.TLabel", font=("Arial", int(9 * scale_factor)), foreground="white")

# Left Panel
left_panel = ttk.Frame(root, style="TFrame", width=int(200 * scale_factor))
left_panel.pack(side="left", fill="y")

filters_label = ttk.Label(left_panel, text="Filters", style="TLabel")
filters_label.pack(pady=10, padx=10, anchor="w")

# Tags Section
tags_label = ttk.Label(left_panel, text="Tags", style="TLabel")
tags_label.pack(pady=10, padx=10, anchor="w")

# Example Tags
button1 = tk.Button(left_panel, text="Movie", bg="#101014", fg="white", relief="flat", activebackground="#2e2e2e")
button1.pack(pady=5, padx=15, anchor="w")

button2 = tk.Button(left_panel, text="Comedy", bg="#101014", fg="white", relief="flat", activebackground="#2e2e2e")
button2.pack(pady=5, padx=15, anchor="w")

button3 = tk.Button(left_panel, text="Drama", bg="#101014", fg="white", relief="flat", activebackground="#2e2e2e")
button3.pack(pady=5, padx=15, anchor="w")

# Main Library Area
library_frame = ttk.Frame(root, style="TFrame")
library_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

header_label = ttk.Label(library_frame, text="Labrary", style="TLabel", font=("Arial", int(18 * scale_factor), "bold"))
header_label.pack(pady=10, anchor="w")

# Scrollable area setup
canvas = tk.Canvas(library_frame, bg="#101014", highlightthickness=0)
scrollable_frame = ttk.Frame(canvas, style="TFrame")
scrollbar = ttk.Scrollbar(library_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the scrollbar and canvas
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Create a window within the canvas to hold the scrollable_frame
scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", configure_canvas)

def on_mousewheel(event):
    canvas.yview_scroll(-1 * int(event.delta / 120), "units")

root.bind_all("<MouseWheel>", on_mousewheel)  # For Windows and macOS
root.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # For Linux (scroll up)
root.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))  # For Linux (scroll down)

movies_frame = ttk.Frame(scrollable_frame, style="TFrame")
movies_frame.pack(fill="both", expand=True)

add_movie_btn = add_movie_button(movies_frame, scale_factor)
add_movie_btn.grid(row=0, column=0, padx=10, pady=10)

# Add movie cards
for i, (title, rating, our_rating, img_path) in enumerate(movies):
    row, col = divmod(i + 1, 5)  # Start from column 1
    card = create_movie_card(movies_frame, title, rating, our_rating, img_path, scale_factor)
    card.grid(row=row, column=col, padx=10, pady=10)

refresh_movies()

root.mainloop()