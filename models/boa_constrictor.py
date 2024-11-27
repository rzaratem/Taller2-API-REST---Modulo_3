class BoaConstrictor:
    # Lista para almacenar todas las instancias de BoaConstrictor
    serpientes = []

    def __init__(self, id, nombre, edad, sonido, tipo="Boa Constrictor"):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.sonido = sonido
        self.tipo = tipo
        BoaConstrictor.serpientes.append(self)  # Agregar a la lista automáticamente

    @classmethod
    def obtener_todas(cls):
        """Devuelve todas las serpientes."""
        return cls.serpientes

    @classmethod
    def buscar_por_id(cls, id):
        """Busca una serpiente por su ID."""
        return next((s for s in cls.serpientes if s.id == id), None)

    @classmethod
    def agregar_serpiente(cls, nombre, edad, sonido):
        """Crea y agrega una nueva serpiente a la lista."""
        nueva_serpiente = cls(id=len(cls.serpientes) + 1, nombre=nombre, edad=edad, sonido=sonido)
        return nueva_serpiente


BoaConstrictor(1, "Kaa", 7, "Siseo")
BoaConstrictor(2, "Nagini", 5, "Silbido")
BoaConstrictor(3, "Python", 4, "Siseo suave")
BoaConstrictor(4, "Kaa2", 5, "Siseooo")