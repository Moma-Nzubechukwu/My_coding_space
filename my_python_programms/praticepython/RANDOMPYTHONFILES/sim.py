import random
import math
import time
import uuid

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def scale(self, factor):
        return Vector2D(self.x * factor, self.y * factor)

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

class Entity:
    def __init__(self, name, position=None, velocity=None):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.position = position or Vector2D()
        self.velocity = velocity or Vector2D()
        self.age = 0

    def update(self):
        self.position = self.position.add(self.velocity)
        self.age += 1

    def __str__(self):
        return f"{self.name}#{self.id} at {self.position} age={self.age}"

class World:
    def __init__(self):
        self.entities = []
        self.time = 0

    def add_entity(self, entity):
        self.entities.append(entity)
        print(f"[WORLD] Added {entity}")

    def update(self):
        for entity in self.entities:
            entity.update()
        self.time += 1

    def remove_dead(self, max_age=50):
        before = len(self.entities)
        self.entities = [e for e in self.entities if e.age < max_age]
        removed = before - len(self.entities)
        if removed:
            print(f"[WORLD] Removed {removed} dead entities")

    def summary(self):
        print(f"[WORLD TIME: {self.time}] Total Entities: {len(self.entities)}")
        for entity in self.entities:
            print(f"  {entity}")

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
    return Entity(name, position, velocity)

def main():
    world = World()

    for _ in range(10):
        world.add_entity(random_entity())

    print("\n=== Starting simulation ===\n")

    for step in range(100):
        if step % 10 == 0:
            world.add_entity(random_entity())

        world.update()
        world.remove_dead()
        if step % 20 == 0:
            world.summary()

        time.sleep(0.05)

    print("\n=== Simulation complete ===\n")
    world.summary()

if __name__ == "__main__":
    main()
