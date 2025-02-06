(define (domain missao)
  (:requirements :strips :typing :fluents)
  (:types missao cliente fato npc recompensa)
  
  (:predicates
    (missao-ativa ?m - missao)
    (cliente-contatado ?m - missao ?c - cliente)
    (fornece ?c - cliente ?f - fato)      ; Indica que o cliente fornece o fato
    (fato-obtido ?m - missao ?f - fato)
    (fato-contado ?m - missao ?f - fato ?n - npc)
    (recompensa-entregue ?m - missao ?r - recompensa)
  )
  
  (:functions
    (clientes-contatados ?m - missao)      ; Contador de clientes contatados
    (progresso-historia ?m - missao)       ; Progresso da história (numérico)
  )
  
  ;; Ação para falar com um cliente
  (:action falar-com-cliente
    :parameters (?m - missao ?c - cliente)
    :precondition (missao-ativa ?m)
    :effect (and
              (cliente-contatado ?m ?c)
              (increase (clientes-contatados ?m) 1)
            )
  )
  
  ;; Ação para obter um fato de um cliente (por exemplo, cliente 3 fornece fato1)
  (:action obter-fato-do-cliente
    :parameters (?m - missao ?c - cliente ?f - fato)
    :precondition (and 
                    (cliente-contatado ?m ?c)
                    (fornece ?c ?f)
                  )
    :effect (fato-obtido ?m ?f)
  )
  
  ;; Ação para contar um fato a um NPC (por exemplo, contar fato1 para rowan)
  (:action contar-fato
    :parameters (?m - missao ?f - fato ?n - npc)
    :precondition (fato-obtido ?m ?f)
    :effect (fato-contado ?m ?f ?n)
  )
  
  ;; Ação para entregar a recompensa, uma vez que o fato foi contado
  (:action entregar-recompensa
    :parameters (?m - missao ?r - recompensa ?f - fato ?n - npc)
    :precondition (fato-contado ?m ?f ?n)
    :effect (recompensa-entregue ?m ?r)
  )
  
  ;; Ação para progredir a história (incrementa o progresso em +3)
  (:action progredir-historia
    :parameters (?m - missao)
    :precondition (missao-ativa ?m)
    :effect (increase (progresso-historia ?m) 3)
  )
)
