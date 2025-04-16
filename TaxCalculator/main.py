import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        # Initialize our window
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280x200")
        self.window.resizable(False, False)

        # Initialize Padding
        self.padding: dict = {"padx": 20, "pady": 10}

        # Income label and entry
        self.income_label = ctk.CTkLabel(self.window, text="Income:")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window, placeholder_text="60000")
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax label and entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text="Percent:")
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window, placeholder_text="30")
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        # Result label and entry
        self.result_label = ctk.CTkLabel(self.window, text="Tax:")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")
        self.result_entry.grid(row=2, column=1, **self.padding)

        # Calculate Button
        self.calculator_btn = ctk.CTkButton(self.window, text="Calculate", command=self._calculate_tax)
        self.calculator_btn.grid(row=3, column=1, **self.padding)

    def _update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def _calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self._update_result(f"{income * (tax_rate / 100):,.2f}")
        except ValueError:
            self._update_result("Invalid input")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    tc = TaxCalculator()
    tc.run()
