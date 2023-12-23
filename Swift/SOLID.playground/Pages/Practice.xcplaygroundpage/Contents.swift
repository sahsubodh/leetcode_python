//: [Previous](@previous)

import Foundation
import UIKit
var greeting = "Hello, playground"

//: [Next](@next)

/*
func scrollViewDidScroll(_ scrollView : UIScrollView) {
    let offset = scrollView.contentOffset.y
    let contentHeight = scrollView.contentSize.height
    
    if offset > contentHeight - scrollView.frame.height {
        loadMoreData()
    }
}

func loadMoreData() {
    let newData  = fetchNewData()
    datasource.append(contentsOf: newData)
    
    tableView.reloadData()
}
 
 tableView.register(UITableViewCell.Self, forCellReuseIdentifier: "test")

 tableView.register(UINib(nibName: "test", bundle: nil), forCellReuseIdentifier: "test1")

 func tableView(_ tableView: UITableView, cellForRowAt indexpath: IndexPath) -> UITableViewCell {
     
     tableView.deque
 }
 
 protocol ProductFactory {
     func createProduct(for product: Product) -> UIViewController
 }

 class BookProductFactory: ProductFactory {
     func createProductViewController(for product: Product) -> UIViewController {
         let book = product as! Book
         let bookViewController = BookViewController()
         bookViewController.book = book
         return bookViewController
     }
 }

 class MainViewController: UIViewController {
     var productFactory: ProductFactory!
     var selectedProduct: Product!
     func showSelectedProduct() {
         let productViewController =
         productFactory.createProductViewController(for: selectedProduct)
         navigationController?.pushViewController(productViewController,
                                                  animated: true)
     }
 }
*//*

let serialQueue = DispatchQueue(label: "subodh.serial.queue")

serialQueue.async {
    print("Task 1 started")
    // Do some work..
    print("Task 1 finished")
}
serialQueue.async {
    print("Task 2 started")
    // Do some work..
    print("Task 2 finished")
}


let concurrentQueue = DispatchQueue(label: "swiftlee.concurrent.queue", attributes: .concurrent)

concurrentQueue.async(flags: .barrier) {
    print("Task 1 started")
    // Do some work..
    print("Task 1 finished")
}
concurrentQueue.async {
    print("Task 2 started")
    // Do some work..
    print("Task 2 finished")
}


if let url = URL(string: "https://example.com/image.png") {
    do {
        let data = try Data(contentsOf: url)
        let image = UIImage(data: data)
        // Use the downloaded image here
    } catch {
        // Handle the error here
    }
}

if let url = URL(string:"https://example.com/image.png") {
    let task = URLSession.shared.dataTask(with: url)  { data,response,error in
        if let data = data, let image = UIImage(data: data) {
            //downloaded image
        } else {
            //handle error
        }
    }
    
    task.resume()
}
*/




func incrementNumber() {
    var number = 5
    
    let workItem = DispatchWorkItem {
        number += 5
    }
    
    workItem.notify(queue: .main) {
        print("the new number is \(number)")
    }
}

let queuetest = DispatchQueue.global(qos: .utility)
queuetest.async {
    incrementNumber()
}


func sampleFunction() {
    // create a high-priority & a low-priority queue
    let highPriorityQueue = DispatchQueue.global(qos: .userInteractive)
    
    let lowPriorityQueue = DispatchQueue.global(qos: .utility)
    // create a high-priority work item
    
    let highPriorityWorkItem = DispatchWorkItem(qos: .userInteractive) {
        sleep(5)
        print("High-priority task completed")
    }
    // create a low-priority work item
    let lowPriorityWorkItem = DispatchWorkItem(qos: .utility) {
        sleep(5)
        print("Low-priority task completed")
    }
    // execute the work items asynchronously on their respective queues
    lowPriorityQueue.async(execute: lowPriorityWorkItem)
    highPriorityQueue.async(execute: highPriorityWorkItem)
}
sampleFunction()


let semaphore = DispatchSemaphore(value: 1)

func sendReq() {
    semaphore.wait()
    
    semaphore.signal()
}


let blockOperation = BlockOperation {
    print("Executing!")
}

let queue = OperationQueue()
queue.addOperation(blockOperation)


