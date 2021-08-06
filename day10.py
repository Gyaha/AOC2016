class Bot():
    def __init__(self, name, low, low_type, high, high_type) -> None:
        self.chips = []
        self.name = name
        self.low = low
        self.high = high
        self.low_type = low_type
        self.high_type = high_type

    def __repr__(self) -> str:
        return "bot#" + self.name


def bots_and_stuff(s: str):
    bots = {}
    inputs = []
    outputs = {}

    for l in s.splitlines():
        ll = l.split()
        if ll[0] == "bot":
            name, low, low_type, high, high_type = ll[1], ll[6], ll[5], ll[11], ll[10]
            bots[name] = Bot(name, low, low_type, high, high_type)
        else:
            chip, target = ll[1], ll[5]
            inputs.append((chip, target))

    for i in inputs:
        bots[i[1]].chips.append(i[0])

    while True:
        for bot in bots.values():
            if len(bot.chips) >= 2:
                if len(bot.chips) > 2:
                    print("ERR")
                if "61" in bot.chips and "17" in bot.chips:
                    return bot.name
                low, high = sorted(bot.chips, key=int)
                transfer_chip(bots, outputs, low, bot.low, bot.low_type)
                transfer_chip(bots, outputs, high, bot.high, bot.high_type)
                bot.chips.clear()


def bots_and_stuff_outputs(s: str):
    bots = {}
    inputs = []
    outputs = {}

    for l in s.splitlines():
        ll = l.split()
        if ll[0] == "bot":
            name, low, low_type, high, high_type = ll[1], ll[6], ll[5], ll[11], ll[10]
            bots[name] = Bot(name, low, low_type, high, high_type)
        else:
            chip, target = ll[1], ll[5]
            inputs.append((chip, target))

    for i in inputs:
        bots[i[1]].chips.append(i[0])

    run = True
    while run:
        run = False
        for bot in bots.values():
            if len(bot.chips) >= 2:
                run = True
                if len(bot.chips) > 2:
                    print("ERR")
                low, high = sorted(bot.chips, key=int)
                transfer_chip(bots, outputs, low, bot.low, bot.low_type)
                transfer_chip(bots, outputs, high, bot.high, bot.high_type)
                bot.chips.clear()

    return int(outputs["0"]) * int(outputs["1"]) * int(outputs["2"])


def transfer_chip(bots, outputs, chip, target, _type):
    if _type == "bot":
        bots[target].chips.append(chip)
    else:
        outputs[target] = chip


with open("input10") as f:
    d = f.read()
    print(bots_and_stuff(d))
    print(bots_and_stuff_outputs(d))
