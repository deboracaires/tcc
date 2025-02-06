(define (problem c0)
  (:domain cenas)
  (:objects
    magiaA - magia
    obja objb objc - objeto)
  (:init 
    (= (progress-historia) 0))
  (:goal 
    (and 
      (>= (progress-historia) 1)
      (diario-achado)))
)
