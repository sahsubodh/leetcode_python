//: [Previous](@previous)

import Foundation
import SwiftUI

var greeting = "Hello, playground"

//: [Next](@next)


class CounterViewModel: ObservableObject {
    @Published var count = 0
    
    func increment() {
        count += 1
    }
}


struct CustomView: View {
    
    @StateObject var vm = CounterViewModel()
    
    var body: some View {
        VStack {
            Text("Count: \(vm.count)")
            Button("Increment:") {
                vm.increment()
            }
        }
        .padding()
    }
}
