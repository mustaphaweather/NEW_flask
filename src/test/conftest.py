import pytest

@pytest.fixture(name = "sum")
def sum(mocker):
	mocker.patch("fixtures_all.aid_fix.to_",return_value = 0)
	return 1 + fixtures_all.aid_fix.to_(1)


