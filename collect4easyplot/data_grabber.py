import os
import pickle
from typing import Any

TMP_PATH = os.environ.get("TEMP")


def collect(data: Any, name: str):
    """ Dump data to file object in TEMP dir. Supposed to be used by EasyPlot """
    file_path = os.path.join(TMP_PATH, f"{name}.obj")
    file_obj = open(file_path, 'wb')
    pickle.dump(data, file_obj)
    file_obj.close()
    print(f"{name} collected successfully!")
