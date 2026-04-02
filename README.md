---
title: Nova O2 Force Plate — Plataforma de Força Open-Source
sidebar_position: 1
---

# Nova O2 Force Plate

Plataforma de força uniaxial (vertical) open-source para ciência do esporte.

## Visão Geral

Dispositivo de baixo custo (~R$ 360-700) capaz de medir força de reação do solo (GRF) a **1000 Hz** com resolução de **24 bits**, validável contra padrão-ouro (Kistler/AMTI/Bertec).

## Especificações-Alvo

| Parâmetro | Valor |
|-----------|-------|
| Eixos | 1 (vertical — Fz) |
| Taxa de amostragem | 1000 Hz |
| Resolução ADC | 24 bits (ADS1256) |
| Resolução teórica | ~0.075–0.15 N |
| Capacidade máxima | 2000 kg (4 × 500 kg) |
| Comunicação | USB-C + BLE (Bluetooth Low Energy) |
| Alimentação | Bateria LiPo recarregável + USB-C |
| Dimensões plataforma | 50 × 60 cm (single) / 2× 50 × 30 cm (dual) |
| Peso estimado | ~7 kg (1 chapa 6 mm + eletrônica) |

## Aplicações

- Countermovement Jump (CMJ) — altura, pico de força, impulso
- Squat Jump (SJ)
- Drop Jump (DJ) — RSI (Reactive Strength Index)
- Rate of Force Development (RFD)
- Testes unilaterais (assimetria via alternância)
- Tempo de contato no solo

## Arquitetura

```
       ┌─────────────────────────┐
       │  Placa alumínio 50×60  │  ← superfície de apoio (topo)
       └────┬────┬────┬────┬────┘
            │    │    │    │
       [4× Células F shear beam 500kg]  ← pézinhos apoiam no chão
            │    │    │    │
       ═══════════════════════════  ← piso rígido e plano
                 │
         [ADS1256 24-bit ADC]  ← 1000 Hz SPI
                 │
              [ESP32-S3]       ← processamento + BLE + USB-C
                 │
          [App Python/Web]     ← análise em tempo real
```

## Estrutura do Projeto

```
force-plate/
├── hardware/       # Esquemáticos, BOM, wiring diagrams
├── firmware/       # Código ESP32 (Arduino/PlatformIO)
├── software/       # App Python para aquisição e análise
├── cad/            # Modelos 3D e desenhos da plataforma
└── docs/
    ├── DEVELOPMENT_PLAN.md    # Como montar e desenvolver (fases, specs, checklists)
    ├── COMPONENTS_SELECTED.md # Registro de compras (itens, lojas, valores)
    └── *.png/pdf              # Datasheets e imagens de referência
```

## Roadmap

| Fase | Escopo | Status |
|------|--------|--------|
| 1 | Hardware — montagem mecânica e eletrônica | Componentes comprados (01/04), aguardando chegada |
| 2 | Firmware — ESP32 + ADS1256 @ 1000 Hz + USB-C/BLE | Aguardando hardware |
| 3 | Software — app Python, visualização, análise de saltos | Pode iniciar (não depende de hardware) |
| 4 | Validação — técnica + científica (N≥20, comparação VALD) | Após montagem |
| 5 | Dual — cortar chapa ao meio (2× 50×30 cm) + 4 sensores extras | Futuro |
| 6 | Produto — PCB, enclosure, app mobile, open-source | Futuro |

## Referências

- [can-can-group/forceplate-hardware-code](https://github.com/can-can-group/forceplate-hardware-code) — projeto de referência
- [force-plate-jump-analyses](https://github.com/stevenhirsch/force-plate-jump-analyses) — análise Python
- [Pyomeca](https://github.com/pyomeca/pyomeca) — framework biomecânica
