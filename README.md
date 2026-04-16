# Open Force Plate

[![License: CERN-OHL-S-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--S--2.0-blue)](LICENSE-HARDWARE)
[![License: GPL v3](https://img.shields.io/badge/Software-GPL--v3-blue)](LICENSE-SOFTWARE)
[![Status: Hardware Phase](https://img.shields.io/badge/Status-Hardware%20Phase-yellow)]()

An open-source, single-axis (vertical) force plate for sport science. Measures ground reaction force (GRF) at **1000 Hz** with **24-bit** resolution, comparable to commercial platforms costing 12–40× more.

> **[🇧🇷 Leia em Português](#português)**

## Specifications

| Parameter | Value |
|-----------|-------|
| Axes | 1 (vertical — Fz) |
| Sampling rate | 1000 Hz |
| ADC resolution | 24 bits (ADS1256) |
| Force resolution | ~0.075–0.15 N |
| Maximum capacity | 2000 kg (4 × 500 kg) |
| Connectivity | USB-C + BLE (Bluetooth Low Energy) |
| Power | Rechargeable Li-ion battery + USB-C |
| Platform dimensions | 600 × 500 mm |
| Estimated weight | ~13 kg |
| Estimated cost | ~$500 USD / ~R$2,500 BRL |

## Hardware Architecture

```
       ┌──────────────────────────────┐
       │  Top plate — Al 5052-F 6.35mm │  ← stepping surface
       ├══════════════════════════════┤
       ║  2× steel 1020 square tubes  ║  ← box section reinforcement
       ║       35×35×2 mm             ║
       ├══════════════════════════════┤
       │  Bottom plate — Al 5052-F 3mm │
       └────┬────┬────────┬────┬─────┘
            │    │        │    │
       [4× DYX-301 load cells 500kg]  ← turned feet rest on floor
            │    │        │    │
       ═══════════════════════════  ← rigid flat floor
                 │
         [ADS1256 24-bit ADC]  ← 1000 Hz SPI
                 │
              [ESP32-S3]       ← processing + BLE + USB-C
                 │
          [Python/Web App]     ← real-time analysis
```

The platform uses 4 shear-beam load cells (DYX-301, 500 kg each) mounted between two aluminum plates (5052-F alloy). A box-section reinforcement (2× steel 1020 square tubes, 35×35×2 mm) bonded with structural epoxy reduces deflection from 21 mm to <0.2 mm under worst-case drop jump loads (7× body weight).

See [Structural Analysis](docs/STRUCTURAL_ANALYSIS.md) and [Component Specs](docs/COMPONENT_SPECS.md) for full engineering details.

## Applications

- Countermovement Jump (CMJ) — height, peak force, impulse
- Squat Jump (SJ)
- Drop Jump (DJ) — Reactive Strength Index (RSI)
- Rate of Force Development (RFD)
- Unilateral tests (asymmetry via alternation)
- Ground contact time

## Project Status

**Current phase:** Hardware — mechanical assembly

- ✅ Component selection and procurement
- ✅ Structural analysis and fabrication drawings
- ✅ Electronics received (ADC, MCU, power, connectors)
- ⏳ Load cells in transit
- ⏳ Aluminum plates acquired, awaiting assembly
- 🔲 Firmware development
- 🔲 Software development
- 🔲 Scientific validation

## Cost Breakdown

| Category | Cost (BRL) | Cost (USD) |
|----------|-----------|-----------|
| Imported components (AliExpress) | R$2,009 | ~$400 |
| Local components (aluminum, steel, hardware) | ~R$505 | ~$100 |
| **Total (single platform)** | **~R$2,500** | **~$500** |

Commercial force plates range from R$30,000–R$100,000 ($6,000–$20,000 USD).

See [Components Selected](docs/COMPONENTS_SELECTED.md) for the full bill of materials.

## Roadmap

| Phase | Scope | Status |
|-------|-------|--------|
| 1 | Hardware — mechanical and electronic assembly | 🔄 In progress |
| 2 | Firmware — ESP32 + ADS1256 @ 1000 Hz + USB-C/BLE | Planned |
| 3 | Software — Python app, real-time visualization, jump analysis | Planned |
| 4 | Validation — technical + scientific (N≥20, comparison with commercial platforms) | Planned |
| 5 | Dual plate — split into 2× 500×300 mm + 4 additional sensors | Future |
| 6 | Product — PCB, enclosure, mobile app | Future |

### GitHub Features Expansion

| Milestone | What gets added |
|-----------|----------------|
| Phase 1 complete | First release `v0.1-alpha`, assembly photos, assembly guide |
| Phase 2 | GitHub Actions (PlatformIO build + lint), `firmware/` directory |
| Phase 3 | GitHub Actions (pytest, mypy, ruff), `software/` directory |
| Phase 4 | Release `v1.0`, DOI via Zenodo, `CITATION.cff` for academic citation |
| Phase 6 | KiCad PCB files, 3D enclosure (STEP/STL) |

## Documentation

| Document | Description |
|----------|-------------|
| [Development Plan](docs/DEVELOPMENT_PLAN.md) | Detailed 6-phase roadmap with assembly checklists |
| [Component Specs](docs/COMPONENT_SPECS.md) | Technical specifications for all components |
| [Components Selected](docs/COMPONENTS_SELECTED.md) | Purchase registry and bill of materials |
| [Structural Analysis](docs/STRUCTURAL_ANALYSIS.md) | Engineering calculations — deflection, stress, safety factors |
| [Shopping List](docs/SHOPPING_LIST.md) | Local procurement guide with vendor categories |
| [Project Log](docs/PROJECT_LOG.md) | Chronological development history |

## Project Structure

```
open-force-plate/
├── hardware/
│   └── cad/            # Analysis scripts and fabrication drawings (PDF)
├── docs/               # Technical documentation
├── .github/            # Issue and PR templates
├── CONTRIBUTING.md     # How to contribute
├── LICENSE-HARDWARE    # CERN-OHL-S v2
└── LICENSE-SOFTWARE    # GPL v3
```

## Contributing

Contributions are welcome! Whether you're interested in firmware development, signal processing, mechanical improvements, validation data, or translations — see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

- **Hardware** (schematics, mechanical designs, CAD): [CERN Open Hardware Licence v2 — Strongly Reciprocal](LICENSE-HARDWARE)
- **Software** (firmware, analysis code): [GNU General Public License v3.0](LICENSE-SOFTWARE)

You're free to use, modify, and distribute this project — as long as derivative works remain open-source under the same licenses.

## References

- [can-can-group/forceplate-hardware-code](https://github.com/can-can-group/forceplate-hardware-code) — Reference open-source force plate project
- [force-plate-jump-analyses](https://github.com/stevenhirsch/force-plate-jump-analyses) — Python jump analysis
- [Pyomeca](https://github.com/pyomeca/pyomeca) — Biomechanics framework

---

<a id="português"></a>

# 🇧🇷 Português

> **[🇬🇧 Read in English](#open-force-plate)**

Uma plataforma de força uniaxial (vertical) open-source para ciência do esporte. Mede a força de reação do solo (GRF) a **1000 Hz** com resolução de **24 bits**, comparável a plataformas comerciais que custam 12–40× mais.

## Especificações

| Parâmetro | Valor |
|-----------|-------|
| Eixos | 1 (vertical — Fz) |
| Taxa de amostragem | 1000 Hz |
| Resolução ADC | 24 bits (ADS1256) |
| Resolução de força | ~0,075–0,15 N |
| Capacidade máxima | 2000 kg (4 × 500 kg) |
| Conectividade | USB-C + BLE (Bluetooth Low Energy) |
| Alimentação | Bateria Li-ion recarregável + USB-C |
| Dimensões da plataforma | 600 × 500 mm |
| Peso estimado | ~13 kg |
| Custo estimado | ~R$2.500 / ~$500 USD |

## Arquitetura de Hardware

```
       ┌──────────────────────────────┐
       │  Top plate — Al 5052-F 6.35mm │  ← stepping surface
       ├══════════════════════════════┤
       ║  2× steel 1020 square tubes  ║  ← box section reinforcement
       ║       35×35×2 mm             ║
       ├══════════════════════════════┤
       │  Bottom plate — Al 5052-F 3mm │
       └────┬────┬────────┬────┬─────┘
            │    │        │    │
       [4× DYX-301 load cells 500kg]  ← turned feet rest on floor
            │    │        │    │
       ═══════════════════════════  ← rigid flat floor
                 │
         [ADS1256 24-bit ADC]  ← 1000 Hz SPI
                 │
              [ESP32-S3]       ← processing + BLE + USB-C
                 │
          [Python/Web App]     ← real-time analysis
```

A plataforma utiliza 4 células de carga do tipo shear beam (DYX-301, 500 kg cada) montadas entre duas chapas de alumínio (liga 5052-F). Um reforço em seção caixão (2× tubos quadrados de aço 1020, 35×35×2 mm) colado com epóxi estrutural reduz a deflexão de 21 mm para menos de 0,2 mm sob cargas de pior caso em drop jump (7× o peso corporal).

Veja a [Análise Estrutural](docs/STRUCTURAL_ANALYSIS.md) e as [Especificações de Componentes](docs/COMPONENT_SPECS.md) para detalhes completos de engenharia.

## Aplicações

- Countermovement Jump (CMJ) — altura, pico de força, impulso
- Squat Jump (SJ)
- Drop Jump (DJ) — Reactive Strength Index (RSI)
- Rate of Force Development (RFD)
- Testes unilaterais (assimetria via alternância)
- Tempo de contato no solo

## Status do Projeto

**Fase atual:** Hardware — montagem mecânica

- ✅ Seleção e compra dos componentes
- ✅ Análise estrutural e desenhos de fabricação
- ✅ Eletrônica recebida (ADC, MCU, alimentação, conectores)
- ⏳ Células de carga em trânsito
- ⏳ Chapas de alumínio adquiridas, aguardando montagem
- 🔲 Desenvolvimento de firmware
- 🔲 Desenvolvimento de software
- 🔲 Validação científica

## Custo Estimado

| Categoria | Custo (BRL) | Custo (USD) |
|----------|-----------|-----------|
| Componentes importados (AliExpress) | R$2.009 | ~$400 |
| Componentes locais (alumínio, aço, fixadores) | ~R$505 | ~$100 |
| **Total (plataforma única)** | **~R$2.500** | **~$500** |

Plataformas de força comerciais custam entre R$30.000 e R$100.000 ($6.000–$20.000 USD).

Veja os [Componentes Selecionados](docs/COMPONENTS_SELECTED.md) para o bill of materials completo.

## Roadmap

| Fase | Escopo | Status |
|-------|-------|--------|
| 1 | Hardware — montagem mecânica e eletrônica | 🔄 Em andamento |
| 2 | Firmware — ESP32 + ADS1256 @ 1000 Hz + USB-C/BLE | Planejado |
| 3 | Software — app Python, visualização em tempo real, análise de saltos | Planejado |
| 4 | Validação — técnica + científica (N≥20, comparação com plataformas comerciais) | Planejado |
| 5 | Dual — dividir em 2× 500×300 mm + 4 sensores adicionais | Futuro |
| 6 | Produto — PCB, enclosure, app mobile | Futuro |

### Expansão de Funcionalidades no GitHub

| Marco | O que será adicionado |
|-----------|----------------|
| Fase 1 concluída | Primeiro release `v0.1-alpha`, fotos da montagem, guia de montagem |
| Fase 2 | GitHub Actions (build + lint PlatformIO), diretório `firmware/` |
| Fase 3 | GitHub Actions (pytest, mypy, ruff), diretório `software/` |
| Fase 4 | Release `v1.0`, DOI via Zenodo, `CITATION.cff` para citação acadêmica |
| Fase 6 | Arquivos KiCad PCB, enclosure 3D (STEP/STL) |

## Documentação

| Documento | Descrição |
|----------|-------------|
| [Plano de Desenvolvimento](docs/DEVELOPMENT_PLAN.md) | Roadmap detalhado em 6 fases com checklists de montagem |
| [Especificações de Componentes](docs/COMPONENT_SPECS.md) | Especificações técnicas de todos os componentes |
| [Componentes Selecionados](docs/COMPONENTS_SELECTED.md) | Registro de compras e bill of materials |
| [Análise Estrutural](docs/STRUCTURAL_ANALYSIS.md) | Cálculos de engenharia — deflexão, tensão, fatores de segurança |
| [Lista de Compras](docs/SHOPPING_LIST.md) | Guia de compras locais com categorias de fornecedores |
| [Diário do Projeto](docs/PROJECT_LOG.md) | Histórico cronológico de desenvolvimento |

## Estrutura do Projeto

```
open-force-plate/
├── hardware/
│   └── cad/            # Scripts de análise e desenhos de fabricação (PDF)
├── docs/               # Documentação técnica
├── .github/            # Templates de issues e PRs
├── CONTRIBUTING.md     # Como contribuir
├── LICENSE-HARDWARE    # CERN-OHL-S v2
└── LICENSE-SOFTWARE    # GPL v3
```

## Como Contribuir

Contribuições são bem-vindas! Se você tem interesse em desenvolvimento de firmware, processamento de sinais, melhorias mecânicas, dados de validação ou traduções — veja [CONTRIBUTING.md](CONTRIBUTING.md) para as diretrizes.

## Licença

- **Hardware** (esquemáticos, projetos mecânicos, CAD): [CERN Open Hardware Licence v2 — Strongly Reciprocal](LICENSE-HARDWARE)
- **Software** (firmware, código de análise): [GNU General Public License v3.0](LICENSE-SOFTWARE)

Você pode usar, modificar e distribuir este projeto livremente — desde que os trabalhos derivados permaneçam open-source sob as mesmas licenças.

## Referências

- [can-can-group/forceplate-hardware-code](https://github.com/can-can-group/forceplate-hardware-code) — Projeto open-source de referência para plataforma de força
- [force-plate-jump-analyses](https://github.com/stevenhirsch/force-plate-jump-analyses) — Análise de saltos em Python
- [Pyomeca](https://github.com/pyomeca/pyomeca) — Framework de biomecânica
