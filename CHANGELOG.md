# Changelog

All notable changes to this project are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow the design revision (`v<rev>.<minor>.<patch>`), tagged in git.

Day-by-day history (purchases, fabrication sessions, measurements) lives in [`docs/PROJECT_LOG.md`](docs/PROJECT_LOG.md).

## [Unreleased]

### Added
- `docs/estado.md` (current state, next steps, open risks) and this changelog; changes go through pull requests (#6).
- Electronics: ADS1256 multiplexed-throughput budget with a summing-junction fallback, power-path and logic-level checks (#5).
- S1 power bench passed: 5.0 V bus in battery and USB modes, no load (#1).

### Changed
- On/off button moved to the battery side of the MT3608 (cuts the boost input), so the pack is not drained while off (#1, #10).
- README "Strategy" section reduced to a one-line "About" (#6).

### Fixed
- Electronics pinout rewritten for the ESP32-S3-DevKitC-1 N16R8; the previous table was for the classic ESP32 (#5).
- MT3608 setup note: on the HW-045 module counterclockwise *raises* the output; the old "20 turns counterclockwise to start low" was inverted (#1).
- Battery connection: the TP4056 board has pads only, so the pack is soldered to B+/B−; no JST-PH adapter (#1).

## [3.1.0-rc1] — 2026-06-10

Mechanical assembly complete (as-built); awaiting first calibration. Supersedes 3.0.0-rc1, which will never be promoted.

### Changed
- Structural tube: 1020 carbon steel 35×35×2 mm → stainless 304 35×35×1.5 mm, 2× 500 mm.
- Shims: 1.5 mm nominal → **2 mm final** (empirical box-section measurement, 2026-05-26).
- Stack height as-built: 45.35 mm; M10×60 thread engagement re-verified ≥ 1×D.
- Surface prep as-built: P24 + acetone; epoxy 4× 23 g in two sessions.
- Feet zinc-plated; rubber pads glued.

### Known limitations
- Assembled without a torque wrench (20–25 N·m not instrumentally verified).

## [3.0.0-rc1] — 2026-05-09

Design complete (fastening redesign), not physically validated.

### Changed
- Fastening: M10×60 DIN 7991 stainless 304 A2-70 + Parlock all-metal locknut + DIN 125 washer (was M10×50 class 8.8 + plain nut).
- Shims: 8 stainless 304 in mirror configuration, 1.5 mm nominal (was 4, top only).
- Plates: perimeter chamfer added.
- Torque target: 20–25 N·m (was 50–60 N·m).

## [2.0.0] — 2026-05-08

Snapshot of the Rev 2.0 design before the fastening redesign.

### Changed
- Plates: Al 5052-F (top 6.35 mm, bottom 3 mm), was Al 6061-T6.
- Box-section reinforcement with 1020 carbon steel tubes 35×35×2 mm (deflection ~21 mm → < 0.2 mm).
- Fastening: M10×50 DIN 7991 class 8.8; 4 shims (top only), 2 mm.

[Unreleased]: https://github.com/Nova-O2/open-force-plate/compare/v3.1.0-rc1...HEAD
[3.1.0-rc1]: https://github.com/Nova-O2/open-force-plate/compare/v3.0.0-rc1...v3.1.0-rc1
[3.0.0-rc1]: https://github.com/Nova-O2/open-force-plate/compare/v2.0.0...v3.0.0-rc1
[2.0.0]: https://github.com/Nova-O2/open-force-plate/releases/tag/v2.0.0
