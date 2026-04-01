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
└── docs/           # Documentação, calibração, validação
```

## Roadmap

| Fase | Escopo | Status |
|------|--------|--------|
| 1 | MVP — plataforma única, vertical, 1000 Hz, BLE | 🔄 Planejamento |
| 2 | Dual — cortar chapa ao meio (2× 50×30 cm) + 4 sensores extras | Futuro |
| 3 | Multiaxial (Fx, Fy, Fz) — forças horizontais | Futuro |

## Referências

- [can-can-group/forceplate-hardware-code](https://github.com/can-can-group/forceplate-hardware-code) — projeto de referência
- [force-plate-jump-analyses](https://github.com/stevenhirsch/force-plate-jump-analyses) — análise Python
- [Pyomeca](https://github.com/pyomeca/pyomeca) — framework biomecânica
