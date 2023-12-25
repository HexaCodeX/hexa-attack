import json
from src.constants.paths import PATH_PROGRAM
from src.utils.struct import struct

try:
    config = struct(
      json.loads(
        open(f"{ PATH_PROGRAM }/config.json", "r").read()
      )
    )
except Exception as err:
    raise Exception(f"invalid json at '~/config.json'")