from swap_meet.item import Item
class Decor(Item):
    def __init__(self, category="Decor",condition=0,id=None, width=0, length=0):
        
        super().__init__(category, condition, id)
        self.width = width
        self.length = length
        
    def condition_description(self):
        return super().condition_description()
        
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
    def get_category(self):
        return f"{self.category}"   