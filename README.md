# Getting Familiar

A visual novel for [NaNoRenO 2024](https://itch.io/jam/nanoreno-2024). Find it
on its [itch.io page](https://elizadev.itch.io/getting-familiar).

## Development
After cloning this repo, run the `tools/bootstrap.sh` script to initialize the
git configuration. This will prevent common errors when dealing with a
git+Ren'Py workflow.

When committing, sometimes git will yell at you to add new entries to
`.gitattributes` or run `tools/sanitize.sh`. In the former case, add an entry
matching the equivalent entries either in the "Text" or "Data" section,
depending on the file type in question. In the latter case, the script will
handle everything for you.
