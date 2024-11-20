import tkinter as tk
from tkinter import messagebox
import time


class ZarobkiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("$MINUTNIK")
        
        # Obliczenia dla zarobków
        self.miesieczna_pensja = 9876.54 # Tu wprowadź swoją pensję
        self.liczba_godzin_miesiecznie = 160
        self.stawka_za_sekunde = self.miesieczna_pensja / (self.liczba_godzin_miesiecznie * 3600)
        
        self.start_time = None
        self.running = False
        self.zarobione = 0
        
        # Etykieta licznika
        self.licznik_label = tk.Label(self.root, text="0.00 zł", font=("Arial", 24))
        self.licznik_label.pack(pady=20)
        
        # Przycisk START
        self.start_button = tk.Button(self.root, text="START", command=self.start, font=("Arial", 14), bg="green", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Przycisk STOP
        self.stop_button = tk.Button(self.root, text="STOP", command=self.stop, font=("Arial", 14), bg="red", fg="white")
        self.stop_button.pack(side=tk.RIGHT, padx=20, pady=10)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_zarobki()

    def update_zarobki(self):
        if self.running:
            czas_pracy = time.time() - self.start_time
            self.zarobione = czas_pracy * self.stawka_za_sekunde
            self.licznik_label.config(text=f"{self.zarobione:.2f} zł")
            self.root.after(1000, self.update_zarobki)
    
    def stop(self):
        if self.running:
            self.running = False
            czas_pracy = time.time() - self.start_time
            zarobione = czas_pracy * self.stawka_za_sekunde
            sformatowany_czas = self.format_czas(czas_pracy)
            messagebox.showinfo(
                "Podsumowanie",
                f"Pracowałeś przez {sformatowany_czas}\nZarobiłeś w tym czasie {zarobione:.2f} zł"
            )
            self.licznik_label.config(text="0.00 zł")
            self.zarobione = 0
            self.start_time = None

    def format_czas(self, sekundy):
        godziny = int(sekundy // 3600)
        minuty = int((sekundy % 3600) // 60)
        sekundy = int(sekundy % 60)
        
        godziny_label = "godzina" if godziny == 1 else "godziny" if 2 <= godziny <= 4 else "godzin"
        minuty_label = "minuta" if minuty == 1 else "minuty" if 2 <= minuty <= 4 else "minut"
        sekundy_label = "sekunda" if sekundy == 1 else "sekundy" if 2 <= sekundy <= 4 else "sekund"
        
        return f"{godziny} {godziny_label} {minuty} {minuty_label} {sekundy} {sekundy_label}"


if __name__ == "__main__":
    root = tk.Tk()
    app = ZarobkiApp(root)
    root.mainloop()
