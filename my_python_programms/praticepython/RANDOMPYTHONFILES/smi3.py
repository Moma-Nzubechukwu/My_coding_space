import tkinter as tk
import random
import uuid
import math
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# VECTOR CLASS FOR MOVEMENT AND PHYSICS
class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def scale(self, factor):
        return Vector2D(self.x * factor, self.y * factor)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        length = self.length()
        if length != 0:
            return self.scale(1 / length)
        return self

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

# ENTITY CLASS TO REPRESENT INDIVIDUAL OBJECTS
class Entity:
    def __init__(self, name, position=None, velocity=None, health=100):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.position = position or Vector2D()
        self.velocity = velocity or Vector2D()
        self.health = health
        self.age = 0
        self.is_alive = True
        self.resources = 0
        self.energy = 100
        self.last_interaction = None

    def update(self):
        if self.is_alive:
            self.position = self.position.add(self.velocity)
            self.age += 1
            self.energy -= 1
            if self.energy <= 0:
                self.take_damage(5)
            self.last_interaction = None

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.is_alive = False
        logging.info(f"{self.name}#{self.id} has died!")

    def interact(self, other_entity):
        self.last_interaction = other_entity
        # Example interaction: damage and resource exchange
        self.take_damage(random.randint(5, 15))
        self.resources += random.randint(1, 10)
        other_entity.take_damage(random.randint(5, 15))
        other_entity.resources += random.randint(1, 10)

    def __str__(self):
        status = "Alive" if self.is_alive else "Dead"
        return f"{self.name}#{self.id} at {self.position} | Health: {self.health} | {status} | Energy: {self.energy} | Resources: {self.resources}"

# WORLD CLASS THAT MANAGES THE SIMULATION
class World:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.entities = []
        self.time = 0
        self.weather = "Clear"
        self.resource_spots = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        self.time += 1
        for entity in self.entities:
            if entity.is_alive:
                entity.update()
            else:
                self.entities.remove(entity)

    def collision_detection(self):
        for i, e1 in enumerate(self.entities):
            for e2 in self.entities[i+1:]:
                if e1.is_alive and e2.is_alive:
                    distance = e1.position.subtract(e2.position).length()
                    if distance < 2:  # Simple collision radius
                        self.handle_collision(e1, e2)

    def handle_collision(self, e1, e2):
        e1.take_damage(random.randint(5, 15))
        e2.take_damage(random.randint(5, 15))

    def interact_entities(self):
        for i, e1 in enumerate(self.entities):
            for e2 in self.entities[i+1:]:
                if e1.is_alive and e2.is_alive:
                    e1.interact(e2)

    def render(self, canvas):
        canvas.delete("all")
        for entity in self.entities:
            if entity.is_alive:
                canvas.create_oval(entity.position.x - 10, entity.position.y - 10, entity.position.x + 10, entity.position.y + 10, fill="blue")

# HELPER FUNCTIONS
def random_vector(max_mag=1.0):
    return Vector2D(
        random.uniform(-max_mag, max_mag),
        random.uniform(-max_mag, max_mag)
    )

def random_entity():
    names = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Omega']
    name = random.choice(names)
    position = random_vector(10)
    velocity = random_vector(1)
    health = random.randint(50, 150)
    return Entity(name, position, velocity, health)

# GUI APPLICATION CLASS
class SimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Entity Simulation")
        
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        
        self.world = World(width=800, height=600)

        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Simulation", command=self.stop_simulation)
        self.stop_button.pack()

        self.spawn_button = tk.Button(root, text="Spawn Entity", command=self.spawn_entity)
        self.spawn_button.pack()

        self.running = False

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.simulation_step()

    def stop_simulation(self):
        self.running = False

    def spawn_entity(self):
        entity = random_entity()
        self.world.add_entity(entity)

    def simulation_step(self):
        if self.running:
            self.world.update()
            self.world.collision_detection()
            self.world.interact_entities()
            self.world.render(self.canvas)
            self.world.spawn_resources()
            self.root.after(100, self.simulation_step)  # Update every 100ms

# MAIN FUNCTION
def main():
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
