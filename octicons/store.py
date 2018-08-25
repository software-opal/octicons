import warnings

from .octicons import OcticonStore

try:
    default_store = OcticonStore.from_file(None)
except Exception as e:
    default_store = None
    warnings.warn("Failed to load Octicons store.", source=e)
