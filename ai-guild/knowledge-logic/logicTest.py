from logic import *

messi = Symbol("Messi")
jordan = Symbol("Jordan")
bolt = Symbol("Bolt")
characters = [messi, jordan, bolt]

soccer = Symbol("Soccer")
basketball = Symbol("Basketball")
running = Symbol("running")
sports = [soccer, basketball, running]

argentina = Symbol("Argentina")
usa = Symbol("USA")
jamaica = Symbol("Jamaica")
countries = [argentina, usa, jamaica]

symbols = characters + sports + countries

knowledge = And(
    Or(messi, jordan, bolt),
    Or(soccer, basketball, running),
    Or(argentina, usa, jamaica)
)


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(symbol)
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# adding knowledge -> process of inference, thereby increasing the knowledge base and eliminating possible solutions
knowledge.add(Not(messi))
knowledge.add(Or(
    Not(jordan), Not(soccer), Not(jamaica)
))

check_knowledge(knowledge)
