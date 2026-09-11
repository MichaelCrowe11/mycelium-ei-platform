# mycelium-ei-platform

Mycelium EI is a handful of Python scripts that score fungal strains against temperature and pH readings and check a license key before a simulation stub runs.

## Status

archived

Development stopped on 2025-01-18 (last content commit 0a6dee4; a merge commit followed on 2025-03-02). The code is kept for reference. Nothing in the repository runs end to end from a command it provides. Tried on 2026-09-10:

- `pytest` stops during collection with two errors: `tests/test_licensing.py` imports `cryptography`, which `requirements.txt` does not list, and `test_openai.py` calls the pre-1.0 OpenAI interface, which raises `APIRemovedInV1` under the `openai>=1.0.0` that `requirements.txt` requires.
- `python -c "import dashboard"` fails with `No module named 'dash'`; `dash` and `plotly` are not in `requirements.txt`.
- `run_simulation.py`, `app/`, `data/fungal_database.json` and `visualizations/`, all named in the previous README, do not exist.
- The homepage `mycelium-ei.io`, the API host `api.mycelium-ei.io` and the contact domain `mycelium-ei.com` have no DNS records.

## Install and first run

Not maintained. No supported install path.

What I did run on 2026-09-10 with Python 3.13.14 (uv for the virtual environment):

```
git clone https://github.com/MichaelCrowe11/mycelium-ei-platform
cd mycelium-ei-platform
uv venv --python 3.13 .venv
VIRTUAL_ENV=.venv uv pip install -r requirements.txt
.venv/bin/python -m pytest -q
```

`pytest` output ends with:

```
ERROR test_openai.py - openai.lib._old_api.APIRemovedInV1:
ERROR tests/test_licensing.py
!!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!
2 errors in 1.42s
```

The one function that works when imported is `prioritize_strains` in `priority_logic.py`. Called with a two-strain list and `{"temperature": 20, "pH": 6.5, "goals": ["restoration"]}` it returned `[{'strain': 'Pleurotus ostreatus', 'score': 4}]`.

Not run: `dashboard.py` (missing dependencies), `core/simulation.py` (needs a license file that nothing in the repository creates), `test_openai.py` (needs a live OpenAI key and fails at import anyway).

## What runs today

Nothing is maintained. `priority_logic.prioritize_strains` and `strain_prioritizer.StrainPrioritizer` are plain scoring loops over a list of dictionaries and can be imported.

## Limits

- There is no fungal database, no weather model, no REST API, no drone control and no simulation in this repository. `API.md` describes endpoints that were never implemented here. `core/simulation.py` prints one line after a license check.
- `Updated_Mycelium_EI_Simulation_Results.csv` has five rows. No code in the repository produces it.
- The licensing tiers, role-based access control and encryption described in the previous README are not in the code. `core/licensing.py` wraps a JSON file with Fernet and nothing else. `config/license_keys.json` is `{}`.
- `LICENSE_SECRET_KEY` falls back to the placeholder `your_generated_key_here` in `config/settings.py`.
- A `.env` file is committed at the repository root. Do not reuse anything in it.
- `test_openai.py` and `clipboard*.txt` are scratch files for calling OpenAI, not part of any product.

## License and contact

Proprietary. See `LICENSE`: use only with written permission from the owner; no modification, distribution or resale. The contact addresses in `LICENSE` and the previous README point at domains that no longer resolve.

Contact: michael@crowelogic.com
