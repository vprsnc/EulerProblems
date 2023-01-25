my.coins <- c(1,2,5,10,20,50,100,200)
my.coins.num <- length(my.coins)
my.money <- 200


find.change <- function(money, num.coins) {
    s <- 0
    range <- c(1:num.coins)

    for ( i in range ) {
        remaining <- money-my.coins[i]

        if( remaining == 0 )
            s <- s + 1

        if(remaining > 0)
            s <- s + find.change( remaining, i )
    }
    return(s)
}

my.change <- find.change(my.money, my.coins.num )

print(my.change)
