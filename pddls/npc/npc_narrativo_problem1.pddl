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
    (= (clientes-contatados m1) 0)
    (= (progresso-historia m1) 0)
    ;; Definindo que o cliente c3 fornece o fato f1 (correspondente à instrução "cliente 3 fato1")
    (fornece c3 f1)
  )
  (:goal
    (and
      ;; Meta: falar com 3 clientes (falar 3 clientes)
      (>= (clientes-contatados m1) 3)
      ;; Meta: obter o fato f1 do cliente (cliente 3 fato1)
      (fato-obtido m1 f1)
      ;; Meta: contar o fato f1 para rowan (contar fato1 rowan)
      (fato-contado m1 f1 rowan)
      ;; Meta: entregar a recompensa x (recompensa x)
      (recompensa-entregue m1 x)
      ;; Meta: progredir na história em +3 (progresso historia +3)
      (>= (progresso-historia m1) 3)
    )
  )
)
