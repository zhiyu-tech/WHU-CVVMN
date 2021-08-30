from .basemodel import BaseModel
from .gcn import GCN
from .savn import SAVN
from .mjolnir_r import MJOLNIR_R
from .mjolnir_o import MJOLNIR_O
from .mjo_base import MJOBASE
from .mjo_savn import MJOSAVN


__all__ = ["BaseModel", "GCN", "SAVN", "MJOLNIR_O","MJOLNIR_R","MJOSAVN","MJOBASE"]

variables = locals()
