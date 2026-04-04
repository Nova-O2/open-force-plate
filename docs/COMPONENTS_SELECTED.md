# Componentes Selecionados — Force Plate MVP

Datas de compra: 2026-04-01 (principal), 2026-04-04 (substituição bateria)
Prazo estimado AliExpress: 20-40 dias (chegada ~21/04–11/05)

**Specs técnicas completas de cada componente:** ver [COMPONENT_SPECS.md](./COMPONENT_SPECS.md).
**Arquitetura de alimentação e dimensões de montagem:** ver [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md).

---

## AliExpress — Comprado 2026-04-01

| # | Item | Loja | Qtd | Unit. (R$) |
|---|------|------|:---:|----------:|
| 1 | Células de carga Decent DYX-301 500kg | DECENT Load Cell | 4 | 208,99 |
| 2 | Módulo ADS1256 24-bit (ADS1256IDB + ADR03) | Shop1105006670 | 2 | 48,29 |
| 3 | ESP32-S3-DevKitC-1 N16R8 (com pin headers) | Gangda Tong | 2 | 38,19 |
| 4 | TP4056 Type-C com proteção (kit 5) | Shop1105163493 | 1 | 10,10 |
| 5 | MT3608 boost converter (regular) | TianShiKai | 2 | 10,89 |
| 6 | Botão 12mm metal self-locking LED 3-9V | TechEss Electric | 1 | 11,89 |
| 7 | Protoboard 830pts (kit 3) | Aokin Wholesale | 1 | 21,44 |
| 8 | Jumper wires Dupont 20cm flexible 24AWG | CHANZON Official | 1 | 38,59 |
| 9 | Conectores XH 2.54mm 4pin 20cm (F5+M5) | Electrical Wire | 1 | 26,60 |
| 10 | Conectores PH 2.0mm (bateria→TP4056) | Electrical Wire | 1 | 36,69 |
| 11 | Kit resistores 300pcs 1/4W 1% metal film | Shop1103844365 | 1 | 12,69 |
| 12 | Kit LED 5mm pré-fiado 12V (30pcs, 6 cores) | CHANZON Global | 1 | 21,32 |

| | Valor (R$) |
|---|----------:|
| **Total pago AliExpress (produtos + impostos)** | **2.009,03** |
| Frete | Grátis |

---

## Mercado Livre — Comprado 2026-04-01

| # | Item | Loja | Qtd |
|---|------|------|:---:|
| 1 | ~~Bateria BGB Energy LiPo 3.7V (rotulada 3000mAh)~~ — **DEVOLVIDA** (overclaim, substituída) | Karina Mayumi | 1 |
| 2 | Ferro de solda Exbom 60W ajustável + 5 pontas + suporte 127V | Monteiro | 1 |
| 3 | Estanho 60/40 com fluxo 0.8mm 80g | MAHDUFINDS | 1 |
| 4 | Kit alicate crimpar + descascador + 1200 terminais ilhós | Cietec (oficial) | 1 |
| 5 | Alicate meia cana reto 6.1/2" Gedore Red | Ferramentasbarth | 1 |
| 6 | Kit multímetro digital + caneta tensão + alicate amperímetro | Meli Shopp (oficial) | 1 |

| | Valor (R$) |
|---|----------:|
| **Total pago Mercado Livre (01/04)** | **315,64** |
| Frete | Grátis |

---

## Mercado Livre — Comprado 2026-04-04 (substituição bateria)

| # | Item | Loja | Qtd | Unit. (R$) |
|---|------|------|:---:|----------:|
| 1 | Pack bateria Li-ion 1S2P 3.7V 5200mAh c/ BMS + JST-XH-2P (36×19×65mm) | EPB Energia Portátil Brasil (loja oficial — ENERGIAPORTATILBRASIL) | 2 | 26,71 |

| | Valor (R$) |
|---|----------:|
| **Total pago Mercado Livre (04/04)** | **53,42** |
| Frete | Grátis |

**Motivo:** substituição da bateria BGB Energy 3000mAh (01/04), que foi identificada como overclaim de capacidade (densidade energética reivindicada de 720 Wh/L, acima do limite teórico Li-ion). Os packs EPB 1S2P têm densidade realista (432 Wh/L), 2× células 18650 de 2.600 mAh cada, BMS integrada, geometria e peso consistentes com specs.

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

## Custo Total do Projeto

| Fonte | Valor (R$) |
|-------|----------:|
| AliExpress (produtos + impostos) | 2.009,03 |
| Mercado Livre (01/04) | 315,64 |
| Mercado Livre (04/04 — baterias EPB) | 53,42 |
| Estorno esperado bateria BGB (devolução ML) | (a deduzir após estorno) |
| Local (placas + juntas + parafusos + broca + escareador + pézinhos + borracha + tubos + cola) | ~505 |
| **TOTAL PROJETO (bruto)** | **~R$ 2.883** |

### Custo Unitário — 1 Plataforma (sem ferramentas, sem backups)

**~R$ 1.858**

| | Nova O2 | VALD FDMini | VALD FDLite |
|---|------:|----------:|----------:|
| Custo | R$ 1.858 | ~R$ 30.000 | ~R$ 60.000 |
| Capacidade | 2000 kg | 1000 kg | 2000 kg |
| Resolução | ~0.075–0.15 N | ~0.15 N | ~0.15 N |
| Conectividade | USB-C + BLE | USB | USB |

Para dual plate (Fase 5): +4 células + 1 ADS1256 ≈ +R$ 900.
