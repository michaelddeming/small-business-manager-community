# Small Business Manager Community Build Logs

1. 05/15/2025 - Merged dev into main.
    - Added auto db file creation for user OS detection in local files.
        - Removing need for user to manaully input PATH of db file into source code.
    - Fixed major issue, issue#001, aux.py (auxillary functions) renamed to funcs.py to avoid Windows OS file name collision.

    - Signed: Michael Deming 05/15/2025
2. XX/XX/2025 -- Proposed dev changes (pending merge).
   - Switched to absolute imports for long-term maintainability.
     - Added `__init__.py` file to folders that have modules.
   - Changed `app.py` to `sbm.py` to avoid ambiguity with folder naming.
   - SBM needs to run as a module now instead of a script.
     - `python -m app.sbm` command must be run from the working directory of `small-business-manager-community` or the folder that contains the `app` folder instead of `python app.py`.
     - 🛠️ Note: This may require the user to update how they launch the app.
   - Signed: Aurorasyr (Sean Scott) 05/16/2025