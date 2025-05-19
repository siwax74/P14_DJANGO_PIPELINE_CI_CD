def test_dummy():
    assert 1

def test_500(request):
    raise Exception("Erreur volontaire")
