import UIKit
import SwiftUI

var greeting = "Hello, playground"


let queue = DispatchQueue(label: "test",attributes: .concurrent)

queue.async {
    print("Hi how are you")
}



struct Vehicle {
    static var wheels : Int {
        return 0
    }
}


print(Vehicle.wheels)

class Vehicles {
    class var wheels: Int {
        return 0
    }
}

print(Vehicles.wheels)



class CounterViewModel: ObservableObject {
    
    @Published var count: Int = 0
    
    func increment() {
        count += 1
    }
}


struct CustomView : View {
    
    @ObservedObject var cvm = CounterViewModel()
    
    var body: some View {
        Text("Count \(cvm.count)")
        
        Button("Increment") {
            cvm.increment()
        }
        .padding()
    }
}


class NetworkClient {
    
    init() {
        
    }
}

class ViewController: UIViewController {
    let networkClient: NetworkClient
    
    required init(networkClient: NetworkClient) {
        self.networkClient = networkClient
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    
    func fetchData(using networkClient: NetworkClient) {
        
    }
}


enum MyError: Error {
    case invalidInput
}

func divide(_ a: Int,_ b: Int) throws -> Int {
    guard b != 0 else {
        throw MyError.invalidInput
    }
    
    return a/b
}

do {
    let res = try divide(3, 0)
    print(res)
} catch let err {
    print(err)
}


func addOne(_ number: Int) throws -> Int {
    guard number >= 0 else {
        throw MyError.invalidInput
    }
    
    return number + 1
}


func manipulateArray(_ array: [Int], using closure: (Int) throws -> Int) rethrows -> [Int] {
    var res:[Int] = []
    for element in array {
        let transform = try closure(element)
        res.append(transform)
    }
    return res
}

let input = [1,2,3,4,5]

do {
    let result = try manipulateArray(input, using: addOne)
} catch let err {
    print(err)
}





let url = URL(string: "www.google.com")
let urlRequest = URLRequest(url: url!)

let config = URLSessionConfiguration.default

//let session = URLSession(configuration: config, delegate: self, delegateQueue: nil)
//session.downloadTask(with: url).resume()

class Vehicle1 {
    var color: String
    init(color: String) {
        self.color = color
    }
}

class Car: Vehicle1 {
    var numDoors: Int
    
    init(numDoors: Int, color: String) {
        self.numDoors = numDoors
        super.init(color: color)
    }
}
