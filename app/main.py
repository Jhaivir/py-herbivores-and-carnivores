class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{"
            + f"Name: {self.name}, "
            + f"Health: {self.health}, "
            + f"Hidden: {self.hidden}"
            + "}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
        for animal in range(len(Animal.alive)):
            if Animal.alive[animal].health <= 0:
                del Animal.alive[animal]
