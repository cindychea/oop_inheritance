class System:

    all_bodies = []

    def __init__(self):
        self.bodies = []

    def add(self, new_body):
        if new_body in self.bodies:        
                print("This body already exists")
        else:
            self.bodies.append(new_body)
            System.all_bodies.append(new_body)
    
    def total_mass(self):
        total_mass = 0
        for body in self.bodies:
            total_mass += body.mass 
        return total_mass

    @classmethod
    def galactic_mass(cls):
        galactic_mass = 0
        for body in cls.all_bodies:
            galactic_mass += body.mass 
        return galactic_mass
    
class Body: 

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __repr__(self):
        return self.name

    
    @classmethod
    def all(cls, bodies):
        select_list = []
        for body in bodies:
            if isinstance(body, cls):
                select_list.append(body)
        return select_list

class Planet(Body):
    
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

class Star(Body):
    
    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

class Moon(Body):
    
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet

solarsystem = System()
alphacentauri = System()

sun = Star('Sun', 1.989, 'G-type')
northstar = Star('North Star', 1.989, 'G-type')
earth = Planet('Earth', 5.972, 23, 365)
moon = Moon("Earth's Moon", 7.35, 27, earth)
sun1 = Star('Alpha Sun', 1.989, 'G-type')
planet1 = Planet('Pluto', 5.972, 23, 365)
moon1 = Moon("Alpha's Moon", 7.35, 27, planet1)

solarsystem.add(sun)
solarsystem.add(northstar)
solarsystem.add(earth)
solarsystem.add(moon)
solarsystem.add(moon)

print(solarsystem.total_mass())

alphacentauri.add(sun1)
alphacentauri.add(planet1)
alphacentauri.add(moon1)

print(solarsystem.bodies)
print(alphacentauri.bodies)
print(System.all_bodies)

print(System.galactic_mass())

print(Star.all(solarsystem.bodies))