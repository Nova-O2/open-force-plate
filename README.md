---
title: Nova O2 Force Plate — Plataforma de Força Open-Source
sidebar_position: 1
---

# Nova O2 Force Plate

Plataforma de força uniaxial (vertical) open-source para ciência do esporte.

## Visão Geral

Dispositivo de baixo custo (~R$ 500-800) capaz de medir força de reação do solo (GRF) a **1000 Hz** com resolução de **24 bits**, validável contra padrão-ouro (Kistler/AMTI/Bertec).

## Especificações-Alvo

| Parâmetro | Valor |
|-----------|-------|
| Eixos | 1 (vertical — Fz) |
| Taxa de amostragem | 1000 Hz |
| Resolução ADC | 24 bits |
| Capacidade máxima | 800 kg (4 × 200 kg) |
| Comunicação | BLE (Bluetooth Low Energy) |
| Alimentação | Bateria LiPo recarregável |
| Dimensões plataforma | ~60 × 40 cm |
| Peso estimado | < 5 kg |

## Aplicações

- Countermovement Jump (CMJ) — altura, pico de força, impulso
- Squat Jump (SJ)
- Drop Jump (DJ) — RSI (Reactive Strength Index)
- Rate of Force Development (RFD)
- Testes unilaterais (assimetria via alternância)
- Tempo de contato no solo

## Arquitetura

```
[4× Células de Carga 200kg]
         │
    [ADS1256 24-bit ADC]  ← 1000 Hz SPI
         │
      [ESP32-S3]          ← processamento + BLE
         │
    [App Python/Web]      ← análise em tempo real
```

## Estrutura do Projeto

```
force-plate/
├── hardware/       # Esquemáticos, BOM, wiring diagrams
├── firmware/       # Código ESP32 (Arduino/PlatformIO)
├── software/       # App Python para aquisição e análise
├── cad/            # Modelos 3D e desenhos da plataforma
└── docs/           # Documentação, calibração, validação
```

## Roadmap

| Fase | Escopo | Status |
|------|--------|--------|
| 1 | MVP — plataforma única, vertical, 1000 Hz, BLE | 🔄 Planejamento |
| 2 | Segunda plataforma (dual) — assimetrias bilaterais | Futuro |
| 3 | Multiaxial (Fx, Fy, Fz) — forças horizontais | Futuro |

## Referências

- [can-can-group/forceplate-hardware-code](https://github.com/can-can-group/forceplate-hardware-code) — projeto de referência
- [force-plate-jump-analyses](https://github.com/stevenhirsch/force-plate-jump-analyses) — análise Python
- [Pyomeca](https://github.com/pyomeca/pyomeca) — framework biomecânica
