# Alunos: Dymas de Sousa Cunha e Vinicius Oliveira do Nascimento

class Tickets():
    def __init__(self, tickets, attendees, numbers):
        self.tickets = tickets
        self.attendees = attendees
        self.numbers = numbers

    def fakefinder(self):
        originals, fakes = list(), list()
        for element in self.numbers:
            if element in originals:
                fakes.append(element)
            else:
                originals.append(element)
        return len(list(set(fakes)))

    def __str__(self):
        return f'{self.tickets} {self.attendees} {self.numbers}'

def main():
    while True:
        rawinput = list(map(int, (input().split())))

        if (rawinput[0] == 0) or (rawinput[0] > 10000):
            return False

        if (rawinput[1] < 1) or (rawinput[1] > 20000):
            return False

        tickets, attendees = rawinput[0], rawinput[1]
        numbers = list(map(int, (input().split())))

        if (len(numbers) < 1) or (len(numbers) > attendees):
            return False

        party = Tickets(tickets, attendees, numbers)
        print(party.fakefinder())

if __name__ == "__main__":
    main()