# Open Force Plate

[![License: CERN-OHL-S-2.0](https://img.shields.io/badge/Hardware-CERN--OHL--S--2.0-blue)](LICENSE-HARDWARE)
[![License: GPL v3](https://img.shields.io/badge/Software-GPL--v3-blue)](LICENSE-SOFTWARE)
[![Status: Hardware Phase](https://img.shields.io/badge/Status-Hardware%20Phase-yellow)]()

An open-source, single-axis (vertical) force plate for sport science. Measures ground reaction force (GRF) at **1000 Hz** with **24-bit** resolution, comparable to commercial platforms costing 12–40× more.

> **[🇧🇷 Leia em Português](#português)**

## Status

- **Status:** 🚧 **Rev 3.1-rc1** — inox 304 throughout, incl. structural tube (release candidate, awaiting physical validation)
- ✅ Mechanical components received: 4× turned foot pieces (Ø55 + base wall serrilhada) + 2× chamfered plates (AL Usinagem 2026-05-08, R$ 1.480)
- ✅ Hardware ordered: M10×60 DIN 7991 inox 304 + Parlock + arruela inox 304 (MercadoLivre 2026-05-08, R$ 136,19, frete grátis)
- ✅ Structural tube acquired: inox 304 35×35×1.5mm, 1 m bar (Real Fortaleza Hidráulica, Jacareí — 2026-05-18, R$ 103,67)
- ✅ Structural epoxy acquired: Araldite Profissional 90 min, 2× 23 g (Real Fortaleza Hidráulica — 2026-05-19, R$ 62,00)
- 🔄 **Pending:** cut tube into 2× 500mm → bond plates+tubes with structural epoxy (24 h cure) → measure box section height empirically → AL Usinagem quote for 8 stainless 304 mirror shims (1.5mm nominal — empirical) → ML hardware delivery → remaining consumables (P40–P60 sandpaper, isopropyl alcohol, bar clamps)
- ⏳ **Validation gate:** assembly of 4 corners + first calibration to promote `v3.1.0-rc1` → `v3.1.0` final
- **Updated:** 2026-05-19

### Engenharia
- **Sprint:** hardware MVP — Rev 3.1 inox 304 throughout + assembly
- **Version:** `v3.1.0-rc1` (release candidate)
- **Deploy:** N/A (hardware physical)

## Strategy

Força-plate é o **primeiro produto do pilar Tecnologia Nova O2** (casa de hardware open sport-tech BR). Strategy formal em:

- [`01-content/marketing/nova-o2/strategy/pilar_tecnologia.md`](../../../01-content/marketing/nova-o2/strategy/pilar_tecnologia.md) — visão pilar + sequenciamento produtos + roadmap captação 4 fases (PIPE → Embrapii → VC) + networking priorizado + armadilhas
- [`05-strategy/nova-o2/README.md`](../../../05-strategy/nova-o2/README.md) — índice de pointers strategy Nova O2

Próximas etapas estratégicas (cascade do pilar Tecnologia, OKRs Q2 2026 sub-pilar 2.T):

1. Rev 3.1 final + primeira calibração (em curso — KR 2.T.1)
2. Lab acadêmico parceiro pra paper validação concorrente vs força-plate comercial (Q3/26 — KR 2.T.2)
3. Primeiros 2-3 clientes em clube (Portuguesa, São José FC via Daniel) — Set-Dez 2026
4. Pacote comercial formal (preço, garantia, suporte, treinamento) — Out-Dez 2026

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
| Estimated cost | ~$770 USD / ~R$3,860 BRL (Rev 3.1) |

## Hardware Architecture

```
       ┌──────────────────────────────┐
       │  Top plate — Al 5052-F 6.35mm │  ← stepping surface
       ├══════════════════════════════┤
       ║  2× inox 304 square tubes    ║  ← box section reinforcement
       ║       35×35×1.5 mm           ║
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

The platform uses 4 shear-beam load cells (DYX-301, 500 kg each) mounted between two aluminum plates (5052-F alloy). A box-section reinforcement (2× stainless steel 304 square tubes, 35×35×1.5 mm) bonded with structural epoxy reduces deflection from 21 mm to ~0.15 mm at the critical drop-jump load (~0.21 mm at the extreme 7× body-weight worst case).

See [Structural Analysis](docs/STRUCTURAL_ANALYSIS.md) and [Component Specs](docs/COMPONENT_SPECS.md) for full engineering details.

## Applications

- Countermovement Jump (CMJ) — height, peak force, impulse
- Squat Jump (SJ)
- Drop Jump (DJ) — Reactive Strength Index (RSI)
- Rate of Force Development (RFD)
- Unilateral tests (asymmetry via alternation)
- Ground contact time

## Project Status

**Current phase:** Hardware — Rev 3.1 mechanical assembly

- ✅ Component selection and procurement
- ✅ Structural analysis recalculated (Rev 3.1) + fabrication drawings (Rev 3.0)
- ✅ Electronics received (ADC, MCU, power, connectors)
- ✅ Load cells received (4× DYX-301, 2026-04-23)
- ✅ Aluminum plates acquired (Casa dos Metais 2026-04-16) + machining received (AL Usinagem 2026-05-08, R$ 1,480: feet + plate finishing + perimeter chamfer)
- ✅ Fastening hardware ordered (Rev 3.0): M10×60 DIN 7991 inox 304 + Parlock + arruela 304 (MercadoLivre 2026-05-08, R$ 136,19)
- ✅ Structural tube acquired (Rev 3.1): inox 304 35×35×1.5mm (Real Fortaleza Hidráulica 2026-05-18, R$ 103,67)
- ✅ Structural epoxy acquired: Araldite Profissional 90 min, 2× 23 g (Real Fortaleza Hidráulica 2026-05-19, R$ 62,00)
- 🔄 Pending: epoxy bonding + box section measurement + 8 stainless 304 mirror shims (AL Usinagem quote) + remaining consumables
- 🔲 Firmware development
- 🔲 Software development
- 🔲 Scientific validation

## Cost Breakdown (Rev 3.1)

| Category | Cost (BRL) | Cost (USD) |
|----------|-----------|-----------|
| Imported electronics (AliExpress: cells + ADC + MCU + power) | ~R$1,300 | ~$260 |
| Battery replacement (ML 2026-04-04: 1S2P 5200mAh × 2) | ~R$55 | ~$11 |
| Aluminum plates (Casa dos Metais) | R$550 | ~$110 |
| AL Usinagem services (foot pieces + plate finishing) | R$1,480 | ~$295 |
| Inox 304 fastening (M10×60 + Parlock + washer, ML 2026-05-08) | R$136 | ~$27 |
| Structural tube (inox 304 35×35×1.5mm, Real Fortaleza 2026-05-18) | R$104 | ~$21 |
| Structural epoxy (Araldite Profissional 2× 23 g, Real Fortaleza 2026-05-19) | R$62 | ~$12 |
| Pending (remaining consumables + 8 stainless 304 shims) | ~R$185 | ~$37 |
| **Total Rev 3.1 (single platform)** | **~R$3,870** | **~$770** |

*Unit cost excludes tools and backup components. Cost increase vs Rev 2.0 estimate (~R$2,500) reflects the shift from "self-fab + carbon steel hardware" to "outsourced precision machining (AL Usinagem) + corrosion-resistant inox 304 fastening" — see [PROJECT_LOG 2026-05-08](docs/PROJECT_LOG.md) for rationale. The Rev 3.1 stainless tube came at R$104 (vs ~R$20 budgeted for carbon steel) — stainless premium + 1 m minimum bar length. See [Components Selected](docs/COMPONENTS_SELECTED.md) for the detailed breakdown.*

Commercial force plates range from R$30,000–R$100,000 ($6,000–$20,000 USD) — Rev 3.1 still 8–26× cheaper.

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
| Custo estimado | ~R$3.860 / ~$770 USD (Rev 3.1) |

## Arquitetura de Hardware

```
       ┌──────────────────────────────┐
       │  Top plate — Al 5052-F 6.35mm │  ← stepping surface
       ├══════════════════════════════┤
       ║  2× inox 304 square tubes    ║  ← box section reinforcement
       ║       35×35×1.5 mm           ║
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

A plataforma utiliza 4 células de carga do tipo shear beam (DYX-301, 500 kg cada) montadas entre duas chapas de alumínio (liga 5052-F). Um reforço em seção caixão (2× tubos quadrados de aço inox 304, 35×35×1,5 mm) colado com epóxi estrutural reduz a deflexão de 21 mm para ~0,15 mm na carga crítica de drop jump (~0,21 mm no pior caso extremo de 7× o peso corporal).

Veja a [Análise Estrutural](docs/STRUCTURAL_ANALYSIS.md) e as [Especificações de Componentes](docs/COMPONENT_SPECS.md) para detalhes completos de engenharia.

## Aplicações

- Countermovement Jump (CMJ) — altura, pico de força, impulso
- Squat Jump (SJ)
- Drop Jump (DJ) — Reactive Strength Index (RSI)
- Rate of Force Development (RFD)
- Testes unilaterais (assimetria via alternância)
- Tempo de contato no solo

## Status do Projeto

**Fase atual:** Hardware — montagem mecânica Rev 3.1

- ✅ Seleção e compra dos componentes
- ✅ Análise estrutural recalculada (Rev 3.1) + desenhos de fabricação (Rev 3.0)
- ✅ Eletrônica recebida (ADC, MCU, alimentação, conectores)
- ✅ Células de carga recebidas (4× DYX-301, 2026-04-23)
- ✅ Chapas de alumínio adquiridas (Casa dos Metais 2026-04-16) + usinagem recebida (AL Usinagem 2026-05-08, R$ 1.480: pezinhos + acabamento das chapas + chanfro perimetral)
- ✅ Hardware de fixação encomendado (Rev 3.0): M10×60 DIN 7991 inox 304 + Parlock + arruela 304 (MercadoLivre 2026-05-08, R$ 136,19)
- ✅ Tubo estrutural adquirido (Rev 3.1): inox 304 35×35×1,5mm (Real Fortaleza Hidráulica 2026-05-18, R$ 103,67)
- ✅ Epóxi estrutural adquirido: Araldite Profissional 90 min, 2× 23 g (Real Fortaleza Hidráulica 2026-05-19, R$ 62,00)
- 🔄 Pendente: colagem epóxi + medição da seção caixão + 8 juntas inox 304 espelho (orçamento AL Usinagem) + consumíveis restantes (lixa P40–P60, álcool isopropílico, grampos sargento)
- 🔲 Desenvolvimento de firmware
- 🔲 Desenvolvimento de software
- 🔲 Validação científica

## Custo Estimado (Rev 3.1)

| Categoria | Custo (BRL) | Custo (USD) |
|----------|-----------|-----------|
| Eletrônica importada (AliExpress: células + ADC + MCU + alimentação) | ~R$1.300 | ~$260 |
| Bateria substituta (ML 2026-04-04: 1S2P 5200mAh × 2) | ~R$55 | ~$11 |
| Chapas de alumínio (Casa dos Metais) | R$550 | ~$110 |
| Serviços AL Usinagem (pezinhos + acabamento das chapas) | R$1.480 | ~$295 |
| Fixação inox 304 (M10×60 + Parlock + arruela, ML 2026-05-08) | R$136 | ~$27 |
| Tubo estrutural (inox 304 35×35×1,5mm, Real Fortaleza 2026-05-18) | R$104 | ~$21 |
| Epóxi estrutural (Araldite Profissional 2× 23 g, Real Fortaleza 2026-05-19) | R$62 | ~$12 |
| Pendente (consumíveis restantes + 8 juntas inox 304) | ~R$185 | ~$37 |
| **Total Rev 3.1 (plataforma única)** | **~R$3.870** | **~$770** |

*Custo unitário exclui ferramentas e componentes de backup. Aumento vs estimativa Rev 2.0 (~R$2.500) reflete migração de "self-fab + fixação aço carbono" para "usinagem precisão (AL Usinagem) + fixação inox 304" — ver [PROJECT_LOG 2026-05-08](docs/PROJECT_LOG.md). O tubo inox da Rev 3.1 saiu R$104 (vs ~R$20 orçado para aço carbono) — prêmio do inox + barra mínima de 1 m. Veja [Componentes Selecionados](docs/COMPONENTS_SELECTED.md) para o detalhamento completo.*

Plataformas de força comerciais custam entre R$30.000 e R$100.000 ($6.000–$20.000 USD) — Rev 3.1 ainda 8–26× mais barata.

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
