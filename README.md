# Event Tree Analysis ✅

**Event Tree Analysis** is a small, dependency-light Python CLI to convert a CSV system description (components and their possible states) into an event tree representation and a list of all event paths. It was originally written by Umair Siddique and is intended as a minimal tool for teaching, prototyping, or integrating into larger safety analysis workflows.

---

## 🔧 Features

- Parse a CSV system description where each column is a component and each row lists a state for that component.
- Generate a Newick-like event tree and print an ASCII visualization (via `ete3`).
- Print all possible event paths (cartesian product of component states).
- Small, single-file CLI (`et_tool.py`) with no heavy framework requirements.

---

## 📦 Requirements

Install the runtime requirements (recommended to use a virtual environment):

```bash
pip install -r requirements.txt
```

Notes:
- `ete3` is used for building and rendering tree ASCII art.
- `pandas` is used for CSV parsing.

---

## 📝 CSV System Format

The CSV should have component names as the header row and each following row contains a state for each component. Example `system.csv`:

```csv
Sensor_1,Sensor_2
open,misaligned
short,low_voltage
stuck,noisy
```

---

## ▶️ Usage

```bash
python3 et_tool.py -s system.csv -o analysis.txt
```

This generates `analysis.txt` containing:
- A printed system description (table)
- ASCII event tree
- A numbered list of all possible event paths

---

## 🧪 Example

Given the `system.csv` above the output contains the system table, an ASCII event tree and the set of paths such as:

```
Path 1 = ('open', 'misaligned')
Path 2 = ('open', 'low_voltage')
...
```

---

## ✅ Next steps / Suggested improvements

Here are a few ways to revive & improve the project (good starting tasks):

1. Add unit tests for `get_system`, `make_tree`, and helper functions.
2. Add command-line validation and better error messages (missing file, malformed CSV).
3. Add optional JSON or DOT export of the event tree for integration with other tools.
4. Add probabilities for states and compute path probabilities & minimal cut sets.
5. Add a GitHub Actions CI workflow for tests and linting.

---

## 🤝 Contributing

Contributions are welcome. Please open issues for bugs or feature requests and submit a PR with tests and a short description.

---

## 📄 License

Add a `LICENSE` file to the project root. (If you want, I can add a permissive MIT license for you.)

---

If you'd like, I can also:
- Add a small unit test suite and CI config ✅
- Clean up `et_tool.py` (fix typos, add argument validation and logging) ✅
- Add an example script to generate visual output (PNG/SVG) via `ete3` (requires Graphviz) ✅

Would you like me to implement any of those next?
