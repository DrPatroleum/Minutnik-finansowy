# 💰 $MINUTNIK - Twój osobisty licznik zarobków w czasie rzeczywistym! 💻

**$MINUTNIK** to prosta aplikacja napisana w Pythonie, która pozwala w czasie rzeczywistym śledzić, ile zarobiłeś na podstawie swojej miesięcznej pensji i ilości godzin pracy. Dzięki temu możesz obserwować, jak rośnie Twój dochód w każdej sekundzie pracy!

## 🚀 Funkcje aplikacji:

- **Śledzenie zarobków w czasie rzeczywistym** – aplikacja przelicza Twoje zarobki na sekundy i pokazuje, ile zarobiłeś od rozpoczęcia pracy.
- **Podsumowanie po zakończeniu pracy** – po zakończeniu pracy otrzymasz komunikat z informacją o czasie pracy i zarobkach w tym okresie.
- **Personalizacja** – wystarczy, że w kodzie podasz swoją miesięczną pensję, a aplikacja zajmie się resztą!

## 🛠 Jak to działa?

1. Podaj swoją miesięczną pensję oraz liczbę godzin pracy miesięcznie w liniach:
   ```python
   self.miesieczna_pensja = 9876.54  # Tu wpisz swoją miesięczną pensję
   self.liczba_godzin_miesiecznie = 160  # Liczba godzin pracy w miesiącu
2. Uruchom aplikację.
3. Kliknij przycisk START, aby rozpocząć zliczanie.
4. Kliknij STOP, gdy chcesz zakończyć pracę i zobaczyć podsumowanie.

## 📋 Instrukcja instalacji:

1. Upewnij się, że masz zainstalowanego Pythona (wersja 3.6 lub nowsza).
2. Pobierz plik zarobki.py z tego repozytorium.
3. Uruchom aplikację w terminalu:
   ```python
   python zarobki.py

## 🖼 Wygląd aplikacji:

Aplikacja posiada prosty i czytelny interfejs graficzny oparty na bibliotece Tkinter:
- Duży licznik pokazujący zarobioną kwotę.
- Dwa przyciski:
  **START** – uruchamia zliczanie.
  **STOP** – zatrzymuje licznik i wyświetla podsumowanie.

## 👨‍💻 Technologie:

- **Python** – język programowania.
- **Tkinter** – biblioteka GUI do tworzenia interfejsu użytkownika.

## 📝 Przykładowe dane:

**Miesięczna pensja**: 9876,54 zł

**Liczba godzin pracy miesięcznie**: 160 godzin

Przykładowa symulacja:

*Po 2 godzinach pracy zarobiłeś 123,45 zł.*
