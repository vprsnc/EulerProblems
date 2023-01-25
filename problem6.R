f <- function(range){

  x = c(1:range)

  return(sum(x)^2 - sum(x^2))
}


y <- f(100)

print(y)
