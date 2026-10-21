import pytest
from main_program import Start,Process
@pytest.fixture
def test_masuk():
    return (
       Start("asja@gmail.com","olllllmmm","13:13 17 saturday 2026")
    )

def test_ada(test_masuk):
   nama =Process()
   nama.tambah(test_masuk)
   assert len(nama.data_base) == 9
   assert len(nama.data_base) == 9
  
  