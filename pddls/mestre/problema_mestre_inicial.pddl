(define (problem jogo-problema)
  (:domain jogo-custo)
  (:objects 
    c0 c1 c2 - ciclo
    mission1 mission2 mission3 mission4 - mission
    d1 d2 - day
    cliente1 - client
    inspector1 - inspector
    p1 p2 p3 p4 - phase
  )
  (:init
    (current-phase p1)
    (client cliente1)
    (inspector inspector1)
  )
  (:goal (and (current-phase p4) (good-c0) (mission-done mission1) (mission-done mission2)))
)
