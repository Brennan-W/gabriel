from src.gabriel_server import local_engine
from src.gabriel_server.local_engine import cognitive_engine

my_engine =cognitive_engine

local_engine.run(engine_factory=lambda: my_engine, source_name='my_source',
                 input_queue_maxsize=60, port=9099, num_tokens=2)