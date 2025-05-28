import random
import time
import math
import uuid
import logging

# Set up basic logging
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

    def update(self):
        if self.is_alive:
            self.position = self.position.add(self.velocity)
            self.age += 1

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.is_alive = False
        logging.info(f"{self.name}#{self.id} has died!")

    def __str__(self):
        status = "Alive" if self.is_alive else "Dead"
        return f"{self.name}#{self.id} at {self.position} | Health: {self.health} | {status}"

# WORLD CLASS THAT MANAGES THE SIMULATION
class World:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.entities = []
        self.time = 0
        self.weather = "Clear"

    def add_entity(self, entity):
        self.entities.append(entity)
        logging.info(f"[WORLD] Added {entity}")

    def update(self):
        self.time += 1
        for entity in self.entities:
            if entity.is_alive:
                entity.update()
            else:
                self.entities.remove(entity)
        self.update_weather()

    def remove_dead(self):
        dead_entities = [e for e in self.entities if not e.is_alive]
        for entity in dead_entities:
            self.entities.remove(entity)
        if dead_entities:
            logging.info(f"[WORLD] Removed {len(dead_entities)} dead entities.")

    def update_weather(self):
        if random.random() < 0.1:
            self.weather = random.choice(["Clear", "Rain", "Storm", "Fog"])
            logging.info(f"[WORLD] Weather changed to {self.weather}")

    def collision_detection(self):
        for i, e1 in enumerate(self.entities):
            for e2 in self.entities[i+1:]:
                if e1.is_alive and e2.is_alive:
                    distance = e1.position.subtract(e2.position).length()
                    if distance < 2:  # Simple collision radius
                        self.handle_collision(e1, e2)

    def handle_collision(self, e1, e2):
        logging.info(f"[COLLISION] {e1.name}#{e1.id} collided with {e2.name}#{e2.id}")
        e1.take_damage(random.randint(5, 15))
        e2.take_damage(random.randint(5, 15))

    def summary(self):
        logging.info(f"[WORLD TIME: {self.time}] Total Entities: {len(self.entities)}")
        for entity in self.entities:
            logging.info(f"  {entity}")
        logging.info(f"Weather: {self.weather}")

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

# MAIN SIMULATION LOOP
def main():
    world = World()

    # Generate initial entities
    for _ in range(20):
        world.add_entity(random_entity())

    logging.info("\n=== Starting simulation ===\n")

    # Run simulation for 100 steps
    for step in range(100):
        if step % 10 == 0:
            world.add_entity(random_entity())  # Randomly add new entities

        world.update()
        world.collision_detection()
        world.remove_dead()
        if step % 20 == 0:
            world.summary()

        time.sleep(0.1)

    logging.info("\n=== Simulation complete ===\n")
    world.summary()

if __name__ == "__main__":
    main()
