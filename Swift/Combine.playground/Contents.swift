import UIKit
import Combine


var greeting = "Hello, playground"

/*
extension Notification.Name {
    static let newblogpost = Notification.Name("new_blog_post")
}

struct BlogPost {
    let title: String
    let url: URL
}


//let blogPublisher = NotificationCenter.Publisher(nam)
let blogPostPublisher = NotificationCenter.Publisher(center: .default, name: .newBlogPost, object: nil).map {
    (notification) -> String? in
    return (notification.object as? BlogPost)?.title ?? ""
}

let lastPostLabel = UILabel()
let lastPostLabelSubscriber = Subscribers.Assign(object: lastPostLabel, keyPath: \.text)

blogPostPublisher
    .subscribe(lastPostLabelSubscriber)



let blogPost = BlogPost(title: "Getting started with the Combine framework in Swift", url: URL(string: "https://www.avanderlee.com/swift/combine/")!)
NotificationCenter.default.post(name: .newBlogPost, object: blogPost)
print("Last post is: \(lastPostLabel.text!)")


final class FormViewController: UIViewController {
    
    @Published var isSubmitAllowed: Bool = false

    @IBOutlet private weak var acceptTermsSwitch: UISwitch!
    @IBOutlet private weak var submitButton: UIButton!

    override func viewDidLoad() {
        super.viewDidLoad()
        $isSubmitAllowed
            .receive(on: DispatchQueue.main)
            .assign(to: \.isEnabled, on: submitButton)
    }

    @IBAction func didSwitch(_ sender: UISwitch) {
        isSubmitAllowed = sender.isOn
    }
}

enum Log {
    enum LogLevel {
        case info
        case warning
        case error
        
        fileprivate var prefix: String {
            switch self {
            case .info:
                return "INFO"
            case .warning:
                return "WARNING"
            case .error:
                return "ERROR"
            }
        }
    }
    
    fileprivate static func handleLog(level: LogLevel, str: String, shouldLogContext: Bool, context: Context) {
        let logComponents = ["[\(level.prefix)]", str]
        var fullString = logComponents.joined(separator: " ")
        if shouldLogContext {
            fullString += "-> \(context.description)"
        }
        
#if DEBUG
        print(fullString)
#endif
    }
    
    struct Context {
        let file: String
        let function: String
        let line: Int
        
        var description: String {
            "\((file as NSString).lastPathComponent):\(line) \(function)"
        }
    }
    
    static func info(_ str: StaticString, shouldLogContext: Bool = true,
                     file: String = #file, function: String = #function,
                     line: Int = #line) {
        let context = Context(file: file, function: function, line: line)
        Log.handleLog(level: .info, str: str.description,
                      shouldLogContext: shouldLogContext, context: context)
    }
    
}

protocol AnalyticsProvider {
    func sendAnalyticsEvent(named name: String, metadata: [String: Any]?)
}

*/

escapingClosure {
    print("I'll execute 3 seconds after the function returns.")
}
nonEscapingClosure {
    print("This will be executed immediately.")
}
func escapingClosure(closure: @escaping (() -> ())) {
    DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
closure() }
}
func nonEscapingClosure(closure: (() -> ())) {
    // Some synchronous code...
    // Calls the closure immediately
    closure()
    // Some synchronous code...
}
print("test")
    


struct Money: Hashable {
    let value: Int
    let currencyCode: String
//    func hash(into hasher: inout Hasher) {
//        hasher.combine(value)
//        hasher.combine(currencyCode)
//    }
}


//class VisitorCount {
//    let queue = DispatchQueue(label: "test", attribues: .concurrent)
//    
//    private var visitorCount = 0
//    
//    func getVisitorCount() -> Int {
//        queue.sync {
//            return visitorCount
//        }
//    }
//    
//    func updateVisitorCount() {
//        queue.sync(flags: .barrier) {
//            visitorCount += 1
//        }
//    }
//}
//
//func deadLock() {
//    let queue = DispatchQueue(label: "deadlock-demo")
//    queue.async { // A
//        queue.async { // B
//            print("B: Waiting on A to finish.")
//        }
//        print("A: Waiting on B to finish.")
//    }
//    
////    queue.async { // A
////        queue.sync { // B
////            print("B: Waiting on A to finish.")
////        }
////        print("A: Waiting on B to finish.")
////    }
//}
//
//deadLock()


let queue1 = DispatchQueue(label: "com.example.queue1")
let queue2 = DispatchQueue(label: "com.example.queue2")

queue1.async {
    print("Task 1a")
    queue2.sync {
        print("Task 1b")
    }
    print("Task 1c")
}

queue2.async {
    print("Task 2a")
    queue1.sync {
        print("Task 2b")
    }
    print("Task 2c")
}
