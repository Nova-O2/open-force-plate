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

## Reporting Issues

Use the provided issue templates. For hardware issues, include photos whenever possible. For firmware/software, include your environment details (OS, Python version, ESP32 variant).

---

## Code of Conduct

We are committed to providing a welcoming and respectful environment. Be constructive, be inclusive, and focus on the work. Harassment or discriminatory behavior will not be tolerated.
