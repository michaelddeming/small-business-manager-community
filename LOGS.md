# Small Business Manager Community Build Logs

1. 05/15/2025 - Merged dev into main.
    - Added auto db file creation for user OS detection in local files.
        - Removing the need for a user to manually input PATH of db file into source code.
    - Fixed a major issue, issue#001, aux.py (auxiliary functions) renamed to funcs.py to avoid Windows OS file name collision.

    - Signed: Michael Deming 05/15/2025

2. XX/XX/2025 - Proposed dev changes (pending merge).
   - Switched to absolute imports for long-term maintainability and best practices.
     - Added `__init__.py` to folders that have functions that need to be exported.
   - Changed `app.py` to `sbm.py` to avoid ambiguity with `app` folder.
   - SBM needs to run as a module now instead of a script.
     - `python -m app.sbm` command must be run from the working directory of `small-business-manager-community` or the folder that contains the `app` folder instead of `python app.py`.
     - 🛠️ Note: This may require the user to update how they launch the app.
   - Small grammar fixes recommended by PyCharm while keeping the original meaning.

   - Signed: Aurorasyr (Sean Scott) 05/19/2025