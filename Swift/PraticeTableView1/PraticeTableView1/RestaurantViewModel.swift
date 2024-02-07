//
//  RestaurantViewModel.swift
//  PraticeTableView1
//
//  Created by Subodh Sah on 1/22/24.
//

import Foundation
import Combine


protocol NetworkServiceProtocol {
    func getResturants(completion: @escaping (Result<[Restaurant], Error>) -> Void)
}


class NetworkService: NetworkServiceProtocol {
    
    var cancellables = Set<AnyCancellable>()
    
    func getResturants(completion: @escaping (Result<[Restaurant], Error>) -> Void) {
        guard let url = Bundle.main.url(forResource: "feed", withExtension: "txt") else {
            
            let error = NSError(domain: "test", code: -1, userInfo: [NSLocalizedDescriptionKey.description: "Failed to open the feed file"])
            completion(.failure(error))
            return
        }
        
        URLSession.shared.dataTaskPublisher(for: url)
            .map { $0.data }
            .decode(type: [Restaurant].self, decoder: JSONDecoder())
            .sink(receiveCompletion: { completionStatus in
                if case .failure(let error) = completionStatus {
                    completion(.failure(error))
                }
                
            } , receiveValue: { restaurants in
                completion(.success(restaurants))
                
            }).store(in: &cancellables)
    }
}

class RestaurantViewModel {
    
    var networkService: NetworkServiceProtocol!
    
    @Published var resturants: [Restaurant] = []
    @Published var errorMessage: String?
    
    init(networkService: NetworkServiceProtocol = NetworkService()) {
        self.networkService = networkService
    }
    
    func fetchRestaurants() {
        networkService.getResturants(completion: { [weak self] result in
            DispatchQueue.main.async {
                switch result {
                case .success(let resturants):
                    self?.resturants = resturants
                case .failure(let error):
                    self?.errorMessage = error.localizedDescription
                }
            }
        })
    }
}
