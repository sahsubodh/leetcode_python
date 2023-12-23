import UIKit

struct Money : Hashable {
    var value:Int
    var currencyCode: String
    
    func hash(into hasher: inout Hasher) {
        hasher.combine(value)
        hasher.combine(currencyCode)
    }
}


//var money = Money(value: 20, currencyCode: "USD")
////Output: Money(value: 20, currencyCode: "USD")
//print(money)
//let closure = { [money]
//    money = Money(value: 200, currencyCode: "USD")
//}
//closure()
////Output: Money(value: 200, currencyCode: "USD")
//print(money)


var money = Money(value: 20, currencyCode: "USD")
//Output: Money(value: 20, currencyCode: "USD")
print(money)
let closure = { [money] in
      print(money)
}
money = Money(value: 200, currencyCode: "USD")
//Output: Money(value: 20, currencyCode: "USD")
closure()
//Output: Money(value: 200, currencyCode: "USD")
print(money)
