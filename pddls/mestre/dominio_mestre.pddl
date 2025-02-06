(define (domain jogo-custo)
  (:requirements :strips :typing :negative-preconditions)
  (:types ciclo mission day client inspector phase)
  (:predicates 
    (iniciado ?c - ciclo)
    (finalizado ?c - ciclo)
    (diario-preso)          ; verdadeiro se o diário foi pego
    (cenario-arrumado)       ; verdadeiro se o cenário foi arrumado
    (mission-done ?m - mission) ; missão concluída
    (client ?cl - client)
    (inspector ?i - inspector)
    (inspector-assigned ?cl - client)
    (current-phase ?p - phase)  ; indica em que fase o jogo está (p1, p2, p3, p4, etc.)
    (good-c0)                   ; verdadeiro se no ciclo 0 o diário e o cenário foram feitos
  )

  ;;; --- CICLO 0: Parte fixa (obrigatório pegar o diário e arrumar o cenário) ---

  (:action iniciar-c0
    :parameters ()
    :precondition (current-phase p1)
    :effect (iniciado c0)
  )

  (:action pegar-diario
    :parameters ()
    :precondition (and (current-phase p1) (iniciado c0) (not (diario-preso)))
    :effect (diario-preso)
  )

  (:action arrumar-cenario
    :parameters ()
    :precondition (and (current-phase p1) (iniciado c0) (not (cenario-arrumado)))
    :effect (cenario-arrumado)
  )

  ;; Se ambos foram feitos, finaliza o ciclo 0 com qualidade boa.
  (:action finalizar-c0-good
    :parameters ()
    :precondition (and (current-phase p1) (iniciado c0) (diario-preso) (cenario-arrumado))
    :effect (and (finalizado c0)
                 (not (current-phase p1))
                 (current-phase p2)
                 (good-c0))
  )

  ;; Se faltar o diário ou o cenário, finaliza o ciclo 0 sem qualidade boa.
  (:action finalizar-c0-bad
    :parameters ()
    :precondition (and (current-phase p1) (iniciado c0)
                       (or (not (diario-preso)) (not (cenario-arrumado))))
    :effect (and (finalizado c0)
                 (not (current-phase p1))
                 (current-phase p2))
  )

  ;;; --- CICLO 1: Opções para o mestre (por exemplo, duas missões) ---

  (:action iniciar-c1
    :parameters ()
    :precondition (current-phase p2)
    :effect (iniciado c1)
  )

  ;; Missão 1: versão de baixo custo (low) se ciclo 0 foi bem feito.
  (:action acao-c1-opcao1-low
    :parameters ()
    :precondition (and (current-phase p2) (iniciado c1) (good-c0) (not (mission-done mission1)))
    :effect (mission-done mission1)
  )

  ;; Missão 1: versão de alto custo (high) se ciclo 0 não foi bom.
  (:action acao-c1-opcao1-high
    :parameters ()
    :precondition (and (current-phase p2) (iniciado c1) (not (good-c0)) (not (mission-done mission1)))
    :effect (mission-done mission1)
  )

  ;; Missão 2: versão de baixo custo.
  (:action acao-c1-opcao2-low
    :parameters ()
    :precondition (and (current-phase p2) (iniciado c1) (good-c0) (not (mission-done mission2)))
    :effect (mission-done mission2)
  )

  ;; Missão 2: versão de alto custo.
  (:action acao-c1-opcao2-high
    :parameters ()
    :precondition (and (current-phase p2) (iniciado c1) (not (good-c0)) (not (mission-done mission2)))
    :effect (mission-done mission2)
  )

  ;; Finaliza o ciclo 1 (é necessário que pelo menos uma missão seja concluída).
  (:action finalizar-c1
    :parameters ()
    :precondition (and (current-phase p2) (iniciado c1)
                       (or (mission-done mission1) (mission-done mission2)))
    :effect (and (finalizado c1)
                 (not (current-phase p2))
                 (current-phase p3))
  )

  ;;; --- CICLO 2: Novas opções (por exemplo, duas outras missões) ---

  (:action iniciar-c2
    :parameters ()
    :precondition (current-phase p3)
    :effect (iniciado c2)
  )

  ;; Missão 3: versão de baixo custo se, por exemplo, missão1 foi concluída no ciclo 1.
  (:action acao-c2-opcao1-low
    :parameters ()
    :precondition (and (current-phase p3) (iniciado c2) (mission-done mission1) (not (mission-done mission3)))
    :effect (mission-done mission3)
  )

  ;; Missão 3: versão de alto custo se missão1 não foi concluída.
  (:action acao-c2-opcao1-high
    :parameters ()
    :precondition (and (current-phase p3) (iniciado c2) (not (mission-done mission1)) (not (mission-done mission3)))
    :effect (mission-done mission3)
  )

  ;; Missão 4: versão de baixo custo se, por exemplo, missão2 foi concluída.
  (:action acao-c2-opcao2-low
    :parameters ()
    :precondition (and (current-phase p3) (iniciado c2) (mission-done mission2) (not (mission-done mission4)))
    :effect (mission-done mission4)
  )

  ;; Missão 4: versão de alto custo se missão2 não foi concluída.
  (:action acao-c2-opcao2-high
    :parameters ()
    :precondition (and (current-phase p3) (iniciado c2) (not (mission-done mission2)) (not (mission-done mission4)))
    :effect (mission-done mission4)
  )

  (:action finalizar-c2
    :parameters ()
    :precondition (and (current-phase p3) (iniciado c2)
                       (or (mission-done mission3) (mission-done mission4)))
    :effect (and (finalizado c2)
                 (not (current-phase p3))
                 (current-phase p4))
  )
)
