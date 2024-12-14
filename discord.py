class Test_function():
    """тестовые фунции"""
    def __init__(self, chelovek, kakoi):
        """свойста человека"""
        self.chelovek = chelovek
        self.kakoi = kakoi
    
    def char(self):
        """описание человека"""
        print(self.chelovek, self.kakoi)