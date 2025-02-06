;; Problema NPC gerado automaticamente
(define (problem missao1)
  (:domain missao)
  (:objects
    m1 - missao
    c1 c2 c3 - cliente
    f1 - fato
    rowan - npc
    x - recompensa
  )
  (:init
    (missao-ativa m1)
    (= (clientes-contatados m1) 3)
    (= (progresso-historia m1) 6)
    (fornece c3 f1)
    (fato-obtido m1 f1)
    (fato-contado m1 f1 rowan)
    (recompensa-entregue m1 x)
  )
  (:goal (and
    (>= (clientes-contatados m1) 3)
    (fato-obtido m1 f1)
    (fato-contado m1 f1 rowan)
    (recompensa-entregue m1 x)
    (>= (progresso-historia m1) 3)
  ))
)
