# Contributing to Open Force Plate

Open Force Plate is an open-source force plate for sport science. Contributions of all kinds are welcome — code, hardware improvements, documentation, translations, and validation data. Thank you for helping make accurate force measurement accessible to everyone.

---

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Make your changes
4. Commit following our conventions (see below)
5. Push and open a Pull Request

---

## Areas for Contribution

- **Firmware** — ESP32-S3 code (PlatformIO/Arduino), ADS1256 driver, BLE communication
- **Software** — Python analysis app, real-time visualization, jump detection algorithms
- **Hardware** — Mechanical design improvements, new sensor configurations, PCB design
- **Validation** — Comparison data with commercial platforms, reliability studies
- **Translations** — Documentation in other languages
- **Documentation** — Guides, tutorials, assembly photos, diagrams

---

## Development Setup

```bash
# Clone the repository
git clone https://github.com/Nova-O2/open-force-plate.git

# CAD analysis scripts require Python 3.12+ with:
pip install matplotlib numpy
```

For firmware (coming soon): PlatformIO with ESP32-S3 support.

---

## Commit Conventions

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation changes
- `chore:` — Maintenance tasks
- `refactor:` — Code restructuring

Commit messages in English.

---

## Code Style

- **Python:** PEP 8, type hints on all function signatures
- **C/C++:** To be defined when firmware development starts

---

## Naming Conventions

| Scope | Convention | Example |
|-------|-----------|---------|
| Root governance files | UPPERCASE (OSS standard) | `README.md`, `CONTRIBUTING.md`, `LICENSE-*` |
| Documentation | UPPER_SNAKE_CASE | `DEVELOPMENT_PLAN.md`, `PROJECT_LOG.md` |
| Code (scripts, firmware, software) | snake_case | `structural_analysis.py` |
| Generated artifacts (PDFs, images) | snake_case, English | `fab_top_plate.pdf` |
| GitHub templates | snake_case (GitHub default) | `bug_report.md` |
| Directories | snake_case | `hardware/cad/` |

---

## Analysis Script Versioning

The `hardware/cad/` directory contains Python scripts that compute structural analysis, material comparisons, and fabrication drawings. These scripts may reference specific design revisions.

**Rules:**

1. **Scripts must declare their design revision** — each analysis script must include a comment at the top indicating which design revision it targets (e.g., Rev 1.0, Rev 2.0)
2. **When design parameters change** (materials, dimensions, load cases), existing scripts should be updated to match the current revision. If the old analysis is historically relevant, note the change in `docs/PROJECT_LOG.md`
3. **Calculated values in scripts must match documentation** — if a script computes a safety factor, deflection, or weight, the same value must appear in the corresponding `.md` doc. Cross-reference discrepancies are bugs
4. **The source of truth for current design parameters** is `docs/STRUCTURAL_ANALYSIS.md` and `docs/COMPONENT_SPECS.md`. Scripts derive from these, not the other way around

**Current revisions:**

| Revision | Materials | Top plate | Reinforcement |
|----------|-----------|-----------|---------------|
| Rev 1.0 (2026-04-01) | Al 6061-T6 | 6 mm | Aluminum tubes |
| Rev 2.0 (2026-04-06) | Al 5052-F | 6.35 mm (1/4 in) | 1020 carbon steel tubes 35×35×2 mm |

Scripts targeting Rev 1.0 are marked with a disclaimer comment. Updated Rev 2.0 scripts are planned.

---

## Reporting Issues

Use the provided issue templates. For hardware issues, include photos whenever possible. For firmware/software, include your environment details (OS, Python version, ESP32 variant).

---

## Code of Conduct

We are committed to providing a welcoming and respectful environment. Be constructive, be inclusive, and focus on the work. Harassment or discriminatory behavior will not be tolerated.
