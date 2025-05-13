// This is a quiz for the following sections:
// - Variables
// - Functions
// - If
//
// Mary is buying apples. The price of an apple is calculated as follows:
// - An apple costs 2 rustbucks.
// - However, if Mary buys more than 40 apples, the price of each apple in the
// entire order is reduced to only 1 rustbuck!

// TODO: Write a function that calculates the price of an order of apples given
// the quantity bought.
const APPLE_PRICE: u16 = 2;
const APPLE_DISCOUNT_PRICE: u16 = 1;
const DISCOUNT_THRESHOLD: u16 = 40;

fn calculate_price_of_apples(apples_bought: u16) -> u16 { 
    apples_bought * if apples_bought <= DISCOUNT_THRESHOLD { APPLE_PRICE } else { APPLE_DISCOUNT_PRICE }
}


fn main() {
    // You can optionally experiment here.
    println!("Price of 35 apples is : {}", calculate_price_of_apples(35));
    println!("Price of 40 apples is : {}", calculate_price_of_apples(40));
    println!("Price of 41 apples is : {}", calculate_price_of_apples(41));
    println!("Price of 65 apples is : {}", calculate_price_of_apples(65));
}

// Don't change the tests!
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn verify_test() {
        assert_eq!(calculate_price_of_apples(35), 70);
        assert_eq!(calculate_price_of_apples(40), 80);
        assert_eq!(calculate_price_of_apples(41), 41);
        assert_eq!(calculate_price_of_apples(65), 65);
    }
}
