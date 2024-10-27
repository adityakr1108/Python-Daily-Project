from turtle import Turtle

# Define the power-up abilities
power_up_abilities = ["extra_health", "extra_speed", "extra_life", "extra_points"]

def create_power_ups():
    """Create a list of turtles representing power-ups."""
    power_ups = []
    for ability in power_up_abilities:
        power_up = Turtle()
        power_up.shape("circle")
        power_up.penup()
        power_up.goto(random.randint(-200, 200), random.randint(-200, 200))
        power_up.ability = ability
        power_ups.append(power_up)
    return power_ups

def apply_ability(turtle, ability):
    """Apply the given ability to the turtle."""
    if ability == "extra_health":
        turtle.health += 1
        print("Extra health gained!")
    elif ability == "extra_speed":
        turtle.speed(turtle.speed() + 1)
        print("Extra speed gained!")
    elif ability == "extra_life":
        turtle.lives += 1
        print("Extra life gained!")
    elif ability == "extra_points":
        turtle.points += 10
        print("Extra points gained!")
