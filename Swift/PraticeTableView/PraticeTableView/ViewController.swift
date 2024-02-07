//
//  ViewController.swift
//  PraticeTableView
//
//  Created by Subodh Sah on 1/20/24.
//

import UIKit
import Combine

/*
 func load2() {
     guard let url = Bundle.main.url(forResource: "feed", withExtension: "txt") else {
         errorMessage = "Failed to find feed.txt in bundle."
         print("Error: \(errorMessage!)")
         return
     }

     URLSession.shared.dataTaskPublisher(for: url)
         .map { $0.data }
         .handleEvents(receiveOutput: { data in
             print("Received data: \(String(describing: String(data: data, encoding: .utf8)))")
         })
         .decode(type: [Restaurant].self, decoder: JSONDecoder())
         .sink(receiveCompletion: { completion in
             switch completion {
             case .failure(let error):
                 if let decodingError = error as? DecodingError {
                     print("Decoding Error: \(decodingError.localizedDescription)")
                     switch decodingError {
                     case .dataCorrupted(let context),
                          .keyNotFound(_, let context),
                          .typeMismatch(_, let context),
                          .valueNotFound(_, let context):
                         print("Decoding Error Context: \(context.debugDescription)")
                         print("Decoding Error Context CodingPath: \(context.codingPath.map { $0.stringValue })")
                     @unknown default:
                         fatalError("very wrong")
                     }
                 } else {
                     print("Other Error: \(error.localizedDescription)")
                 }
             case .finished:
                 break
             }
         },receiveValue: { [weak self] in
             print("Parsed restaurants: \($0)")
             self?.restaurants = $0
         })
         .store(in: &cancellables)
 }
 
 func load() {
     guard let url = Bundle.main.url(forResource: "feed", withExtension: "txt") else {
         errorMessage = "Failed to find feed.txt in bundle."
         print("Error: \(errorMessage!)")
         return
     }

     URLSession.shared.dataTaskPublisher(for: url)
         .map { $0.data }
         .handleEvents(receiveOutput: { data in
             print("Received data: \(String(describing: String(data: data, encoding: .utf8)))")
         })
         .decode(type: [Restaurant].self, decoder: JSONDecoder())
         .sink(receiveCompletion: { [weak self] completion in
             if case .failure(let error) = completion {
                 self?.errorMessage = error.localizedDescription
                 print("Error: \(error.localizedDescription)")
             }
         }, receiveValue: { [weak self] in
             print("Parsed restaurants: \($0)")
             self?.restaurants = $0
         })
         .store(in: &cancellables)
 }

 func load1() {
     guard let url = Bundle.main.url(forResource: "feed", withExtension: "txt") else {
         fatalError("Failed to find feed.txt in bundle.")
     }
                                     
     URLSession.shared.dataTaskPublisher(for: url)
         .map { $0.data }
         .decode(type: [Restaurant].self, decoder: JSONDecoder())
         .replaceError(with: [])
         .receive(on: DispatchQueue.main)
         .sink(receiveCompletion: { [weak self] completion in
             if case .failure(let error) = completion {
                 self?.errorMessage = error.localizedDescription
             }
         }, receiveValue: { [weak self] in
             print($0)
             self?.restaurants = $0
         })
         .store(in: &cancellables)
 }
 */

protocol NetworkServiceProtocol {
    func fetchRestaurants(completion: @escaping (Result<[Restaurant], Error>) -> Void)
}

//protocol ImageDownloading {
//    func downloadImage(for url: URL, completion: @escaping(UIImage?) -> Void)
//}

class NetworkService: NetworkServiceProtocol {
    
    private var cancellables = Set<AnyCancellable>()
    
    func fetchRestaurants(completion: @escaping (Result<[Restaurant], Error>) -> Void) {
        guard let url = Bundle.main.url(forResource: "feed", withExtension: "txt") else {
//            errorMessage = "Failed to find feed.txt in bundle."
//            print("Error: \(errorMessage!)")
            completion(.failure(NSError(domain: "", code: -1, userInfo: [NSLocalizedDescriptionKey: "Failed to find feed.txt in bundle."])))

            return
        }
        
        URLSession.shared.dataTaskPublisher(for: url)
            .map { $0.data }
            .decode(type: [Restaurant].self, decoder: JSONDecoder())
            .sink(receiveCompletion: {completionStatus in
                if  case .failure(let error) = completionStatus {
                    completion(.failure(error))
                }
            }, receiveValue: { resturants in
                completion(.success(resturants))
                
            })
        
        
        
//        URLSession.shared.dataTask(with: url) { data, response, error in
//            // Handle any errors from the network request
//            if let error = error {
//                DispatchQueue.main.async {
//                    completion(.failure(error))
//                }
//                return
//            }
//
//            guard let data = data else {
//                DispatchQueue.main.async {
//                    completion(.failure(URLError(.badServerResponse)))
//                }
//                return
//            }
//
//            // Optional: Print the received data
//            print("Received data: \(String(describing: String(data: data, encoding: .utf8)))")
//
//            // Decode the data
//            do {
//                let restaurants = try JSONDecoder().decode([Restaurant].self, from: data)
//                DispatchQueue.main.async {
//                    completion(.success(restaurants))
//                }
//            } catch {
//                DispatchQueue.main.async {
//                    completion(.failure(error))
//                }
//            }
//        }.resume()
//        
        

        URLSession.shared.dataTaskPublisher(for: url)
            .map { $0.data }
            .handleEvents(receiveOutput: { data in
                print("Received data: \(String(describing: String(data: data, encoding: .utf8)))")
            })
            .decode(type: [Restaurant].self, decoder: JSONDecoder())
            .sink(receiveCompletion: { completionStatus in
                if case .failure(let error) = completionStatus {
                    completion(.failure(error))
                }
            }, receiveValue: { restaurants in
                completion(.success(restaurants))
            })
            
            .store(in: &cancellables)
    }
}


class ResturantViewModel {
    
    private let networkService: NetworkServiceProtocol
    @Published var restaurants: [Restaurant] = []
    @Published var errorMessage: String?
    
    init(networkService: NetworkServiceProtocol = NetworkService()) {
        self.networkService = networkService
    }
    
    func loadRestaurants() {
        networkService.fetchRestaurants { [weak self] result in
            DispatchQueue.main.async {
                switch result {
                case .success(let restaurants):
                    self?.restaurants = restaurants
                case .failure(let error):
                    self?.errorMessage = error.localizedDescription
                }
            }
        }
    }
}

class ViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    
    @IBOutlet weak var tableView: UITableView!
    
    var viewModel: ResturantViewModel?
    var imageDownloader: ImageDownloader?
    private var cancellables = Set<AnyCancellable>()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        imageDownloader = ImageDownloader()
        viewModel = ResturantViewModel(networkService: NetworkService())
        self.tableView.dataSource = self
        self.tableView.delegate = self
        
//        self.tableView.rowHeight = UITableView.automaticDimension
//        self.tableView.estimatedRowHeight = 100
        
        self.tableView.register(RestaurantCell.nib(), forCellReuseIdentifier: "RestaurantCell")
        
        if let vm = viewModel {
            vm.loadRestaurants()
        }
        
        self.viewModel?.$restaurants
            .receive(on: DispatchQueue.main)
            .sink(receiveValue:  {[weak self]  _ in
                self?.tableView.reloadData()
        })
        .store(in: &cancellables)
        
        self.viewModel?.$errorMessage
            .receive(on: DispatchQueue.main)
            .sink {
            [weak self] errorMessage in
            if let message = errorMessage {
                self?.showError(message)
            }
        }
        .store(in: &cancellables)

        
    }

    private func showError(_ message: String) {
        let alert = UIAlertController(title: "error", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "Ok", style: .default))
        alert.addAction(UIAlertAction(title: "cancel", style: .cancel))
        self.present(alert, animated: true)
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return viewModel?.restaurants.count ?? 0
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: RestaurantCell.identifier, for: indexPath) as! RestaurantCell
        
        if let resturant = viewModel?.restaurants[indexPath.row] {
           cell.setFields(resturant.name, description: resturant.description)
        }

        return cell
    }
}
