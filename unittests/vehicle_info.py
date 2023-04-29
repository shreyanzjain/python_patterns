class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: int

    def __init__(self, brand: str, electric: bool, catalogue_price: int) -> None:
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self, tax_exemption_amount: int = 0) -> float:
        if tax_exemption_amount < 0:
            raise ValueError(
                f"Tax exemption amount must be a positive number, but recieved {tax_exemption_amount} instead.")
        tax_percent = 0.05
        if self.electric:
            tax_percent = 0.02
        if self.catalogue_price - tax_exemption_amount < 0:
            return 0
        return tax_percent * (self.catalogue_price - tax_exemption_amount)

    def can_lease(self, yearly_income) -> bool:
        if self.catalogue_price > 0.7 * yearly_income:
            return False
        else:
            return True
