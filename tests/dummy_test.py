import pandas as pd
from pathlib import Path
import pytest

def test_date_parsing():
    s = "2025-11-19 10:30:00 (UTC-4)"
    import re
    s_clean = re.sub(r"\s*\(UTC-4\)\s*$", "", s)
    dt = pd.to_datetime(s_clean, utc=True, errors='coerce')
    assert not pd.isna(dt)
