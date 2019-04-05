from Car import Car
from Event import Event


def main():
    print("type speed / slow / stop / turn_right / turn_left")
    event = Event()
    car1 = Car(event)

    while event.get_command() != "stop":
        command = input('event: ')
        event.set_command(command)
        car1.act(event)


if __name__ == "__main__":
    main()
