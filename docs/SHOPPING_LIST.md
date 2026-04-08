---
title: Shopping List — Montagem Mecânica
sidebar_position: 4
---

# Shopping List — Montagem Mecânica

**Data:** 2026-04-06
**Status:** Chapas de alumínio orçadas (Casa dos Metais). Aguardar AliExpress (~21/04–11/05) antes de fechar compras locais.
**Orçamento total:** ~R$ 845

---

## Metalúrgica / Corte de Chapas (~R$ 230)

| # | Item | Especificação | Qtd | Orçamento (R$) |
|---|------|--------------|:---:|----------:|
| 1 | Chapa superior | Al 5052-F, 603×503mm, 6,35mm (1/4"), cantos arredondados R30 | 1 | **410,00** |
| 2 | Chapa inferior | Al 5052-F, 530×399mm, 3mm, cantos chanfrados 15×15 a 45° | 1 | **140,00** |
| 3 | Tubo quadrado | Aço carbono 1020, 35×35×2mm, 2 peças de 527mm | 2 | ~20 |

:::tip Orçamento recebido (2026-04-06)
**Fornecedor:** Casa dos Metais Ltda — CNPJ 65.916.320/0001-31
Chapas 1 e 2 orçadas com dimensões comerciais (+3mm de folga). Total chapas: **R$ 550,00**.
Falta orçar corte dos cantos (R30 e chanfro 45°) e tubos de aço — possivelmente outro fornecedor.
:::

:::info Mudança de materiais (2026-04-06)
**Liga alumínio:** 6061-T6 não disponível localmente → 5052-F. Rigidez idêntica (E ~70 GPa), escoamento menor (90 vs 276 MPa) mas FS > 4 com a seção caixão.
**Tubos:** Alumínio quadrado difícil de encontrar → aço carbono padrão. Mais rígido (+23%), mais barato, produto de prateleira. Acréscimo de +1,4 kg no peso total.
:::

**Levar PDFs:** `cad/fab_chapa_superior.pdf`, `cad/fab_chapa_inferior.pdf`

:::note
Pedir corte e arredondamento/chanfro na metalúrgica. Furação e escareamento fazer em casa com gabarito para maior precisão.
:::

---

## Torneiro Mecânico (~R$ 160)

| # | Item | Especificação | Qtd | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 4 | Pézinho torneado com colar | Aço carbono ou inox, barra Ø60mm | 4 | ~160 |

**Dimensões da peça (de baixo para cima):**

| Parte | Dimensão |
|-------|----------|
| Borracha | Ø60mm × 1mm neoprene (colada após usinagem) |
| Base | Ø60mm × 8mm |
| Chanfro | Ø60→Ø20, 6mm altura (~17°) |
| Colar | Ø20mm × 5mm (batente mecânico) |
| Rosca | M12×1,75, Ø12mm, 32mm comprimento |
| **Altura total** | **52mm** |

**Levar PDF:** `cad/fab_pezinho.pdf`

---

## Serralheria / Usinagem (~R$ 20)

| # | Item | Especificação | Qtd | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 5 | Junta de aço | Aço carbono, 56×32mm, 2mm espessura, 2 furos Ø11mm passante, 25mm entre centros | 4 | ~20 |

**Levar PDF:** `cad/fab_junta.pdf`

---

## Parafusaria / Ferragens (~R$ 50)

| # | Item | Especificação | Qtd | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 6 | Parafuso Allen cabeça chata | M10×50, DIN 7991 (escareado/cônico) | 8 | ~20 |
| 7 | Porca sextavada M10 | DIN 934 (padrão) ou DIN 439 (baixa) | 8 | ~5 |
| 8 | Arruela lisa M10 | DIN 125 | 8 | ~5 |
| 9 | Broca HSS para metal | Ø11mm | 1 | ~10 |
| 10 | Escareador cônico 90° | Para M10, diâmetro Ø20mm | 1 | ~10 |

---

## Materiais e Consumíveis (~R$ 45)

| # | Item | Especificação | Qtd | Est. (R$) |
|---|------|--------------|:---:|----------:|
| 11 | Cola epóxi estrutural | Araldite Professional 24ml (ou Loctite EA, Devcon equiv.) | 1 | ~25 |
| 12 | Borracha neoprene | Disco Ø60mm × 1mm (cortar de manta se necessário) | 4 | ~10 |
| 13 | Lixa para metal | Grão 80 (preparação de superfície para colagem) | 2 | ~5 |
| 14 | Álcool isopropílico | Desengordurar superfícies antes da colagem | 1 | ~5 |

---

## Resumo por Fornecedor

| Fornecedor | Itens | Subtotal | Status |
|------------|:-----:|----------:|--------|
| Casa dos Metais (chapas Al) | 1–2 | **R$ 550** | Orçado |
| Metalúrgica (corte + tubos) | 3 + acabamento 1–2 | ~R$ 50 | Estimar |
| Torneiro | 4 | ~R$ 160 | Estimar |
| Serralheria | 5 | ~R$ 20 | Estimar |
| Parafusaria | 6–10 | ~R$ 50 | Estimar |
| Materiais | 11–14 | ~R$ 45 | Estimar |
| **Total** | **14 itens** | **~R$ 875** | |

---

## Checklist de Compras

- [ ] Casa dos Metais — fechar compra das 2 chapas Al (R$ 550)
- [ ] Metalúrgica — corte cantos (R30 + chanfro), furação se possível, tubos aço (levar 3 PDFs)
- [ ] Torneiro — 4 pézinhos (levar 1 PDF)
- [ ] Serralheria — 4 juntas de aço (levar 1 PDF)
- [ ] Parafusaria — parafusos M10×50 DIN 7991 + porcas + arruelas + broca + escareador
- [ ] Materiais — epóxi + borracha + lixa + álcool

:::warning Antes de comprar
1. Aguardar chegada das células de carga (AliExpress)
2. Montar 1 canto de teste para confirmar o gap entre chapas
3. Tubo de aço: 35×35×2mm (preferencial) ou 30×30×2mm com base no gap medido
4. Confirmar comprimento do parafuso M10×50 no empilhamento real
:::
