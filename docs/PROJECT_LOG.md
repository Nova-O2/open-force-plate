# Project Log — Nova O2 Force Platform

Chronological project record. Most recent entry at the top.

For technical specs: [COMPONENT_SPECS.md](./COMPONENT_SPECS.md) | For costs: [COMPONENTS_SELECTED.md](./COMPONENTS_SELECTED.md) | For roadmap: [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md)

---

## 2026-06-10 — Auditoria as-built completa + desenhos re-renderizados (Rev 3.1)

Auditoria de conformidade as-built em toda a documentação (3 agentes paralelos), corrigindo tudo que ainda representava valores previstos em vez dos reais:

### Correções aplicadas

- **`fabrication_drawings.py` + 5 PDFs re-renderizados:** `SHIM_T` 1.5 → **2 mm**, `DESIGN_REV` 3.0 → **3.1**, header com histórico Rev 3.1. `fab_shim.pdf` agora cota 2 mm final (debt do log 08/06 quitado)
- **Stack height corrigido em 3 docs:** 44.35 → **45.35 mm** as-built (shim 2 mm). Engajamento M10×60 reverificado: trecho em stack abaixo da cabeça escareada 39.85 mm → 14.65 mm livres = arruela + Parlock + ~2.6 mm de sobra — **≥ 1×D mantido** ✓ (margem 1 mm menor que o nominal)
- **COMPONENT_SPECS:** pezinho as-built (zincado 25/05; borracha = retalho + Tekbond 793, não neoprene comprado), epóxi 2× → **4× 23 g**, prep as-built **P24 + acetona** (spec era P40-P60 + isopropílico), nota as-built de torque não instrumentado em §2.6
- **DEVELOPMENT_PLAN:** checklists de procurement/assembly/tube bonding fechadas com datas reais (13 itens [ ] → [x]); itens restantes anotados como pré-calibração (visual check escareado, nivelamento, teste de rigidez); anti-seize marcado como não usado as-built
- **CONTRIBUTING:** tabela de revisões ganhou linha **Rev 3.1** (tubo inox 304 1.5 mm + shim 2 mm + assembly 08/06)
- **STRUCTURAL_ANALYSIS §7.2:** nota as-built — caixão interno medido ~36 mm (bondlines ~0.5 mm/junta), efeito <3% e conservador; shims fora da seção de flexão, cálculos inalterados
- **SHOPPING_LIST:** dims das chapas esclarecidas (603×503/530×399 = stock +3 mm → 600×500/527×396 finais)

### Permanece previsto (não medido — honesto)

- Peso total ~13 kg (estimado); torque 20-25 N·m não verificado (sem torquímetro); scripts Rev 1.0 (`structural_analysis.py` etc.) seguem arquivados como histórico — SSOT é o STRUCTURAL_ANALYSIS.md

### Tag `v3.1.0-rc1` criada (governança git)

Gap de rotulagem detectado e fechado: a Rev 3.1 (18/05) tinha substituído a Rev 3.0 sem tag — README declarava "Rev 3.1-rc1" sem âncora no git. Tag anotada `v3.1.0-rc1` criada em `d9cd823` seguindo o precedente da `v3.0.0-rc1` (que nunca será promovida — design superado antes da validação): registra estado as-built, caveat do torque e checklist de promoção a `v3.1.0` (visual check + piso/nível + rigidez + 1ª calibração <0.5% erro). Ponteiro do submodule no workspace também estava stale (2 pushes sem bump) — corrigido; naming do release Fase 1 no README alinhado ao semver (`v0.1-alpha` → `v3.1.0`).

---

## 2026-06-08 — Montagem mecânica concluída

### Assembly final — 4 cantos montados

- Montagem completa da plataforma: 4 cantos com célula DYX-301 + 2× shim inox 304 2 mm (espelhado) + M10×60 DIN 7991 + arruela 304 + Parlock, sobre a estrutura colada (chapas Al 5052-F + seção caixão inox 304)
- **Sem torquímetro** — aperto manual por sensibilidade; spec de 20–25 N·m **não verificada instrumentalmente**. Aceito para o MVP; re-torque instrumentado opcional antes da primeira calibração se houver acesso a torquímetro
- **Fase de montagem mecânica ENCERRADA** — estrutura física da plataforma completa

### Próximos passos

- Bancada eletrônica: ADS1256 + ESP32-S3 + alimentação + cabeamento das 4 células
- First calibration → trigger `v3.1.0-rc1` → `v3.1.0` tag promotion
- Debt registrado: `COMPONENT_SPECS.md` §2.3 atualizado para 2 mm final; re-render de `fabrication_drawings.py` + `fab_shim.pdf` com 2 mm ainda pendente

### Cascade executada 2026-06-10

Cascade write-through acumulada desde 19/05 aplicada em batch nesta data (README EN+PT, SHOPPING_LIST, COMPONENTS_SELECTED, COMPONENT_SPECS §2.3, `00-core/priorities.md`): Araldite 4× 23 g (R$ 124), zincagem pezinhos (R$ 105), hardware ML entregue (R$ 136,19), chapa inox shim (R$ 79,90), corte+furação shims AL Usinagem (R$ 180), shim 2 mm final, borracha Tekbond 793.

---

## 2026-05-29 a 2026-06-03 — Shims fabricados: chapa recebida → AL Usinagem → 8 shims entregues

- **29/05:** chapa inox 304 300×100×2 mm (MALUCOMERCIAL/ML, R$ 79,90) **chegou** (previsão era 27-28/05) — **entregue no mesmo dia à AL Usinagem** com as medidas previstas
- **03/06:** AL Usinagem **entregou os 8 shims** cortados e furados nas medidas previstas, 2 mm de espessura
- **Custo do serviço: R$ 180** (não foi cortesia — corte + furação dos 8 shims)
- Custo total dos shims: R$ 259,90 (chapa R$ 79,90 + serviço R$ 180) — dentro da estimativa de R$ 150–200 só do serviço

---

## 2026-05-26 — Borracha colada (Tekbond 793) + medição seção caixão + pivot shim fabrication

### Borracha dos pezinhos — colada

- Adesivo de contato neoprene (cola preta de reparo de wetsuit, policloropreno) — bond **parcial / inconsistente** (pegou em algumas regiões, não em outras), insuficiente pra confiar em uso cíclico
- Solução adotada: **Tekbond Adesivo Instantâneo 793 (100 g, cianoacrilato)** — colou bem, pezinhos prontos
- Trade-off aceito: cianoacrilato é bond rígido sob compressão cíclica → risco de peel failure no médio prazo. Aceitável para o protótipo MVP; refazer com adesivo flexível na v2 caso descole
- Hipóteses pra falha do contato (não verificadas, p/ futura referência): selo cromatado do zincado branco deixa superfície mais inerte que metal nu; surface prep com lixa P150-220 + álcool pode ter sido insuficiente — lixa mais agressiva (P80) ou etch químico leve poderia ter ajudado

### Medição empírica da seção caixão (pós-cura Sessão 2)

- Espaço interno entre as chapas: **~36 mm**
- Cell DYX-301 H: 32 mm
- **Gap total a vencer pelos shims: 4 mm**
- Configuração espelhada confirmada: 2 mm de shim em cima + 2 mm em baixo
- **Shim thickness final: 2 mm** (Rev 3.0 previa 1.5 mm nominal — empírico ficou 0,5 mm acima, dentro da tolerância da bondline Araldite)

### Shim sourcing — material self-sourced, machining ainda na AL Usinagem

- Decisão: comprar a chapa stock diretamente (sem markup intermediário) e enviar para AL Usinagem fazer **corte + furação** dos 8 shims
- **Chapa adquirida hoje:** aço inox 304, **300 × 100 × 2 mm**, MALUCOMERCIAL (MercadoLivre) — **R$ 79,90**
- **Previsão de entrega: qua-qui 27-28/05/2026**
- Yield: 30.000 mm² disponíveis → folga confortável para 8 shims (geometria final a definir antes da ordem na AL)
- **AL Usinagem (cut + drill 8 shims):** custo TBD — pode ser cobrado ou cortesia ("talvez cobrem, talvez não") dado o relacionamento já estabelecido + serviço de baixa complexidade

### Próximos passos

- Aguardar chegada da chapa (27-28/05)
- Definir geometria final dos 8 shims (dimensões + furação) — alinhada com hardware ML já em mãos (M10×60)
- Levar chapa + spec para AL Usinagem
- Receber shims cortados e furados
- Test-fit em 1 canto: alinhamento + torque 20–25 N·m sem deformação visível na chapa Al
- First calibration → trigger `v3.1.0-rc1` → `v3.1.0` tag promotion

### Cascade pendente — acumulada (mantida adiada por decisão Aldo)

Itens a refletir no cascade write-through quando disparar:
- Araldite total (4× 23 g = R$ 124)
- Zincagem pezinhos (R$ 105 — TL Tratamento Superficial)
- Hardware ML entregue (R$ 136,19 — ver entrada 12-13/05)
- **Chapa inox 304 stock 300×100×2 mm (R$ 79,90 — MALUCOMERCIAL/MercadoLivre) [novo hoje]**
- **AL Usinagem cut + drill 8 shims (custo TBD — pode ser cortesia)** [novo hoje]
- Mudança de plano: material da chapa shim self-sourced (era "AL Usinagem cota tudo"); machining (corte + furação) permanece na AL Usinagem
- Shim thickness final empírico: 2 mm (era 1.5 mm nominal no Rev 3.0)
- Borracha pezinhos: colada com Tekbond 793 (adesivo já em estoque doméstico — custo zero p/ projeto)

---

## 2026-05-25 — Pezinhos zincados retirados + Sessão 2 curada + medições do dia

### Pezinhos — zincagem concluída

- **Retirados hoje pela manhã** (antes do almoço, conforme planejado no log de 20/05)
- **Pagamento: R$ 105** (meio banho zincagem anti-corrosão) — despesa registrada, fica para a cascade
- Próximo passo imediato: colar borracha (retalho disponível) na base dos pezinhos — execução prevista para hoje

### Bonding Sessão 2 — cura completa, junta íntegra

- Cura concluída após 5 dias (20/05 → 25/05, mais que os 24 h mínimos do Araldite Profissional)
- Inspeção visual da junta: íntegra, sem desalinhamento ou bolha visível
- Estrutura aprovada para próxima fase (medição + assembly)

### Próximas execuções de hoje

- Colar borracha nos pezinhos zincados (retalho disponível, adesivo de contato)
- **Medir altura real da seção caixão empiricamente** (com paquímetro nos 4 cantos — base para shim final)
- **Cotar 8 shims inox 304** com AL Usinagem (espessura definida pela medição acima)

### Cascade write-through — ainda adiada

Decisão Aldo: cascade write-through (README EN+PT, SHOPPING_LIST, COMPONENTS_SELECTED, `00-core/priorities.md`) **continua adiada** — será executada em batch quando o ciclo de medição + cotação + assembly avançar mais. Itens acumulados para a cascade:

- Araldite total (4× 23 g = R$ 124)
- Zincagem pezinhos (R$ 105)
- Hardware ML entregue (ver entrada 12-13/05)

---

## 2026-05-20 — Bonding session 2: bottom plate + foot zincagem encaminhada

### Aquisição

- **2× 23 g Araldite Profissional** comprados hoje na **Real Fortaleza Hidráulica Industrial** (mesmo fornecedor, mesmo preço — R$ 62 total). Lote novo para Sessão 2.

### Execução

- **Re-prep das faces remanescentes:** tubos inox 304 (face oposta, que mateia com chapa inferior) re-lixados P24 — Cr₂O₃ já re-passivou desde Sessão 1
- **Chapa inferior Al 5052-F:** prep nova P24
- **Degrease:** acetona pura
- **Aplicação:** Araldite Profissional 2× 23 g misturado 1:1 → aplicado nas 2 faces (bottom plate + faces remanescentes dos tubos) → assentado → carga aplicada
- **Cura:** 24 h+ em curso, atravessa toda a viagem Belém (21-24/05). Retorno seg 25/05 para inspeção da junta.

### Pezinhos — tratamento zincagem anti-corrosão (paralelo)

- Pezinhos deixados na **terça 19/05** em serviço de zincagem anti-corrosão (fornecedor confirmou prazo: prontos segunda)
- **Custo meio banho: R$ 105** (despesa nova, ainda não refletida em SHOPPING/COMPONENTS — cascade no fechamento)
- **Retirada agendada seg 25/05 antes do almoço**

### Próximos passos — seg 25/05 (pós-viagem)

- Buscar pezinhos zincados antes do almoço
- Inspecionar junta da Sessão 2 após cura completa
- Colar borracha (retalho disponível) nos pezinhos
- Apenas então: medir altura real da seção caixão + cotar 8 shims inox 304 + checar entrega ML hardware

### Cascade pendente (mantido do log da Sessão 1)

Cascade write-through (README EN+PT, SHOPPING_LIST, COMPONENTS_SELECTED, `00-core/priorities.md`) fica adiado até inspeção pós-cura na seg 25/05 — decisão Aldo, evita atualizar várias vezes. Incluir nesta cascade: Araldite total (4× 23 g = R$ 124), zincagem pezinhos (R$ 105).

---

## 2026-05-19 (tarde) — Bonding session 1: top plate + tubes (parcial — 2ª sessão pendente)

### Execução

- **Tubos cortados** em 2× 500 mm (corte feito antes da lixa para não re-lixar topos)
- **Prep das superfícies (lado bondado hoje):** tubos inox lixados P150 → P24 (faces que mateiam com chapa superior); chapa superior Al 5052-F lixada P24
- **Degrease:** acetona pura (álcool isopropílico indisponível — Tekbond aceita acetona como alternativa equivalente)
- **Roteamento de cabos:** decidido passar pelo canal entre os 2 tubos — sem furos nas barras (evita concentrador de tensão + fadiga)
- **Aplicação:** Araldite Profissional 2× 23 g misturado 1:1 → aplicado nas 2 faces (top plate + topo dos tubos) → assentado → carga aplicada
- **Clamping improvisado:** sacos de areia distribuídos sobre as linhas dos tubos + tábua de distribuição de carga em cima da chapa superior + cunhas laterais para restrição de slip durante a fase de baixa viscosidade
- **Cura:** 24 h em temperatura ambiente em curso

### Desvio do plano original (Rev 3.1 → bonding em 2 estágios)

- Plano original: bondar chapas superior + inferior na mesma sessão com 2× 23 g (≈ 46 g total)
- Realidade: 46 g cobriu só uma face — folga de 25% sobre 25-35 mL estimados foi otimista em prática
- Decisão: bonding em 2 estágios — top plate hoje, bottom plate em sessão futura com novo lote de Araldite
- Trade-off aceito: 2 sessões + R$ 62 adicionais (compra) vs. risco de underfill da junta

### Pendente (próxima sessão)

- Comprar **mais 2× 23 g Araldite Profissional** (~R$ 62, Real Fortaleza Hidráulica)
- **Re-prep das faces remanescentes:**
  - Tubos: face oposta (que mateia com chapa inferior) — re-lixar P24 (Cr₂O₃ vai re-passivar até lá)
  - Chapa inferior Al 5052-F: prep nova P24 (não foi tocada hoje)
- Degrease acetona + aplicação + assentamento + clamping 24 h
- Apenas então: medir altura real da seção caixão + cotar 8 shims inox 304 (AL Usinagem) + checar entrega ML hardware

### Não atualizado nesta entrada (será atualizado quando a 2ª sessão fechar)

- README.md (EN + PT) — Status, cost breakdown, pending list
- docs/SHOPPING_LIST.md — total spent, item Araldite quantidade
- docs/COMPONENTS_SELECTED.md — quantidade real de Araldite
- 00-core/priorities.md — linha force-plate

Cascade write-through será feito de uma vez no fechamento da 2ª sessão (decisão Aldo, evita atualizar 2 vezes).

---

## 2026-05-19 (manhã) — Structural epoxy acquired (Araldite Professional)

- **Real Fortaleza Hidráulica Industrial** (same supplier as the Rev 3.1 inox 304 tube), Praça Independência 107, São João, Jacareí-SP
- **Araldite Profissional bicomponente** (Tekbond BRAP000), 23 g bisnaga — **2 unidades × R$ 31,00 = R$ 62,00**
- Estimate was ~R$ 50 → actual R$ 62 (+R$ 12 / +24%): single-supplier convenience over hunting hardware stores
- Unblocks bonding step (chapas + tubos inox 304 com epóxi estrutural, 24 h cura) once tube is cut into 2× 500 mm

### Pending (next steps)

- Cut tube into 2× 500 mm
- Buy remaining consumables (P40–P60 sandpaper, isopropyl alcohol, bar clamps)
- Bond plates + tubes with structural epoxy (24 h cure under clamping)
- Measure bonded box section height empirically → quote 8 inox 304 shims (AL Usinagem)
- Test-fit single corner → first calibration → promote `v3.1.0-rc1` → `v3.1.0`

---

## 2026-05-18 — Rev 3.1: stainless steel 304 structural tube acquired

### Tube purchased

- **Real Fortaleza Hidráulica Industrial** (D.A. Coutinho & Cia Ltda), Praça Independência 107, São João, Jacareí-SP
- TUBO QUADRADO 304 35×35×1,50 mm — 1,00 m — **R$ 103,67** (cartão de crédito, NFC-e nº 3014, 2026-05-18 13:22)
- Cut plan: 1 m bar → 2 pieces of 500 mm

### Spec deviations from Rev 3.0 (all validated, accepted as Rev 3.1)

1. **Material:** 1020 carbon steel → **stainless steel 304** — upgrade. Galvanic compatibility with Al 5052-F, no anti-corrosion coating needed. Completes the "inox 304 throughout" rule from Rev 3.0 (the tube was the last carbon-steel exception).
2. **Wall:** 2 mm → **1.5 mm** — the off-the-shelf stainless square tube. Transformed inertia recomputed: I_tr 1,305,342 → 1,234,842 mm⁴ (−5%). DJ 5× deflection 0.143 → 0.151 mm; structural FS 5.9 → 5.5; bond τ 0.95 → 0.98 MPa (FS ≈ 14–16×). All STRUCTURAL_ANALYSIS §9 acceptance criteria still met.
3. **Length:** 527 mm → **500 mm** (2 pieces from a 1 m bar) — covers the 475 mm support span with ~12.5 mm cantilever each side.

### Adhesive decision

- **Araldite Professional 90 min** (Tekbond, code BRAP000) selected for the MVP prototype — 2× 23 g bisnaga (≈ 42 mL, 25% headroom over the 25–35 mL effective need).
- On stainless, ambient cure: ~14–16 MPa shear → bond FS ≈ 14–16×. Design is dominated by stiffness, not bond strength.
- DP460 (≥ 20 MPa, FS > 20×) noted as the upgrade path for a continuously-used production v2 — overkill for the prototype.
- Surface prep: P40–P60 grit (coarse — stainless 304 passive Cr₂O₃ layer; P80 too fine).

### Documentation

- Transformed-section recalculation done by hand — the CAD scripts (`hardware/cad/*.py`) remain Rev 1.0 archaeological: they never implemented the composite transformed section, so `STRUCTURAL_ANALYSIS.md` §7 is the analysis SSOT. Recompute verified by reproducing the Rev 2.0 baseline.
- Cascade: STRUCTURAL_ANALYSIS, COMPONENT_SPECS, COMPONENTS_SELECTED, SHOPPING_LIST, README (EN+PT), DEVELOPMENT_PLAN updated to Rev 3.1.

### Pending (next steps)

- Buy Araldite Professional (2× 23 g) + consumables (P40–P60 sandpaper, isopropyl alcohol, bar clamps)
- Cut tube into 2× 500 mm
- Bond plates + tubes with structural epoxy (24 h cure under clamping)
- Measure bonded box section height empirically → quote 8 inox 304 shims (AL Usinagem)
- Test-fit single corner → first calibration → promote `v3.1.0-rc1` → `v3.1.0`

---

## 2026-05-12 a 13 — Hardware MercadoLivre entregue

- Entrega dos itens comprados em 08/05 (ver entrada daquela data):
  - 10× M10×60 DIN 7991 inox 304 (MIXPARAFUSOS)
  - 20× porca Parlock M10 inox 304 all-metal (EMAIFIX)
  - 20× arruela plana M10 inox A2/304 (USINIK)
- Total R$ 136,19 — todos os itens em mãos, prontos para o assembly após medição da seção caixão
- Desbloqueia: assembly de teste em 1 canto assim que shims novos chegarem

---

## 2026-05-08 — Rev 3.0 trigger: components received + fastening redesign

### Components received from AL Usinagem (machine shop)

- 4× turned foot pieces (M12 thread + collar + base + rubber pad)
  - **Spec deviation noted:** turned bar Ø55 mm (was specified Ø60 mm in Rev 2.0) — machine shop preference for available material stock
  - **Spec addition noted:** base vertical wall (Ø55 mm cylindrical surface) knurled (recartilhado) — facilitates operator grip when threading the foot piece M12 into the load cell
- 4× aluminum plates (top + bottom, both Al 5052-F) — drilled (8× Ø11 mm thru-holes each, with countersinking on top plate) + perimeter chamfer
  - **Acabamento (chamfer) details:**
    - Top plate (6.35 mm): 45° × 2.12 mm chamfer on **both faces** (1/3 of thickness)
    - Bottom plate (3 mm): 45° × 1.5 mm chamfer on **bottom face only** (1/2 of thickness)
  - Documented from AL Usinagem hand-sketch (lateral cross-section view)

### Costs (AL Usinagem)

- Foot pieces machining: R$ 1,120 (R$ 280 each × 4)
- Plate finishing (drilling + chamfer): R$ 360
- **Subtotal AL Usinagem (received): R$ 1,480**

### Hardware purchased today (MercadoLivre)

- M10×60 DIN 7991 inox 304 (kit 10 un) — **MIXPARAFUSOS** — R$ 76,05 (frete grátis)
- M10 Parlock all-metal locknut inox 304 (2× kit 10 un) — **EMAIFIX** — R$ 37,14 (16% off, frete grátis)
- M10 plain washer inox A2/304 (2× kit 10 un) — **USINIK** (loja oficial) — R$ 23,00 (frete grátis)
- **Subtotal ML hardware: R$ 136,19** — awaiting delivery

### Design decisions (this session) → trigger Rev 3.0

- Switch fastening from class 8.8 carbon steel to **inox 304 throughout** (parafuso + porca + arruela + shim) for galvanic compatibility with Al 5052-F plates and reusable anti-vibration locking (Parlock)
- **Add 4 bottom shims** (mirror configuration: 4 top + 4 bottom = 8 total). Bearing FS analysis: direct nut-on-aluminum (without bottom shim) gives FS ≈ 1.05 → unsafe; mirror shim brings FS ≈ 11
- Bolt length 50 → 60 mm to accommodate added bottom shim in stack (top plate 6.35 + top shim 1.5 + cell 32 + bottom shim 1.5 + bottom plate 3 = 44.35 mm + nut + washer)
- Shim thickness 2 → 1.5 mm nominal (final TBD empirical — see `COMPONENT_SPECS.md` §2.3.1 process gate)
- Torque target reduced 50–60 → 20–25 N·m (lower preload of A2-70 vs cl 8.8) + anti-seize on DIN 7991 cone face
- Discarded purchase: parafuso M10×40 DIN 7991 (Belenus, LUTEC) — incorrect length (would not reach nut after stack)

### Pending (next steps — see Rev 3.0 plan)

- Steel tubes 35×35×2 mm 1020 carbon — confirm arrival + dimensions with caliper
- Bond plates+tubes with structural epoxy (24 h cure)
- Measure bonded box section height + cell H actual at 4 corner positions
- Quote 8 new shims (inox 304, thickness from measurement) — AL Usinagem
- Hardware ML delivery
- Test-fit single corner before mass assembly (torque 20–25 N·m, no visible Al deformation)
- First calibration → triggers `v3.0.0-rc1` → `v3.0.0` final tag promotion

---

## 2026-04-25 — AL Usinagem kickoff: measurements verified, machining started

- Meeting with AL Usinagem (machine shop) — measurement check on aluminum plates and discussion of fabrication scope
- Measurements confirmed against fabrication PDFs (`hardware/cad/fab_top_plate.pdf`, `fab_bottom_plate.pdf`, `fab_foot_piece.pdf`)
- Machining started: top + bottom plates (corner cutting R30 / 15×15 chamfer + Ø11 mm drilling + Ø20 countersinking) and 4× turned foot bolts with collar
- Steel shims (4×) and steel tubes (35×35×2 mm box section) still to be sourced — pending gap measurement after first corner assembled

## 2026-04-23 — Load cells received

- 4× DYX-301 500 kg shear-beam load cells received, all units intact (no damage)
- Last AliExpress shipment closed — all components now in hand
- Unblocks: turned foot machining (measurements can be verified against actual cell threads/dimensions)

## 2026-04-16 — Components in hand, mechanical assembly begins

- 5052-F aluminum plates picked up at Casa dos Metais (R$550 — 6.35mm top + 3mm bottom)
- All AliExpress + Mercado Livre components in hand, except DYX-301 load cells
- Load cells already in Brazil — expected to arrive this week
- Turned feet on hold until load cells arrive to confirm measurements before ordering from machinist

## 2026-04-14 — AliExpress delivery

- 11 of 12 AliExpress items received in a single batch: ADS1256, ESP32-S3, TP4056, MT3608, button, breadboards, jumpers, XH/PH connectors, resistors, LEDs
- DYX-301 load cells not included in this batch (separate seller/shipment)

## 2026-04-11 — Replacement batteries received

- Received 2× Li-ion 1S2P 5200mAh batteries with BMS (replacement for the returned BGB battery, which was identified as a capacity overclaim)

## 2026-04-04 — Mechanical design Rev. 2.0

Complete overhaul of mechanical design with structural analysis:

- Material change: 6061-T6 aluminum → 5052-F (local availability), Al tubes → 1020 steel (off-the-shelf)
- Top plate thickness: 6mm → 6.35mm (1/4" — available standard)
- Box section (2× 35×35mm steel tubes) reduces deflection from 21mm to <0.2mm
- Correction: M10×45 screws → M10×50, 30mm chamfer → 15mm
- Structural analysis recalculated with transformed section (n = 2.845) — FS >4 in all scenarios
- Local components shopping list created (~R$500)
- BGB Energy 3000mAh battery identified as overclaim (720 Wh/L, above theoretical Li-ion limit) — returned
- Privacy cleanup: supplier data moved to gitignored file

## 2026-04-01/02 — Mechanical design Rev. 1.0 + purchases

**Component selection and purchases (01/04):**
- Components selected: DYX-301 500kg (shear beam), ADS1256 24-bit ADC, ESP32-S3 N16R8
- Architecture decision: AMS1117 LDO replaced by MT3608 boost converter (stable 5V from LiPo 3.3–4.2V)
- AliExpress order placed: 12 items, R$2,009
- Mercado Livre order placed: 7 items (tools + battery), R$369
- Docs reorganized: specs separated from purchases, clear responsibilities between files

**Mechanical design (01–02/04):**
- Design finalized: 62° angle (half-plate diagonal), single bottom plate, 56×32mm shims
- Fabrication drawings generated (3 PDFs with Nova O2 branding): top plate, bottom plate, turned foot
- Turned foot specs: M12×1.75 shaft, ~17° chamfer, Ø60×8mm base, Ø20×5mm collar, 1mm rubber pad

## 2026-03-28 — Project start

- Project created: open-source force platform for sports science
- Initial specs defined: uniaxial (Fz), 1000 Hz, 24-bit, 2000 kg, USB-C + BLE
- Positioning: comparable to VALD FDLite (~R$60,000) at a fraction of the cost (~R$2,500)
- 6-phase development plan: hardware → firmware → software → validation → dual plate → product
