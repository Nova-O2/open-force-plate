# Componentes Selecionados — Force Plate MVP

Datas de compra: 2026-04-01 (principal), 2026-04-04 (substituição bateria)
Prazo estimado AliExpress: 20-40 dias (chegada ~21/04–11/05)

**Specs técnicas completas de cada componente:** ver [COMPONENT_SPECS.md](./COMPONENT_SPECS.md).
**Arquitetura de alimentação e dimensões de montagem:** ver [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md).
**Fornecedores e preços:** `suppliers_private.md` (gitignored, não versionado).

---

## AliExpress — Comprado 2026-04-01

| # | Item | Qtd |
|---|------|:---:|
| 1 | Células de carga Decent DYX-301 500kg | 4 |
| 2 | Módulo ADS1256 24-bit (ADS1256IDB + ADR03) | 2 |
| 3 | ESP32-S3-DevKitC-1 N16R8 (com pin headers) | 2 |
| 4 | TP4056 Type-C com proteção (kit 5) | 1 |
| 5 | MT3608 boost converter (regular) | 2 |
| 6 | Botão 12mm metal self-locking LED 3-9V | 1 |
| 7 | Protoboard 830pts (kit 3) | 1 |
| 8 | Jumper wires Dupont 20cm flexible 24AWG | 1 |
| 9 | Conectores XH 2.54mm 4pin 20cm (F5+M5) | 1 |
| 10 | Conectores PH 2.0mm (bateria→TP4056) | 1 |
| 11 | Kit resistores 300pcs 1/4W 1% metal film | 1 |
| 12 | Kit LED 5mm pré-fiado 12V (30pcs, 6 cores) | 1 |

---

## Mercado Livre — Comprado 2026-04-01

| # | Item | Qtd |
|---|------|:---:|
| 1 | ~~Bateria BGB Energy LiPo 3.7V (rotulada 3000mAh)~~ — **DEVOLVIDA** (overclaim, substituída) | 1 |
| 2 | Ferro de solda Exbom 60W ajustável + 5 pontas + suporte 127V | 1 |
| 3 | Estanho 60/40 com fluxo 0.8mm 80g | 1 |
| 4 | Kit alicate crimpar + descascador + 1200 terminais ilhós | 1 |
| 5 | Alicate meia cana reto 6.1/2" Gedore Red | 1 |
| 6 | Kit multímetro digital + caneta tensão + alicate amperímetro | 1 |

---

## Mercado Livre — Comprado 2026-04-04 (substituição bateria)

| # | Item | Qtd |
|---|------|:---:|
| 1 | Pack bateria Li-ion 1S2P 3.7V 5200mAh c/ BMS + JST-XH-2P (36×19×65mm) | 2 |

**Motivo:** substituição da bateria BGB Energy 3000mAh (01/04), que foi identificada como overclaim de capacidade (densidade energética reivindicada de 720 Wh/L, acima do limite teórico Li-ion). Os packs 1S2P substitutos têm densidade realista (432 Wh/L), 2× células 18650 de 2.600 mAh cada, BMS integrada, geometria e peso consistentes com specs.

---

## Comprar Local (quando AliExpress chegar)

| # | Item | Qtd | Est. (R$) |
|---|------|:---:|----------:|
| 1 | Placa superior alumínio 6061-T6, 600×500mm, 6mm, cantos R30 | 1 | ~150 |
| 2 | Placa inferior alumínio, 527×396mm, 3mm, cantos chanfrados 15×15 | 1 | ~60 |
| 3 | Juntas de aço 2mm (56×32mm, 2× Ø11mm, 25mm entre centros) | 4 | ~20 |
| 4 | Parafusos Allen M10×50 DIN 7991 + porcas M10 + arruelas (8+8+8) | 1 | ~30 |
| 5 | Broca Ø11mm + escareador 90° M10 (Ø20) | 1 | ~20 |
| 6 | Pézinhos torneados com colar Ø20×5mm (peça única, torneiro) | 4 | ~160 |
| 7 | Discos borracha neoprene Ø60mm × 1mm | 4 | ~10 |
| 8 | Tubo quadrado alumínio 30×30 ou 35×35×2mm, ~527mm | 2 | ~30 |
| 9 | Cola epóxi estrutural (Araldite Professional 24ml ou equiv.) | 1 | ~25 |
| | | **Subtotal** | **~R$ 505** |

---

## Custo Unitário — 1 Plataforma (sem ferramentas, sem backups)

**~R$ 1.858**

| | Nova O2 | VALD FDMini | VALD FDLite |
|---|------:|----------:|----------:|
| Custo | R$ 1.858 | ~R$ 30.000 | ~R$ 60.000 |
| Capacidade | 2000 kg | 1000 kg | 2000 kg |
| Resolução | ~0.075–0.15 N | ~0.15 N | ~0.15 N |
| Conectividade | USB-C + BLE | USB | USB |

Para dual plate (Fase 5): +4 células + 1 ADS1256 ≈ +R$ 900.
