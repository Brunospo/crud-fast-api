import sys
sys.path.append('../')

import pytest
from models.postgresql.settings.connection import db_connection_handler

#teste de integração
@pytest.mark.skip(reason='integracao com o banco')
def test_connection_db():
    engine = db_connection_handler.get_engine()
    assert engine is None
    
    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
