from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")


# wrap logical connectives around the sentences that serve as arguments to these functions

sentence = And(rain, hagrid)

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)


print(sentence.formula())
print(model_check(knowledge, rain))
