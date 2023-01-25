(setq max-lisp-eval-depth 10000)
(setq max-specpdl-size 10000)

(defun self-power-sum (x)
	(if (= x 0) 0
	(+ (expt x x) (self-power-series (- x 1)))))

(setq mylist
  (list(self-power-sum 1000)))

(message(substring (format "%s" mylist) -11 -1))
