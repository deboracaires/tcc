(define (domain cenas)
  (:requirements :strips :typing :fluents)
  (:types 
    magia objeto - entity)

  (:predicates 
    (learned ?m - magia)
    (aplicado ?m - magia ?obj - objeto)
    (diario-achado))

  (:functions 
    (progress-historia))

  ;; Ação para aprender a magiaA
  (:action aprender-magiaA
    :parameters ()
    :precondition (not (learned magiaA))
    :effect (learned magiaA))

  ;; Ação para aplicar a magiaA em um objeto (ex.: obja, objb ou objc)
  (:action aplicar-magiaA
    :parameters (?obj - objeto)
    :precondition (learned magiaA)
    :effect (aplicado magiaA ?obj))

  ;; Ação para achar o objeto diário
  (:action achar-diario
    :parameters ()
    :precondition (not (diario-achado))
    :effect (diario-achado))

  ;; Ação para conceder a recompensa da missão "arrrumarcenario 3obj":
  ;; incrementa o progresso da história se a magiaA foi aprendida e aplicada em obja, objb e objc.
  (:action recompensa-historia
    :parameters ()
    :precondition (and 
                    (learned magiaA)
                    (aplicado magiaA obja)
                    (aplicado magiaA objb)
                    (aplicado magiaA objc))
    :effect (increase (progress-historia) 1))
)
