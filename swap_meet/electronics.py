from swap_meet.item import Item

class Electronics(Item):
    # category = "Electronics"

    def __init__(self, condition=0, type="Unknown", id=None, category="Electronics"):
        # super().__init__(category=Electronics.category, condition=condition, id=id)
        super().__init__(condition=condition, id=id)
        self.type = type
        self.category = category
    
    def get_category(self):
        return self.category

    def condition_description(self):
        return super().condition_description()

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
