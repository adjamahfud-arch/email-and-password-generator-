import pytest
from main_program import Start,To_hash,Hash_in

@pytest.fixture
def test_masuk():
    return (
       Start("asja@gmail.com","olllllmmm","13:13 17 saturday 2026")
    )

def test_ada(test_masuk):
   nama =To_hash()
   nama.tambah_hash(test_masuk)
   assert len(nama.data_hash) == 0


  