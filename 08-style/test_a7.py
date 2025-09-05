import a7

def test_champions_2_champs():
    ledger = [("Huff", 10),
              ("Griff", 50),
              ("RC", 40),
              ("Huff", 90),
              ("Sly", -10),
              ("Griff", 100),
              ("Griff", -60),
              ("RC", 80),
              ("Griff", 50)]

    assert a7.champions(ledger, 100, 2) == ['Huff', 'Griff']


def test_champions_6_champs():
    ledger = [("Huff", 10),
              ("Griff", 50),
              ("RC", 40),
              ("Huff", 90),
              ("Sly", -10),
              ("Griff", 100),
              ("Griff", -60),
              ("RC", 80),
              ("Griff", 50)]

    assert a7.champions(ledger, 100, 6) == ['Huff', 'Griff', 'RC']
