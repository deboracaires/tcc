;; Problema gerado automaticamente
(define (problem problema_mestre)
  (:domain jogo-custo)
  (:objects 
    c0 c1 c2 - ciclo
    mission1 mission2 mission3 mission4 - mission
    p1 p2 p3 p4 - phase
  )
  (:init
    (current-phase p3)
    (diario-preso)
    (cenario-arrumado)
    (good-c0)
    (mission-done mission1)
  )
  (:goal (current-phase p4))
)
