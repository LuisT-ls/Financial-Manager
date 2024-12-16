import tkinter as tk
from ui.gui_interface import FinancialManagerApp

def main():
    root = tk.Tk()
    app = FinancialManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()