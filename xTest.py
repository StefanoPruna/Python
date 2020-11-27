import X

def noInteger():
    assert 1 == X.calculatestrangevalue(1, 2)
    assert 2 == X.calculatestrangevalue(2, 2)
    assert not X.isValidPositiveIntegerInput(-1)
    assert not X.isValidPositiveIntegerInput("")

noInteger()